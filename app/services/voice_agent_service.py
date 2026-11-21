"""
LookingForHome — Advanced AI Real Estate Voice & WhatsApp Agent
Conversational multi-turn engine with per-user session memory,
dynamic property recommendation, pagination ("más opciones"),
detailed property inspection, visit booking, and rent split calculations.
Connected to official WhatsApp support line: +34 603 331 391
"""

import re
import urllib.parse
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from app.models.database import get_properties, DBContext

AGENT_WHATSAPP_NUMBER = "+34603331391"
AGENT_WHATSAPP_CLEAN = "34603331391"

EUROPEAN_CITIES = [
    "madrid", "barcelona", "valencia", "sevilla", "málaga", "malaga",
    "bilbao", "zaragoza", "alicante", "granada", "berlin", "múnich", "munich",
    "hamburgo", "paris", "parís", "lyon", "marsella", "lisboa", "porto",
    "oporto", "dublín", "dublin", "roma", "milán", "milan", "ámsterdam",
    "amsterdam", "bruselas", "viena"
]


class UserSession:
    """Maintains multi-turn context and conversational state per phone/user."""

    def __init__(self, user_id: str, user_name: str = "Usuario"):
        self.user_id = user_id
        self.user_name = user_name or "Usuario"
        self.city: Optional[str] = None
        self.offset: int = 0
        self.last_properties: List[Dict[str, Any]] = []
        self.selected_property: Optional[Dict[str, Any]] = None
        self.budget_max: Optional[float] = None
        self.roommates_count: Optional[int] = None
        self.state: str = "idle"  # idle, browsing, viewing_detail, visit_pending_time, visit_confirmed
        self.last_visit_booking: Optional[Dict[str, Any]] = None
        self.last_activity = datetime.now()

    def touch(self):
        self.last_activity = datetime.now()


class HousingVoiceAgent:
    """
    State-of-the-art conversational voice & WhatsApp agent for LookingForHome.
    Maintains conversational memory, understands context, allows smooth pagination,
    displays structured property cards in WhatsApp, and schedules visits seamlessly.
    """

    def __init__(self):
        self.whatsapp_number = AGENT_WHATSAPP_NUMBER
        self.clean_whatsapp = AGENT_WHATSAPP_CLEAN
        self.sessions: Dict[str, UserSession] = {}

    def get_or_create_session(self, user_id: Optional[str], user_name: Optional[str] = None) -> UserSession:
        uid = str(user_id or "anonymous_guest").strip()
        # Clean older sessions (> 24h)
        now = datetime.now()
        expired = [k for k, s in self.sessions.items() if (now - s.last_activity).total_seconds() > 86400]
        for k in expired:
            del self.sessions[k]

        if uid not in self.sessions:
            self.sessions[uid] = UserSession(uid, user_name or "Usuario")
        else:
            if user_name and user_name != "Usuario":
                self.sessions[uid].user_name = user_name
            self.sessions[uid].touch()

        return self.sessions[uid]

    def process_query(
        self,
        message: str,
        lang: str = "es",
        user_id: Optional[str] = None,
        user_name: Optional[str] = None,
        channel: str = "whatsapp"
    ) -> Dict[str, Any]:
        """
        Processes any user message with full multi-turn awareness.
        channel can be 'whatsapp' or 'web'.
        """
        session = self.get_or_create_session(user_id, user_name)
        msg_raw = (message or "").strip()
        msg_clean = msg_raw.lower()

        # 1. Detect greetings / presentation
        if any(msg_clean == w or msg_clean.startswith(f"{w} ") for w in [
            "hola", "buenas", "buenos dias", "buenos días", "buenas tardes",
            "buenas noches", "hello", "hi", "hey", "bonjour", "hallo"
        ]):
            return self._handle_greeting(session, lang, channel)

        # 2. Detect "Muestrame mas opciones" / "Tienes mas?" / Pagination
        more_keywords = [
            "mas opciones", "más opciones", "muestrame mas", "muéstrame más",
            "tienes mas", "tienes más", "ver mas", "ver más", "siguiente",
            "siguientes", "otras opciones", "otro piso", "hay mas", "hay más",
            "mostrar mas", "mostrar más", "otra opcion", "otra opción", "next"
        ]
        if any(k in msg_clean for k in more_keywords):
            return self._handle_more_options(session, lang, channel)

        # 3. Detect option selection (1, 2, 3, "la 1", "el segundo", etc.)
        selection_idx = self._extract_selection_index(msg_clean)
        if selection_idx is not None and session.last_properties:
            return self._handle_select_property(session, selection_idx, lang, channel)

        # 4. Detect Visit Scheduling (e.g. "mañana a las 17h", "el viernes por la tarde")
        if self._is_visit_request(msg_clean):
            return self._handle_visit_scheduling(session, msg_raw, lang, channel)

        # 5. Detect City / Property search intent
        matched_city = None
        for city in EUROPEAN_CITIES:
            # check word boundary
            if re.search(rf"\b{re.escape(city)}\b", msg_clean):
                matched_city = city.capitalize()
                # normalize accents
                if matched_city in ["Munich", "Múnich"]:
                    matched_city = "Múnich"
                elif matched_city in ["Paris", "París"]:
                    matched_city = "París"
                elif matched_city in ["Malaga", "Málaga"]:
                    matched_city = "Málaga"
                break

        # Check for bedroom count request
        beds_match = re.search(r"(\d+)\s*(habitaciones|dormitorios|habs|cuartos|rooms)", msg_clean)
        bedrooms = int(beds_match.group(1)) if beds_match else None

        # Check for budget filter
        budget_match = re.search(r"(\d{3,4})\s*(€|euros|euro)", msg_clean)
        budget_max = float(budget_match.group(1)) if budget_match else None

        if matched_city or (session.city and any(w in msg_clean for w in ["piso", "habitacion", "habitación", "dormitorio", "alquiler", "barrio", "zona", "centro"])):
            target_city = matched_city or session.city
            return self._handle_city_search(session, target_city, bedrooms, budget_max, lang, channel)

        # 6. Detect Rent-Split Calculator / Roommates intent
        calc_match = re.search(r"(\d+)\s*(personas|amigos|habitaciones|habs|compañeros|roommates)", msg_clean)
        if any(w in msg_clean for w in ["calcular", "cuota", "reparto", "cuanto pagaria", "cuánto pagaría", "divid"]) or (calc_match and budget_match):
            roommates = int(calc_match.group(1)) if calc_match else (session.roommates_count or 4)
            total_rent = float(budget_match.group(1)) if budget_match else 1800.0
            return self._handle_calculator(session, roommates, total_rent, lang, channel)

        # 7. Detect FAQs & Policies (Fianza, Gastos incluidos, Mascotas, Contratos)
        faq_response = self._handle_faqs(session, msg_clean, lang, channel)
        if faq_response:
            return faq_response

        # 8. Detect Direct WhatsApp / Human Agent Request
        if any(w in msg_clean for w in ["humano", "persona", "operador", "llamar", "telefono", "teléfono"]):
            return self._handle_human_request(session, lang, channel)

        # 9. Dynamic Contextual Fallback
        return self._handle_dynamic_fallback(session, msg_raw, lang, channel)

    # ── HANDLERS ─────────────────────────────────────────────────────────────

    def _handle_greeting(self, session: UserSession, lang: str, channel: str) -> Dict[str, Any]:
        session.state = "browsing"
        user_greet = f"¡Hola, {session.user_name}!" if session.user_name != "Usuario" else "¡Hola!"

        if channel == "whatsapp":
            reply = (
                f"{user_greet} Te saluda el Asistente Inteligente de *LookingForHome* 🏡\n\n"
                "Te ayudo a encontrar pisos compartidos de calidad y coordinar visitas en las principales ciudades de Europa:\n"
                "• 🇪🇸 *España:* Barcelona, Madrid, Valencia, Sevilla, Málaga\n"
                "• 🇫🇷 *Francia:* París, Lyon\n"
                "• 🇩🇪 *Alemania:* Berlín, Múnich\n"
                "• 🇵🇹 *Portugal:* Lisboa, Oporto\n\n"
                "¿En qué ciudad te gustaría vivir o cuál es tu presupuesto mensual?"
            )
        else:
            reply = (
                f"{user_greet} Soy el Agente de Voz de LookingForHome. "
                "Puedo buscarte pisos para compartir en Barcelona, Madrid, Valencia, París o Berlín, "
                "calcular cuánto pagarías por persona y agendar visitas. ¿En qué ciudad te gustaría encontrar vivienda?"
            )

        return {
            "reply_text": reply,
            "action": "greeting",
            "whatsapp_url": self.build_whatsapp_link("Hola LookingForHome, quiero información sobre pisos compartidos."),
            "suggested_properties": []
        }

    def _handle_city_search(
        self,
        session: UserSession,
        city: str,
        bedrooms: Optional[int],
        budget_max: Optional[float],
        lang: str,
        channel: str
    ) -> Dict[str, Any]:
        session.city = city
        session.offset = 0
        if bedrooms:
            session.roommates_count = bedrooms
        if budget_max:
            session.budget_max = budget_max

        props = self._query_properties(city=city, bedrooms=bedrooms, max_rent_per_person=budget_max)
        if not props and (bedrooms or budget_max):
            # Relax filters if too restrictive
            props = self._query_properties(city=city)

        if not props:
            # Fallback to general properties
            props = get_properties()[:6]

        session.last_properties = props[:3]
        total_found = len(props)

        if channel == "whatsapp":
            items_text = []
            for i, p in enumerate(session.last_properties, 1):
                rent_p = round(p.get("rent_per_person", 450))
                total = round(p.get("total_rent", 1800))
                beds = p.get("bedrooms", 4)
                surface = p.get("surface_sqm", 110)
                items_text.append(
                    f"*{i}️⃣ {p.get('title')}*\n"
                    f"📍 {p.get('address') or p.get('city')}\n"
                    f"🛏️ {beds} habs | 📐 {surface} m² | 💶 *{rent_p}€/mes por persona* (Total: {total}€)"
                )

            cards = "\n\n".join(items_text)
            reply = (
                f"🏙️ *Viviendas disponibles en {city} ({total_found} encontradas):*\n\n"
                f"{cards}\n\n"
                "👉 *¿Cómo quieres continuar?*\n"
                "• Escribe *1*, *2* o *3* para ver la ficha completa y fotos del piso.\n"
                "• Escribe *\"más opciones\"* para ver los siguientes pisos disponibles.\n"
                "• O indícame si buscas un presupuesto o barrio en particular."
            )
        else:
            best = session.last_properties[0]
            rent_p = round(best.get("rent_per_person", 450))
            reply = (
                f"He encontrado excelentes opciones en {city}. "
                f"Por ejemplo: '{best.get('title')}', con {best.get('bedrooms')} habitaciones por solo {rent_p}€ por persona al mes. "
                f"Te he resaltado {len(session.last_properties)} opciones en pantalla. "
                "Escribe el número de la opción o pide 'más opciones' para ver el resto."
            )

        return {
            "reply_text": reply,
            "action": "property_recommendations",
            "city": city,
            "suggested_properties": session.last_properties,
            "offset": session.offset,
            "total_count": total_found
        }

    def _handle_more_options(self, session: UserSession, lang: str, channel: str) -> Dict[str, Any]:
        target_city = session.city or "Barcelona"
        session.offset += 3

        all_props = self._query_properties(city=target_city)
        if not all_props:
            all_props = get_properties()

        # Check if offset is beyond available listings
        if session.offset >= len(all_props):
            session.offset = 0  # Loop back to beginning or suggest another city
            next_props = all_props[:3]
            wrapped = True
        else:
            next_props = all_props[session.offset:session.offset + 3]
            wrapped = False

        session.last_properties = next_props

        if channel == "whatsapp":
            items_text = []
            for i, p in enumerate(next_props, 1):
                rent_p = round(p.get("rent_per_person", 450))
                total = round(p.get("total_rent", 1800))
                beds = p.get("bedrooms", 4)
                surface = p.get("surface_sqm", 110)
                items_text.append(
                    f"*{i}️⃣ {p.get('title')}*\n"
                    f"📍 {p.get('address') or p.get('city')}\n"
                    f"🛏️ {beds} habs | 📐 {surface} m² | 💶 *{rent_p}€/mes por persona* (Total: {total}€)"
                )

            cards = "\n\n".join(items_text)
            header = f"🔄 *Otras {len(next_props)} opciones destacadas en {target_city}:*" if not wrapped else f"🔄 *Has recorrido todas las opciones en {target_city}. Aquí tienes las más populares:*"

            reply = (
                f"{header}\n\n"
                f"{cards}\n\n"
                "👉 Responde con *1*, *2* o *3* para ver detalles y coordinar visita, o escribe otra ciudad (ej: *Madrid*, *Valencia*, *Berlín*)."
            )
        else:
            best = next_props[0]
            rent_p = round(best.get("rent_per_person", 450))
            reply = (
                f"Aquí tienes más opciones en {target_city}. Por ejemplo: '{best.get('title')}', "
                f"por solo {rent_p}€ por persona. Te he actualizado los resultados en pantalla."
            )

        return {
            "reply_text": reply,
            "action": "property_recommendations",
            "city": target_city,
            "suggested_properties": next_props,
            "offset": session.offset
        }

    def _handle_select_property(
        self,
        session: UserSession,
        idx: int,
        lang: str,
        channel: str
    ) -> Dict[str, Any]:
        if idx < 0 or idx >= len(session.last_properties):
            idx = 0

        prop = session.last_properties[idx]
        session.selected_property = prop
        session.state = "viewing_detail"

        title = prop.get("title", "Piso en alquiler")
        city = prop.get("city", "Barcelona")
        address = prop.get("address", city)
        beds = prop.get("bedrooms", 4)
        baths = prop.get("bathrooms", 2)
        surface = prop.get("surface_sqm", 110)
        total_rent = round(prop.get("total_rent", 1800))
        rent_p = round(prop.get("rent_per_person", 450))
        desc = prop.get("description", "Vivienda totalmente equipada para minicomunidad.")
        if len(desc) > 220:
            desc = desc[:217] + "..."

        features = []
        if prop.get("has_elevator"):
            features.append("Ascensor")
        if prop.get("is_exterior"):
            features.append("Exterior con mucha luz")
        if prop.get("is_furnished"):
            features.append("Amueblado completo")
        if prop.get("has_terrace"):
            features.append("Balcón / Terraza")
        if prop.get("has_air_con"):
            features.append("Climatización")
        features_str = " • ".join(features) if features else "Amueblado y reformado"

        contact = prop.get("contact_name", "Equipo LookingForHome")

        if channel == "whatsapp":
            reply = (
                f"✨ *Detalles de la Opción {idx + 1}:*\n"
                f"🏠 *{title}*\n\n"
                f"📍 *Ubicación:* {address}, {city}\n"
                f"💶 *Cuota individual:* *{rent_p}€/mes por persona*\n"
                f"💰 *Alquiler total:* {total_rent}€/mes ({beds} habitaciones y {baths} baños)\n"
                f"📐 *Superficie:* {surface} m²\n"
                f"🛋️ *Equipamiento:* {features_str}\n"
                f"📋 *Descripción:* {desc}\n"
                f"👤 *Gestión directa:* {contact}\n\n"
                "📅 *¿Deseas concertar una visita (presencial o por videollamada)?*\n"
                "Dime qué día y hora te viene bien (por ejemplo: *\"Mañana a las 17:00\"* o *\"El viernes por la mañana\"*) y te la agendo ahora mismo."
            )
        else:
            reply = (
                f"Has seleccionado '{title}' en {city}. Tiene {beds} habitaciones y {baths} baños por {rent_p}€ por persona. "
                "¿Te gustaría agendar una visita presencial o virtual? Dime qué día te va mejor."
            )

        return {
            "reply_text": reply,
            "action": "property_detail",
            "property": prop,
            "suggested_properties": [prop]
        }

    def _handle_visit_scheduling(
        self,
        session: UserSession,
        raw_msg: str,
        lang: str,
        channel: str
    ) -> Dict[str, Any]:
        # If no property has been chosen yet, take the first from last_properties
        if not session.selected_property and session.last_properties:
            session.selected_property = session.last_properties[0]

        target_prop = session.selected_property
        prop_title = target_prop.get("title", "Vivienda compartida") if target_prop else "Piso seleccionado"
        prop_city = target_prop.get("city", session.city or "Barcelona") if target_prop else "tu ciudad elegida"
        prop_addr = target_prop.get("address", "") if target_prop else ""

        # Extract time / date mention
        schedule_time = raw_msg
        session.state = "visit_confirmed"
        session.last_visit_booking = {
            "property_title": prop_title,
            "city": prop_city,
            "time": schedule_time,
            "user": session.user_name,
            "phone": session.user_id,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if channel == "whatsapp":
            reply = (
                "✅ *¡Visita Pre-Agendada con Éxito!*\n\n"
                f"🏠 *Vivienda:* {prop_title}\n"
                f"📍 *Dirección:* {prop_addr or prop_city}\n"
                f"🕒 *Horario solicitado:* {schedule_time}\n"
                f"👤 *Titular:* {session.user_name} ({session.user_id})\n\n"
                "Uno de nuestros coordinadores locales se pondrá en contacto contigo por este mismo chat de WhatsApp "
                "para confirmar los detalles del acceso y enviarte la ficha técnica.\n\n"
                "¿Deseas consultar algo más sobre la fianza, las habitaciones o ver otras opciones?"
            )
        else:
            reply = (
                f"¡Excelente! He registrado tu solicitud de visita para '{prop_title}' en el horario '{schedule_time}'. "
                "Nuestro equipo te contactará para confirmar."
            )

        return {
            "reply_text": reply,
            "action": "visit_booked",
            "booking": session.last_visit_booking
        }

    def _handle_calculator(
        self,
        session: UserSession,
        roommates: int,
        total_rent: float,
        lang: str,
        channel: str
    ) -> Dict[str, Any]:
        roommates = max(1, roommates)
        per_person = round(total_rent / roommates)
        savings = max(0, 950 - per_person)
        session.roommates_count = roommates

        if channel == "whatsapp":
            reply = (
                f"🧮 *Cálculo de Reparto de Alquiler:*\n\n"
                f"• *Alquiler total del piso:* {int(total_rent)}€/mes\n"
                f"• *Número de compañeros:* {roommates} personas\n"
                f"• *Cuota individual:* 👉 *{per_person}€/mes por persona*\n"
                f"• *Ahorro estimado frente a vivir solo:* ~{savings}€ al mes por persona 🚀\n\n"
                f"¿Quieres que te muestre los mejores pisos de {roommates} habitaciones disponibles en {session.city or 'Barcelona o Madrid'} que encajen con esta cuota?"
            )
        else:
            reply = (
                f"Para un alquiler de {int(total_rent)}€ entre {roommates} personas, cada uno pagaría {per_person}€ al mes, "
                f"ahorrando unos {savings}€ respecto a alquilar un estudio individual."
            )

        return {
            "reply_text": reply,
            "action": "calculator_result",
            "per_person": per_person,
            "total_rent": total_rent,
            "roommates": roommates
        }

    def _handle_faqs(self, session: UserSession, msg: str, lang: str, channel: str) -> Optional[Dict[str, Any]]:
        # Fianza / Garantías
        if any(w in msg for w in ["fianza", "deposito", "depósito", "garantia", "garantía"]):
            reply = (
                "🔒 *Información sobre la Fianza y Depósito:*\n\n"
                "• La fianza estándar es de *1 mes de alquiler*, depositada legalmente en el organismo oficial de la comunidad (ej: INCASÒL en Cataluña o IVIMA en Madrid).\n"
                "• Se devuelve íntegramente al finalizar el contrato tras la revisión de la vivienda.\n"
                "• En LookingForHome no cobramos comisión de agencia abusiva a los inquilinos.\n\n"
                "¿Te gustaría ver las viviendas disponibles o consultar sobre los suministros?"
            )
            return {"reply_text": reply, "action": "faq_fianza"}

        # Gastos y suministros (Luz, agua, wifi)
        if any(w in msg for w in ["gastos", "suministros", "luz", "agua", "internet", "wifi"]):
            reply = (
                "💡 *Gastos y Suministros Incluidos:*\n\n"
                "• En la mayoría de nuestras minicomunidades, los gastos (agua, luz, gas y fibra óptica de alta velocidad) se reparten a partes iguales.\n"
                "• La media suele rondar entre *35€ y 50€ al mes por persona*.\n"
                "• Muchos pisos cuentan con internet WiFi ya activo desde el primer día.\n\n"
                "¿Buscas piso en alguna ciudad específica?"
            )
            return {"reply_text": reply, "action": "faq_gastos"}

        # Mascotas
        if any(w in msg for w in ["mascota", "mascotas", "perro", "perros", "gato", "gatos"]):
            reply = (
                "🐾 *Política de Mascotas:*\n\n"
                "La admisión de mascotas depende de cada propietario y del acuerdo entre los compañeros de piso.\n"
                "Indícanos qué piso te interesa o en qué ciudad buscas y te filtraremos los que aceptan animales sin coste adicional."
            )
            return {"reply_text": reply, "action": "faq_mascotas"}

        # Cómo funciona LookingForHome
        if any(w in msg for w in ["como funciona", "cómo funciona", "que es lookingforhome", "qué es lookingforhome"]):
            reply = (
                "🏡 *¿Cómo funciona LookingForHome?*\n\n"
                "1. *Búsqueda:* Te conectamos con pisos grandes y luminosos en las mejores zonas de Europa.\n"
                "2. *Reparto Justo:* Dividimos el alquiler legalmente entre 3 a 5 compañeros para que pagues desde solo 380€ - 490€/mes.\n"
                "3. *Visita y Reserva:* Coordinamos visitas presenciales o por videollamada y formalizamos contratos protegidos.\n\n"
                "Dime en qué ciudad buscas vivienda para empezar."
            )
            return {"reply_text": reply, "action": "faq_info"}

        return None

    def _handle_human_request(self, session: UserSession, lang: str, channel: str) -> Dict[str, Any]:
        if channel == "whatsapp":
            reply = (
                "👩‍💼 *Atención Directa:*\n\n"
                "Ya estás conectado a la línea oficial de LookingForHome. "
                "Uno de nuestros asesores inmobiliarios humanos revisará la conversación y te responderá por este mismo chat en breve si necesitas asistencia personalizada.\n\n"
                "Mientras tanto, puedes seguir preguntándome sobre pisos, zonas, precios o solicitar visitas."
            )
        else:
            reply = (
                f"Puedes escribir directamente a nuestro equipo por WhatsApp al {self.whatsapp_number} "
                "para atención personalizada inmediata."
            )

        return {"reply_text": reply, "action": "human_requested"}

    def _handle_dynamic_fallback(self, session: UserSession, raw_msg: str, lang: str, channel: str) -> Dict[str, Any]:
        city_hint = f" en *{session.city}*" if session.city else ""
        if channel == "whatsapp":
            reply = (
                f"He recibido tu consulta: *\"{raw_msg}\"*\n\n"
                f"Para ayudarte de la mejor manera, puedes decirme:\n"
                f"• Una ciudad: *Barcelona*, *Madrid*, *Valencia*, *París*, *Berlín*...\n"
                f"• Pedir *\"más opciones\"*{city_hint}\n"
                "• Escribir el número de una opción (*1*, *2* o *3*) para ver fotos y concertar visita\n"
                "• Tu presupuesto máximo (ej: *\"busco piso por 450€\"*)\n"
                "• O preguntar por *fianza*, *gastos* o *reparto de alquiler*."
            )
        else:
            reply = (
                "LookingForHome te permite acceder a vivienda compartida de calidad en Europa. "
                "Dime en qué ciudad buscas o qué presupuesto tienes para recomendarte las mejores opciones."
            )

        return {"reply_text": reply, "action": "fallback"}

    # ── HELPERS ───────────────────────────────────────────────────────────────

    def _query_properties(
        self,
        city: Optional[str] = None,
        bedrooms: Optional[int] = None,
        max_rent_per_person: Optional[float] = None
    ) -> List[Dict[str, Any]]:
        try:
            return get_properties(
                city=city,
                min_bedrooms=bedrooms,
                max_rent_per_person=max_rent_per_person
            )
        except Exception as e:
            print(f"[VoiceAgent] Error querying properties: {e}")
            return get_properties()

    def _extract_selection_index(self, msg: str) -> Optional[int]:
        # exact single digit
        if msg in ["1", "1️⃣", "primero", "primera", "el 1", "la 1", "opcion 1", "opción 1", "el primero", "la primera"]:
            return 0
        if msg in ["2", "2️⃣", "segundo", "segunda", "el 2", "la 2", "opcion 2", "opción 2", "el segundo", "la segunda"]:
            return 1
        if msg in ["3", "3️⃣", "tercero", "tercera", "el 3", "la 3", "opcion 3", "opción 3", "el tercero", "la tercera"]:
            return 2

        # regex matches
        m1 = re.search(r"\b(la|el|opcion|opción)?\s*1\b", msg)
        if m1 and "10" not in msg and "11" not in msg and "12" not in msg:
            return 0
        m2 = re.search(r"\b(la|el|opcion|opción)?\s*2\b", msg)
        if m2 and "20" not in msg and "21" not in msg:
            return 1
        m3 = re.search(r"\b(la|el|opcion|opción)?\s*3\b", msg)
        if m3 and "30" not in msg:
            return 2

        return None

    def _is_visit_request(self, msg: str) -> bool:
        time_words = [
            "mañana", "hoy", "lunes", "martes", "miercoles", "miércoles",
            "jueves", "viernes", "sabado", "sábado", "domingo", "tarde",
            "mañana por", "a las", "hora", "17h", "18h", "19h", "16h", "10h",
            "11h", "12h", "visita", "visitar", "agendar", "cita"
        ]
        return any(w in msg for w in time_words) and ("visita" in msg or "a las" in msg or "por la tarde" in msg or "por la mañana" in msg or "quiero ver" in msg)

    def build_whatsapp_link(self, message: str) -> str:
        encoded = urllib.parse.quote(message)
        return f"https://wa.me/{self.clean_whatsapp}?text={encoded}"


# Global singleton instance
voice_agent = HousingVoiceAgent()

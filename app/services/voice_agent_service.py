"""
LookingForHome — AI Voice Agent Service
Autonomous Voice Assistant for European Shared Housing & Rent-Splitter.
Connected to official WhatsApp support line: +34 603 331 391
"""

import re
import urllib.parse
from typing import Dict, Any, List, Optional
from app.models.database import get_properties

AGENT_WHATSAPP_NUMBER = "+34603331391"
AGENT_WHATSAPP_CLEAN = "34603331391"

class HousingVoiceAgent:
    """
    Intelligent conversational voice agent that understands European housing inquiries,
    recommends flats, calculates per-person splits, and connects users directly
    to WhatsApp +34 603 331 391 for automated voice notes, visits, and reservations.
    """

    def __init__(self):
        self.whatsapp_number = AGENT_WHATSAPP_NUMBER
        self.clean_whatsapp = AGENT_WHATSAPP_CLEAN

    def process_query(self, message: str, lang: str = "es") -> Dict[str, Any]:
        msg_clean = (message or "").strip().lower()
        
        # 1. Detect greetings
        if any(w in msg_clean for w in ["hola", "buenos días", "buenas tardes", "hello", "hi", "bonjour", "hallo"]):
            return self._greeting_response(lang)

        # 2. Detect WhatsApp / Call intent
        if any(w in msg_clean for w in ["whatsapp", "wsp", "wasap", "teléfono", "llamar", "contactar", "agente", "humano", "número"]):
            return self._whatsapp_direct_response(lang, "Solicito información general o asistencia directa")

        # 3. Detect Calculator / Split Rent intent
        calc_match = re.search(r"(\d+)\s*(personas|amigos|habitaciones|habs|compañeros)", msg_clean)
        price_match = re.search(r"(\d{3,5})\s*(€|euros|euro)", msg_clean)
        if "calcular" in msg_clean or "cuota" in msg_clean or "reparto" in msg_clean or (calc_match and price_match):
            roommates = int(calc_match.group(1)) if calc_match else 4
            total_rent = float(price_match.group(1)) if price_match else 1800.0
            return self._calculator_response(roommates, total_rent, lang)

        # 4. Detect City / Property search intent
        cities = ["madrid", "barcelona", "valencia", "sevilla", "málaga", "bilbao", "berlin", "múnich", "munich", "paris", "lyon", "lisboa", "porto", "dublín", "dublin", "roma", "milán", "milan", "ámsterdam", "amsterdam"]
        matched_city = None
        for city in cities:
            if city in msg_clean:
                matched_city = city.capitalize()
                break

        # Check for bedroom count request
        beds_match = re.search(r"(\d+)\s*(habitaciones|dormitorios|habs|cuartos)", msg_clean)
        bedrooms = int(beds_match.group(1)) if beds_match else None

        if matched_city or "piso" in msg_clean or "casa" in msg_clean or "alquiler" in msg_clean or "habitacion" in msg_clean:
            return self._property_search_response(matched_city, bedrooms, lang)

        # 5. Default Fallback intelligent advice
        return self._general_advice_response(message, lang)

    def _greeting_response(self, lang: str) -> Dict[str, Any]:
        if lang == "en":
            reply = (
                "Hello! I am your LookingForHome AI Voice Assistant. "
                "You can ask me to find shared flats in Madrid, Barcelona, Paris or Berlin, "
                "calculate individual rent splits, or speak with our team directly on WhatsApp +34 603 331 391. "
                "What city or budget are you looking for?"
            )
        else:
            reply = (
                "¡Hola! Soy tu Agente de Voz de LookingForHome. "
                "Puedo buscarte pisos para compartir en Madrid, Barcelona, Valencia, París o Berlín, "
                "calcular cuánto pagarías por persona, o conectarte de inmediato con nuestro WhatsApp oficial +34 603 331 391. "
                "¿En qué ciudad te gustaría encontrar vivienda?"
            )

        wa_url = self.build_whatsapp_link("Hola Agente de Voz de LookingForHome, quiero información para buscar piso compartido.")
        return {
            "reply_text": reply,
            "action": "greeting",
            "whatsapp_url": wa_url,
            "whatsapp_display": self.whatsapp_number,
            "suggested_properties": []
        }

    def _whatsapp_direct_response(self, lang: str, reason: str) -> Dict[str, Any]:
        wa_text = f"Hola, vengo desde la web de LookingForHome. {reason}. Necesito asistencia del agente IA."
        wa_url = self.build_whatsapp_link(wa_text)

        if lang == "en":
            reply = (
                f"You can connect directly with our AI agent and human coordinator on WhatsApp at {self.whatsapp_number}. "
                "You can send voice notes or text messages anytime for instant property details and visit bookings!"
            )
        else:
            reply = (
                f"Puedes hablar directamente con nuestro agente IA y coordinadores en el WhatsApp {self.whatsapp_number}. "
                "Pulsa el botón de WhatsApp o envíanos una nota de voz para concertar visitas o consultar disponibilidad en tiempo real."
            )

        return {
            "reply_text": reply,
            "action": "open_whatsapp",
            "whatsapp_url": wa_url,
            "whatsapp_display": self.whatsapp_number,
            "suggested_properties": []
        }

    def _calculator_response(self, roommates: int, total_rent: float, lang: str) -> Dict[str, Any]:
        roommates = max(1, roommates)
        per_person = round(total_rent / roommates)
        savings = max(0, 950 - per_person)

        if lang == "en":
            reply = (
                f"For a total rent of {int(total_rent)}€ shared among {roommates} people, "
                f"each person pays only {per_person}€ per month! "
                f"Compared to living alone in Europe, you save approximately {savings}€ every month. "
                f"Would you like me to connect you with our WhatsApp {self.whatsapp_number} to reserve a flat with this quota?"
            )
        else:
            reply = (
                f"Para un alquiler total de {int(total_rent)}€ compartido entre {roommates} personas, "
                f"cada persona pagaría solo {per_person}€ al mes. "
                f"¡Esto supone un ahorro de unos {savings}€ mensuales frente a un alquiler individual! "
                f"¿Deseas que te reservemos plazas para este reparto en el WhatsApp {self.whatsapp_number}?"
            )

        wa_text = f"Hola, quiero reservar plazas para un reparto de {total_rent}€ entre {roommates} personas ({per_person}€/mes) en LookingForHome."
        return {
            "reply_text": reply,
            "action": "calculator_result",
            "per_person": per_person,
            "total_rent": total_rent,
            "roommates": roommates,
            "whatsapp_url": self.build_whatsapp_link(wa_text),
            "whatsapp_display": self.whatsapp_number,
            "suggested_properties": []
        }

    def _property_search_response(self, city: Optional[str], bedrooms: Optional[int], lang: str) -> Dict[str, Any]:
        all_props = get_properties()
        matches = []

        for p in all_props:
            if city and city.lower() not in p.get("city", "").lower():
                continue
            if bedrooms and p.get("bedrooms", 0) < bedrooms:
                continue
            matches.append(p)

        if not matches:
            matches = all_props[:3]

        suggested = matches[:3]
        city_name = city or "las principales ciudades europeas"
        best = suggested[0]
        rent_p = round(best.get("rent_per_person", 450))

        if lang == "en":
            reply = (
                f"I found great shared housing opportunities in {city_name}. "
                f"For instance, '{best.get('title')}' with {best.get('bedrooms')} bedrooms for only {rent_p}€ per person per month. "
                f"I have displayed {len(suggested)} options on your screen. "
                f"You can also chat directly via WhatsApp at {self.whatsapp_number} to organize a viewing!"
            )
        else:
            reply = (
                f"He encontrado excelentes opciones en {city_name}. "
                f"Por ejemplo: '{best.get('title')}', con {best.get('bedrooms')} habitaciones por solo {rent_p}€ por persona al mes. "
                f"Te he resaltado {len(suggested)} opciones en pantalla. "
                f"Para concertar una visita ya mismo, puedes escribir a nuestro WhatsApp oficial {self.whatsapp_number}."
            )

        wa_text = f"Hola, me interesa la vivienda '{best.get('title')}' en {best.get('city')} ({rent_p}€/persona). ¿Podemos concertar visita?"
        return {
            "reply_text": reply,
            "action": "property_recommendations",
            "city": city_name,
            "suggested_properties": suggested,
            "whatsapp_url": self.build_whatsapp_link(wa_text),
            "whatsapp_display": self.whatsapp_number
        }

    def _general_advice_response(self, user_msg: str, lang: str) -> Dict[str, Any]:
        if lang == "en":
            reply = (
                "LookingForHome empowers you to access dignified, affordable housing across Europe "
                "by creating cooperative minicommunities to split large apartments. "
                f"Our AI Voice Agent is connected to WhatsApp {self.whatsapp_number}. "
                "Tell me which city you want to live in, or click below to speak directly with an agent on WhatsApp!"
            )
        else:
            reply = (
                "LookingForHome te permite acceder a una vivienda digna en las principales ciudades de Europa "
                "formando minicomunidades para repartir pisos grandes a un precio muy accesible. "
                f"Nuestro Agente IA está sincronizado con el WhatsApp {self.whatsapp_number}. "
                "Dime qué ciudad buscas o pulsa en el enlace para hablar directamente por WhatsApp."
            )

        wa_text = f"Hola, tengo una consulta sobre LookingForHome: {user_msg}"
        return {
            "reply_text": reply,
            "action": "general_advice",
            "whatsapp_url": self.build_whatsapp_link(wa_text),
            "whatsapp_display": self.whatsapp_number,
            "suggested_properties": []
        }

    def build_whatsapp_link(self, message: str) -> str:
        encoded = urllib.parse.quote(message)
        return f"https://wa.me/{self.clean_whatsapp}?text={encoded}"

# Global instance
voice_agent = HousingVoiceAgent()

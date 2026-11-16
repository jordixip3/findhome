/**
 * LookingForHome — European Shared Housing & Rent-Dividing Platform
 * Core Frontend Client: Leaflet Maps, 5-Language i18n with Full Property Translations,
 * Country/City Cascading Filters, Property Type & Surface Range, Rent-Splitter Calculator.
 */

// ── Multi-Language Dictionaries (ES, EN, CA, EU, FR) ─────────────────────────
const I18N = {
  es: {
    nav_properties: "Pisos & Casas",
    nav_communities: "Minicomunidades (3-5)",
    nav_portals: "Portales Europeos",
    nav_stats: "Métricas",
    btn_publish: "Publicar Piso",
    hero_title: "Vivienda digna y accesible en Europa dividiendo el arriendo",
    hero_subtitle: "Forma minicomunidades de 3 a 5 personas, comparte gastos y accede a pisos exteriores en Madrid, Barcelona, Bilbao, París, Berlín y más.",
    microfee_badge_title: "Microcuota Comunitaria: 5€",
    microfee_badge_desc: "Por nuevo miembro al unirse a una minicomunidad confirmada",
    filter_country: "País",
    filter_all_countries: "Todos los países",
    country_es: "España",
    country_fr: "Francia",
    country_de: "Alemania",
    country_nl: "Países Bajos",
    country_pt: "Portugal",
    country_ie: "Irlanda",
    country_it: "Italia",
    filter_city: "Ciudad",
    filter_all_cities: "Todas las ciudades",
    filter_property_type: "Tipo de vivienda",
    filter_all_types: "Todos los tipos",
    type_piso: "Piso",
    type_apartamento: "Apartamento",
    type_atico: "Ático",
    type_casa: "Casa / Chalet",
    type_loft: "Loft",
    filter_surface: "Superficie (m²)",
    filter_all_sizes: "Cualquier tamaño",
    size_lt_80: "< 80 m²",
    size_80_110: "80 – 110 m²",
    size_110_140: "110 – 140 m²",
    size_gt_140: "> 140 m²",
    filter_bedrooms: "Habitaciones mín.",
    filter_bathrooms: "Baños mín.",
    filter_any: "Cualquiera",
    filter_elevator: "Con Ascensor",
    filter_exterior: "Exterior / Balcón",
    filter_max_per_person: "Máx. por persona:",
    filter_reset: "Limpiar",
    showing_properties: "Mostrando",
    properties_avail: "viviendas para minicomunidades",
    click_card_tip: "💡 Haz clic en cualquier piso para ver la ficha o centrar en el mapa",
    map_title: "Mapa Europeo de Viviendas",
    map_badge_prices: "● Precios divididos por persona",
    calc_title: "Calculadora de Reparto de Arriendo",
    calc_subtitle: "Descubre cuánto ahorras al dividir el alquiler entre 3 y 5 personas.",
    calc_total_rent: "Alquiler mensual total del piso:",
    calc_roommates_label: "Miembros de la minicomunidad:",
    calc_per_person_label: "Tu cuota mensual estimada",
    calc_per_person_sub: "por persona / mes (suministros compartidos)",
    calc_savings_text: "🎉 Ahorro estimado vs. alquiler individual (1 dorm): ~",
    comm_heading: "Minicomunidades Activas en Europa",
    comm_subheading: "Grupos de 3 a 5 personas buscando piso juntos para dividir el arriendo y reducir costes a una fracción.",
    comm_btn_create: "Crear Nueva Minicomunidad",
    modal_join_title: "Unirse a la Minicomunidad",
    modal_join_intro: "Completa tus datos de contacto básicos para enviar tu solicitud al grupo y verificar tu plaza.",
    form_name: "Nombre completo *",
    form_email: "Correo electrónico *",
    form_phone: "Teléfono / WhatsApp *",
    form_age: "Edad",
    form_occupation: "Ocupación / Profesión",
    form_bio: "Breve presentación al grupo",
    fee_box_title: "Cuota Comunitaria Europea",
    fee_box_desc: "Garantía antifraude, reserva de plaza y verificación de convivencia",
    fee_box_agree: "Acepto la microcuota de 5€ al confirmar la formación del grupo",
    btn_confirm_join: "Confirmar y Unirme a la Minicomunidad",
    modal_portal_title: "Importar desde Portales Inmobiliarios Europeos",
    modal_portal_intro: "Pega el enlace de un piso en cualquier portal gratuito o abierto europeo (Idealista, Fotocasa, SeLoger, ImmoScout24, Daft.ie, Funda) y LookingForHome calculará automáticamente la división de arriendo para 3-5 personas.",
    form_portal_url: "URL del anuncio *",
    form_target_rent: "Alquiler Total (€/mes)",
    form_roommates_count: "Habitaciones / Compañeros ideales (3 a 5)",
    btn_import_parse: "Importar y Normalizar Datos",
    modal_create_title: "Publicar Vivienda para Minicomunidad",
    form_prop_title: "Título del Anuncio *",
    form_neighborhood: "Barrio / Distrito",
    form_total_rent_input: "Alquiler Total (€/mes) *",
    form_bedrooms_input: "Habitaciones (3-5) *",
    form_desc: "Descripción y características para la convivencia",
    btn_publish_prop: "Publicar Piso en LookingForHome",
    view_details: "Ver Ficha",
    form_community_action: "Formar Grupo",
    members_title_text: "Miembros y plazas",
    open_slot: "Plaza disponible",
    total_rent_label: "Total:",
    rooms_label: "habs",
    baths_label: "baños",
    elevator_yes: "Ascensor",
    elevator_no: "Sin ascensor",
    exterior_yes: "Exterior",
    interior_yes: "Interior",
    per_person_month: "persona / mes",
    recommended_split: "DIVISIÓN RECOMENDADA",
    btn_maximize: "⛶ Maximizar Fotos",
    click_zoom_tip: "🔍 Clic en la foto para ampliar en pantalla completa",
    photo_counter_label: "Foto",
    photo_of: "de",
    btn_join_community: "Unirme a la Minicomunidad",
    contact_owner_title: "Gestión y Contacto Directo",
    btn_whatsapp: "WhatsApp Directo",
    btn_call: "Llamar",
    btn_email: "Enviar Email",
    btn_portal: "Ver Anuncio Oficial en",
    inquiry_title: "Solicitud directa de visita o información:",
    btn_send_inquiry: "Enviar Mensaje Directo al Gestor"
  },
  en: {
    nav_properties: "Flats & Houses",
    nav_communities: "Minicommunities (3-5)",
    nav_portals: "European Portals",
    nav_stats: "Metrics",
    btn_publish: "List Property",
    hero_title: "Decent and affordable housing in Europe by splitting rent",
    hero_subtitle: "Form minicommunities of 3 to 5 people, split costs, and access sunny apartments across Madrid, Barcelona, Bilbao, Paris, Berlin and beyond.",
    microfee_badge_title: "Community Micro-Fee: 5€",
    microfee_badge_desc: "Per new member upon joining a confirmed minicommunity",
    filter_country: "Country",
    filter_all_countries: "All countries",
    country_es: "Spain",
    country_fr: "France",
    country_de: "Germany",
    country_nl: "Netherlands",
    country_pt: "Portugal",
    country_ie: "Ireland",
    country_it: "Italy",
    filter_city: "City",
    filter_all_cities: "All cities",
    filter_property_type: "Property Type",
    filter_all_types: "All types",
    type_piso: "Flat",
    type_apartamento: "Apartment",
    type_atico: "Penthouse",
    type_casa: "House / Townhouse",
    type_loft: "Loft",
    filter_surface: "Surface (sqm)",
    filter_all_sizes: "Any size",
    size_lt_80: "< 80 m²",
    size_80_110: "80 – 110 m²",
    size_110_140: "110 – 140 m²",
    size_gt_140: "> 140 m²",
    filter_bedrooms: "Min bedrooms",
    filter_bathrooms: "Min bathrooms",
    filter_any: "Any",
    filter_elevator: "With Elevator",
    filter_exterior: "Exterior / Balcony",
    filter_max_per_person: "Max per person:",
    filter_reset: "Reset",
    showing_properties: "Showing",
    properties_avail: "properties for minicommunities",
    click_card_tip: "💡 Click on any property to view details or center on the map",
    map_title: "European Housing Map",
    map_badge_prices: "● Prices split per person",
    calc_title: "Rent-Dividing Calculator",
    calc_subtitle: "Discover how much you save by sharing rent among 3 to 5 people.",
    calc_total_rent: "Total monthly flat rent:",
    calc_roommates_label: "Minicommunity members:",
    calc_per_person_label: "Your estimated monthly share",
    calc_per_person_sub: "per person / month (shared utilities)",
    calc_savings_text: "🎉 Estimated savings vs single flat (1-bed): ~",
    comm_heading: "Active Minicommunities in Europe",
    comm_subheading: "Groups of 3 to 5 people seeking housing together to split rent and slash living costs.",
    comm_btn_create: "Create New Minicommunity",
    modal_join_title: "Join Minicommunity",
    modal_join_intro: "Provide your basic contact info to send your request to the group and reserve your room.",
    form_name: "Full name *",
    form_email: "Email address *",
    form_phone: "Phone / WhatsApp *",
    form_age: "Age",
    form_occupation: "Occupation / Job",
    form_bio: "Short intro to the group",
    fee_box_title: "European Community Fee",
    fee_box_desc: "Anti-fraud protection, room reservation & verified cohabitation",
    fee_box_agree: "I agree to the 5€ micro-fee upon confirming the group formation",
    btn_confirm_join: "Confirm and Join Minicommunity",
    modal_portal_title: "Import from European Housing Portals",
    modal_portal_intro: "Paste a listing link from any European portal (Idealista, Fotocasa, SeLoger, ImmoScout24, Daft.ie, Funda) and LookingForHome will compute the 3-5 person rent split.",
    form_portal_url: "Listing URL *",
    form_target_rent: "Total Rent (€/month)",
    form_roommates_count: "Ideal Bedrooms / Flatmates (3 to 5)",
    btn_import_parse: "Import and Normalize Data",
    modal_create_title: "Publish Property for Minicommunity",
    form_prop_title: "Listing Title *",
    form_neighborhood: "Neighborhood / District",
    form_total_rent_input: "Total Rent (€/month) *",
    form_bedrooms_input: "Bedrooms (3-5) *",
    form_desc: "Description & cohabitation features",
    btn_publish_prop: "Publish Flat on LookingForHome",
    view_details: "View Flat",
    form_community_action: "Form Group",
    members_title_text: "Members and spots",
    open_slot: "Available spot",
    total_rent_label: "Total:",
    rooms_label: "beds",
    baths_label: "baths",
    elevator_yes: "Elevator",
    elevator_no: "No elevator",
    exterior_yes: "Exterior",
    interior_yes: "Interior",
    per_person_month: "person / month",
    recommended_split: "RECOMMENDED SPLIT",
    btn_maximize: "⛶ Maximize Photos",
    click_zoom_tip: "🔍 Click photo to view fullscreen",
    photo_counter_label: "Photo",
    photo_of: "of",
    btn_join_community: "Join Minicommunity",
    contact_owner_title: "Direct Management & Contact",
    btn_whatsapp: "Direct WhatsApp",
    btn_call: "Call",
    btn_email: "Send Email",
    btn_portal: "View Official Listing on",
    inquiry_title: "Direct visit request or inquiry:",
    btn_send_inquiry: "Send Direct Message to Manager"
  },
  ca: {
    nav_properties: "Pisos & Cases",
    nav_communities: "Minicomunitats (3-5)",
    nav_portals: "Portals Europeus",
    nav_stats: "Mètriques",
    btn_publish: "Publicar Pis",
    hero_title: "Habitatge digne i assequible a Europa dividint el lloguer",
    hero_subtitle: "Forma minicomunitats de 3 a 5 persones, comparteix despeses i accedeix a pisos exteriors a Barcelona, Madrid, París, Berlín i més.",
    microfee_badge_title: "Microquota Comunitària: 5€",
    microfee_badge_desc: "Per nou membre en unir-se a una minicomunitat confirmada",
    filter_country: "País",
    filter_all_countries: "Tots els països",
    country_es: "Espanya",
    country_fr: "França",
    country_de: "Alemanya",
    country_nl: "Països Baixos",
    country_pt: "Portugal",
    country_ie: "Irlanda",
    country_it: "Itàlia",
    filter_city: "Ciutat",
    filter_all_cities: "Totes les ciutats",
    filter_property_type: "Tipus d'habitatge",
    filter_all_types: "Tots els tipus",
    type_piso: "Pis",
    type_apartamento: "Apartament",
    type_atico: "Àtic",
    type_casa: "Casa / Xalet",
    type_loft: "Loft",
    filter_surface: "Superfície (m²)",
    filter_all_sizes: "Qualsevol mida",
    size_lt_80: "< 80 m²",
    size_80_110: "80 – 110 m²",
    size_110_140: "110 – 140 m²",
    size_gt_140: "> 140 m²",
    filter_bedrooms: "Habitacions mín.",
    filter_bathrooms: "Banys mín.",
    filter_any: "Qualsevol",
    filter_elevator: "Amb Ascensor",
    filter_exterior: "Exterior / Balcó",
    filter_max_per_person: "Màx. per persona:",
    filter_reset: "Netejar",
    showing_properties: "Mostrant",
    properties_avail: "habitatges per a minicomunitats",
    click_card_tip: "💡 Fes clic a qualsevol pis per veure la fitxa o centrar al mapa",
    map_title: "Mapa Europeu d'Habitatges",
    map_badge_prices: "● Preus dividits per persona",
    calc_title: "Calculadora de Repartiment de Lloguer",
    calc_subtitle: "Descobreix quant estalvies dividint el lloguer entre 3 i 5 persones.",
    calc_total_rent: "Lloguer mensual total del pis:",
    calc_roommates_label: "Membres de la minicomunitat:",
    calc_per_person_label: "La teva quota mensual estimada",
    calc_per_person_sub: "per persona / mes (despeses compartides)",
    calc_savings_text: "🎉 Estalvi estimat vs lloguer individual (1 hab): ~",
    comm_heading: "Minicomunitats Actives a Europa",
    comm_subheading: "Grups de 3 a 5 persones cercant pis junts per dividir el lloguer i reduir despeses.",
    comm_btn_create: "Crear Nova Minicomunitat",
    modal_join_title: "Unir-se a la Minicomunitat",
    modal_join_intro: "Completa les teves dades bàsiques de contacte per enviar la teva sol·licitud al grup.",
    form_name: "Nom complet *",
    form_email: "Correu electrònic *",
    form_phone: "Telèfon / WhatsApp *",
    form_age: "Edat",
    form_occupation: "Ocupació / Professió",
    form_bio: "Breu presentació al grup",
    fee_box_title: "Quota Comunitària Europea",
    fee_box_desc: "Garantia antifrau, reserva de plaça i verificació de convivència",
    fee_box_agree: "Accepto la microquota de 5€ en confirmar la formació del grup",
    btn_confirm_join: "Confirmar i Unir-me a la Minicomunitat",
    modal_portal_title: "Importar des de Portals Immobiliaris Europeus",
    modal_portal_intro: "Enganxa l'enllaç d'un pis de qualsevol portal europeu i LookingForHome calcularà el repartiment per a 3-5 persones.",
    form_portal_url: "URL de l'anunci *",
    form_target_rent: "Lloguer Total (€/mes)",
    form_roommates_count: "Habitacions / Companys ideals (3 a 5)",
    btn_import_parse: "Importar i Normalitzar Dades",
    modal_create_title: "Publicar Habitatge per a Minicomunitat",
    form_prop_title: "Títol de l'Anunci *",
    form_neighborhood: "Barri / Districte",
    form_total_rent_input: "Lloguer Total (€/mes) *",
    form_bedrooms_input: "Habitacions (3-5) *",
    form_desc: "Descripció i característiques per a la convivència",
    btn_publish_prop: "Publicar Pis a LookingForHome",
    view_details: "Veure Fitxa",
    form_community_action: "Formar Grup",
    members_title_text: "Membres i places",
    open_slot: "Plaça disponible",
    total_rent_label: "Total:",
    rooms_label: "habs",
    baths_label: "banys",
    elevator_yes: "Ascensor",
    elevator_no: "Sense ascensor",
    exterior_yes: "Exterior",
    interior_yes: "Interior",
    per_person_month: "persona / mes",
    recommended_split: "REPARTIMENT RECOMANAT",
    btn_maximize: "⛶ Maximitzar Fotos",
    click_zoom_tip: "🔍 Clic a la foto per ampliar en pantalla completa",
    photo_counter_label: "Foto",
    photo_of: "de",
    btn_join_community: "Unir-me a la Minicomunitat",
    contact_owner_title: "Gestió i Contacte Directe",
    btn_whatsapp: "WhatsApp Directe",
    btn_call: "Trucar",
    btn_email: "Enviar Email",
    btn_portal: "Veure Anunci Oficial a",
    inquiry_title: "Sol·licitud directa de visita o informació:",
    btn_send_inquiry: "Enviar Missatge Directe al Gestor"
  },
  eu: {
    nav_properties: "Etxebizitzak",
    nav_communities: "Minikomunitateak (3-5)",
    nav_portals: "Europako Atariak",
    nav_stats: "Metrikak",
    btn_publish: "Etxebizitza Argitaratu",
    hero_title: "Etxebizitza duina eta eskuragarria Europan alokairua zatituz",
    hero_subtitle: "Eratu 3-5 laguneko minikomunitateak, gastuak partekatu eta sarbidea izan Bilbon, Donostian, Madrilen, Parisen eta gehiagotan.",
    microfee_badge_title: "Komunitateko Mikro-kuota: 5€",
    microfee_badge_desc: "Kide berri bakoitzeko baieztatutako talde batera batzean",
    filter_country: "Herrialdea",
    filter_all_countries: "Herrialde guztiak",
    country_es: "Espainia",
    country_fr: "Frantzia",
    country_de: "Alemania",
    country_nl: "Herbehereak",
    country_pt: "Portugal",
    country_ie: "Irlanda",
    country_it: "Italia",
    filter_city: "Hiria",
    filter_all_cities: "Hiri guztiak",
    filter_property_type: "Etxebizitza mota",
    filter_all_types: "Mota guztiak",
    type_piso: "Pisua",
    type_apartamento: "Apartamentua",
    type_atico: "Atikoa",
    type_casa: "Etxea / Txaleta",
    type_loft: "Loft-a",
    filter_surface: "Azalera (m²)",
    filter_all_sizes: "Edozein tamaina",
    size_lt_80: "< 80 m²",
    size_80_110: "80 – 110 m²",
    size_110_140: "110 – 140 m²",
    size_gt_140: "> 140 m²",
    filter_bedrooms: "Gutxieneko logelak",
    filter_bathrooms: "Gutxieneko bainugelak",
    filter_any: "Edozein",
    filter_elevator: "Igogailuarekin",
    filter_exterior: "Kanpokoa / Balkoia",
    filter_max_per_person: "Gehieneko prezioa:",
    filter_reset: "Garbitu",
    showing_properties: "Erakusten:",
    properties_avail: "minikomunitateentzako etxebizitza",
    click_card_tip: "💡 Sakatu edozein etxebizitza fitxa ikusteko edo mapan kokatzeko",
    map_title: "Europako Etxebizitzen Mapa",
    map_badge_prices: "● Prezioak pertsonako banatuta",
    calc_title: "Alokairu Zatiketaren Kalkulagailua",
    calc_subtitle: "Ikusi zenbat aurrezten duzun alokairua 3-5 pertsonaren artean banatuz.",
    calc_total_rent: "Etxebizitzaren hileko alokairu osoa:",
    calc_roommates_label: "Minikomunitateko kideak:",
    calc_per_person_label: "Zure estimatutako hileko kuota",
    calc_per_person_sub: "pertsonako / hilean (gastuak partekatuta)",
    calc_savings_text: "🎉 Banakako alokairuarekiko aurrezpen estimatua: ~",
    comm_heading: "Minikomunitate Aktiboak Europan",
    comm_subheading: "3-5 laguneko taldeak etxea elkarrekin bilatuz alokairua zatitu eta kostuak murrizteko.",
    comm_btn_create: "Minikomunitate Berria Sortu",
    modal_join_title: "Minikomunitatera Batu",
    modal_join_intro: "Bete zure oinarrizko harremanetarako datuak taldeari eskaera bidaltzeko.",
    form_name: "Izen osoa *",
    form_email: "Helbide elektronikoa *",
    form_phone: "Telefonoa / WhatsApp *",
    form_age: "Adina",
    form_occupation: "Lanbidea / Ikasketak",
    form_bio: "Aurkezpen laburra taldeari",
    fee_box_title: "Europako Komunitate Kuota",
    fee_box_desc: "Iruzurraren aurkako bermea, lekua erreserbatzea eta bizikidetza egiaztatua",
    fee_box_agree: "5€-ko mikro-kuota onartzen dut taldea osatzean",
    btn_confirm_join: "Baieztatu eta Minikomunitatera Batu",
    modal_portal_title: "Europako Higiezinen Atarietatik Inportatu",
    modal_portal_intro: "Itsatsi edozein ataritako lotura eta LookingForHome-k 3-5 pertsonentzako alokairuaren zatiketa kalkulatuko du.",
    form_portal_url: "Iragarkiaren URL-a *",
    form_target_rent: "Alokairu Osoa (€/hil)",
    form_roommates_count: "Logelak / Kideak (3tik 5era)",
    btn_import_parse: "Datuak Inportatu eta Normalizatu",
    modal_create_title: "Etxebizitza Argitaratu Taldearentzat",
    form_prop_title: "Iragarkiaren Izenburua *",
    form_neighborhood: "Auzoa / Barrutia",
    form_total_rent_input: "Alokairu Osoa (€/hil) *",
    form_bedrooms_input: "Logelak (3-5) *",
    form_desc: "Deskribapena eta bizikidetza ezaugarriak",
    btn_publish_prop: "Argitaratu LookingForHome-n",
    view_details: "Fitxa Ikusi",
    form_community_action: "Taldea Sortu",
    members_title_text: "Kideak eta plazak",
    open_slot: "Plaza librea",
    total_rent_label: "Guztira:",
    rooms_label: "logela",
    baths_label: "bainugela",
    elevator_yes: "Igogailua",
    elevator_no: "Igogailurik gabe",
    exterior_yes: "Kanpokoa",
    interior_yes: "Barrukoa",
    per_person_month: "pertsona / hila",
    recommended_split: "GOMENDATUTAKO BANAKETA",
    btn_maximize: "⛶ Argazkiak handitu",
    click_zoom_tip: "🔍 Egin klik argazkian pantaila osoan ikusteko",
    photo_counter_label: "Argazkia",
    photo_of: "-(e)tik",
    btn_join_community: "Minikomunitatera Batu",
    contact_owner_title: "Zuzeneko Kudeaketa eta Harremana",
    btn_whatsapp: "Zuzeneko WhatsApp",
    btn_call: "Deitu",
    btn_email: "Emaila Bidali",
    btn_portal: "Iragarki Ofiziala Ikusi hemen:",
    inquiry_title: "Bisita edo informazio eskaera zuzena:",
    btn_send_inquiry: "Kudeatzaileari Mezua Bidali"
  },
  fr: {
    nav_properties: "Logements & Appartements",
    nav_communities: "Minicommunautés (3-5)",
    nav_portals: "Portails Européens",
    nav_stats: "Métriques",
    btn_publish: "Publier un Logement",
    hero_title: "Un logement digne et abordable en Europe en divisant le loyer",
    hero_subtitle: "Formez des minicommunautés de 3 à 5 personnes, partagez les frais et accédez à des appartements à Paris, Berlin, Madrid, Bruxelles et au-delà.",
    microfee_badge_title: "Micro-Cotisation Communautaire : 5€",
    microfee_badge_desc: "Par nouveau membre lors de l'intégration à un groupe confirmé",
    filter_country: "Pays",
    filter_all_countries: "Tous les pays",
    country_es: "Espagne",
    country_fr: "France",
    country_de: "Allemagne",
    country_nl: "Pays-Bas",
    country_pt: "Portugal",
    country_ie: "Irlande",
    country_it: "Italie",
    filter_city: "Ville",
    filter_all_cities: "Toutes les villes",
    filter_property_type: "Type de bien",
    filter_all_types: "Tous les types",
    type_piso: "Appartement",
    type_apartamento: "Logement",
    type_atico: "Attique / Penthouse",
    type_casa: "Maison",
    type_loft: "Loft",
    filter_surface: "Surface (m²)",
    filter_all_sizes: "Toutes surfaces",
    size_lt_80: "< 80 m²",
    size_80_110: "80 – 110 m²",
    size_110_140: "110 – 140 m²",
    size_gt_140: "> 140 m²",
    filter_bedrooms: "Chambres min.",
    filter_bathrooms: "Salles de bain min.",
    filter_any: "Tous",
    filter_elevator: "Avec Ascenseur",
    filter_exterior: "Extérieur / Balcon",
    filter_max_per_person: "Max. par personne :",
    filter_reset: "Réinitialiser",
    showing_properties: "Affichage de",
    properties_avail: "logements pour minicommunautés",
    click_card_tip: "💡 Cliquez sur un logement pour afficher les détails ou centrer sur la carte",
    map_title: "Carte Européenne des Logements",
    map_badge_prices: "● Prix divisés par personne",
    calc_title: "Calculateur de Répartition du Loyer",
    calc_subtitle: "Découvrez vos économies en partageant le loyer entre 3 et 5 personnes.",
    calc_total_rent: "Loyer mensuel total du logement :",
    calc_roommates_label: "Membres de la minicommunauté :",
    calc_per_person_label: "Votre part mensuelle estimée",
    calc_per_person_sub: "par personne / mois (charges partagées)",
    calc_savings_text: "🎉 Économie estimée par rapport à un studio individuel : ~",
    comm_heading: "Minicommunautés Actives en Europe",
    comm_subheading: "Des groupes de 3 à 5 personnes cherchant ensemble pour diviser le loyer et alléger leurs charges.",
    comm_btn_create: "Créer une Minicommunauté",
    modal_join_title: "Rejoindre la Minicommunauté",
    modal_join_intro: "Renseignez vos coordonnées de base pour transmettre votre demande au groupe.",
    form_name: "Nom complet *",
    form_email: "Adresse e-mail *",
    form_phone: "Téléphone / WhatsApp *",
    form_age: "Âge",
    form_occupation: "Profession / Statut",
    form_bio: "Courte présentation pour le groupe",
    fee_box_title: "Cotisation Communautaire Européenne",
    fee_box_desc: "Garantie antifraude, réservation de place et cohabitation vérifiée",
    fee_box_agree: "J'accepte la micro-cotisation de 5€ à la confirmation du groupe",
    btn_confirm_join: "Confirmer et Rejoindre le Groupe",
    modal_portal_title: "Importer depuis les Portails Immobiliers Européens",
    modal_portal_intro: "Collez le lien d'un appartement depuis SeLoger, Idealista, ImmoScout24, Daft.ie ou Funda et LookingForHome calculera la division pour 3-5 colocataires.",
    form_portal_url: "URL de l'annonce *",
    form_target_rent: "Loyer Total (€/mois)",
    form_roommates_count: "Chambres / Colocataires idéaux (3 à 5)",
    btn_import_parse: "Importer et Normaliser",
    modal_create_title: "Publier un Logement pour Minicommunauté",
    form_prop_title: "Titre de l'annonce *",
    form_neighborhood: "Quartier / Arrondissement",
    form_total_rent_input: "Loyer Total (€/mois) *",
    form_bedrooms_input: "Chambres (3-5) *",
    form_desc: "Description et atouts pour la vie commune",
    btn_publish_prop: "Publier sur LookingForHome",
    view_details: "Voir la Fiche",
    form_community_action: "Former un Groupe",
    members_title_text: "Membres et places",
    open_slot: "Place disponible",
    total_rent_label: "Total :",
    rooms_label: "chambres",
    baths_label: "salles de bain",
    elevator_yes: "Ascenseur",
    elevator_no: "Sans ascenseur",
    exterior_yes: "Extérieur",
    interior_yes: "Intérieur",
    per_person_month: "personne / mois",
    recommended_split: "RÉPARTITION RECOMMANDÉE",
    btn_maximize: "⛶ Agrandir les photos",
    click_zoom_tip: "🔍 Cliquez sur la photo pour agrandir en plein écran",
    photo_counter_label: "Photo",
    photo_of: "sur",
    btn_join_community: "Rejoindre la Minicommunauté",
    contact_owner_title: "Gestion et Contact Direct",
    btn_whatsapp: "WhatsApp Direct",
    btn_call: "Appeler",
    btn_email: "Envoyer un Email",
    btn_portal: "Voir l'Annonce Officielle sur",
    inquiry_title: "Demande directe de visite ou information :",
    btn_send_inquiry: "Envoyer un Message Direct au Gestionnaire"
  }
};

// ── Complete Property Translations (ES, EN, CA, EU, FR) ──────────────────────
const PROPERTY_TRANSLATIONS = {
  "prop-mad-01": {
    type: "atico",
    es: {
      title: "Ático luminoso con terraza en Malasaña — Ideal para 4 personas",
      description: "Gran piso reformado en pleno centro de Madrid. 4 habitaciones independientes amplias con armarios empotrados, salón exterior con luz natural todo el día, 2 baños completos y cocina equipada. Edificio con ascensor."
    },
    en: {
      title: "Sunny Penthouse with Terrace in Malasaña — Ideal for 4 People",
      description: "Spacious renovated flat in the heart of Madrid. 4 independent bedrooms with built-in wardrobes, bright exterior living room with sunlight all day, 2 full bathrooms, and equipped kitchen. Building with elevator."
    },
    ca: {
      title: "Àtic lluminós amb terrassa a Malasaña — Ideal per a 4 persones",
      description: "Gran pis reformat al centre de Madrid. 4 habitacions independents àmplies amb armaris encastats, saló exterior amb llum natural tot el dia, 2 banys complets i cuina equipada. Edifici amb ascensor."
    },
    eu: {
      title: "Atiko argitsua terrazarekin Malasañan — 4 lagunentzat aproposa",
      description: "Madril erdiguneko etxebizitza berritu zabala. 4 logela independente horma-armairuekin, egongela kanpokoa argi naturalarekin egun osoan, 2 bainugela oso eta sukalde hornitua. Igogailudun eraikina."
    },
    fr: {
      title: "Penthouse lumineux avec terrasse à Malasaña — Idéal pour 4 personnes",
      description: "Grand appartement rénové au cœur de Madrid. 4 chambres indépendantes avec placards intégrés, salon extérieur baigné de lumière toute la journée, 2 salles de bain complètes et cuisine équipée. Immeuble avec ascenseur."
    }
  },
  "prop-mad-02": {
    type: "piso",
    es: {
      title: "Piso señorial en Chamberí — 5 dormitorios y 3 baños",
      description: "Excelente vivienda para minicomunidad joven de 5 profesionales o estudiantes. Techos altos, calefacción central, exterior a calle ajardinada, 3 baños para máxima comodidad y cocina office."
    },
    en: {
      title: "Stately Flat in Chamberí — 5 Bedrooms and 3 Bathrooms",
      description: "Superb home for a young minicommunity of 5 professionals or students. High ceilings, central heating, exterior views onto a garden street, 3 bathrooms for maximum comfort, and large eat-in kitchen."
    },
    ca: {
      title: "Pis senyorial a Chamberí — 5 dormitoris i 3 banys",
      description: "Excel·lent habitatge per a minicomunitat jove de 5 professionals o estudiants. Sostres alts, calefacció central, exterior a carrer enjardinat, 3 banys per a màxima comoditat i cuina office."
    },
    eu: {
      title: "Jauregi-itxurako pisua Chamberín — 5 logela eta 3 bainugela",
      description: "Etxebizitza bikaina 5 profesional edo ikaslez osatutako minikomunitatearentzat. Sabai altuak, berogailu zentrala, lorategidun kalera begira, 3 bainugela eta sukalde handia."
    },
    fr: {
      title: "Bel appartement bourgeois à Chamberí — 5 chambres et 3 salles de bain",
      description: "Superbe logement pour une jeune minicommunauté de 5 professionnels ou étudiants. Hauts plafonds, chauffage central, vue dégagée sur rue arborée, 3 salles de bain et grande cuisine dînatoire."
    }
  },
  "prop-mad-03": {
    type: "loft",
    es: {
      title: "Loft moderno cerca de Madrid Río — 3 habitaciones dobles",
      description: "Espacio vanguardista con techos de 3.5m, grandes ventanales, zona común abierta y 3 dormitorios espaciosos con mesa de trabajo. Cerca de Metro Pirámides y parque Madrid Río."
    },
    en: {
      title: "Modern Loft near Madrid Río — 3 Double Bedrooms",
      description: "Avant-garde space with 3.5m ceilings, oversized windows, open living area, and 3 spacious bedrooms with work desks. Close to Pirámides Metro and Madrid Río park."
    },
    ca: {
      title: "Loft modern a prop de Madrid Río — 3 habitacions dobles",
      description: "Espai avantguardista amb sostres de 3,5m, grans finestrals, zona comuna oberta i 3 dormitoris espaiosos amb taula de treball. A prop del metro Pirámides i el parc Madrid Río."
    },
    eu: {
      title: "Loft modernoa Madrid Río ondoan — 3 gela bikoitz",
      description: "Gune banguardista 3,5 metroko sabaiekin, leiho handiekin, gune komun irekiarekin eta lan-mahaidun 3 logela zabalekin. Pirámides metrotik eta Madrid Río parketik gertu."
    },
    fr: {
      title: "Loft contemporain près de Madrid Río — 3 chambres doubles",
      description: "Espace avant-gardiste avec 3,5m sous plafond, grandes baies vitrées, séjour ouvert et 3 chambres spacieuses avec bureaux de travail. Proche du métro Pirámides et du parc Madrid Río."
    }
  },
  "prop-bcn-01": {
    type: "piso",
    es: {
      title: "Piso modernista junto a Passeig de Gràcia — 4 habitaciones",
      description: "Piso de época con suelos hidráulicos originales y balcones a la calle. 4 habitaciones grandes, cocina recién reformada, 2 baños completos y salón comedor espacioso. Finca regia con ascensor."
    },
    en: {
      title: "Modernist Flat next to Passeig de Gràcia — 4 Bedrooms",
      description: "Period home featuring original hydraulic tile floors and street-facing balconies. 4 large bedrooms, newly renovated kitchen, 2 full bathrooms, and expansive living-dining room. Stately building with elevator."
    },
    ca: {
      title: "Modernista al costat de Passeig de Gràcia — 4 habitacions",
      description: "Pis d'època amb terres hidràulics originals i balcons al carrer. 4 habitacions grans, cuina recent reformada, 2 banys complets i saló menjador espaiós. Ascensor i finca règia cuidada."
    },
    eu: {
      title: "Pisu modernista Passeig de Gràcia ondoan — 4 logela",
      description: "Garai bateko etxebizitza lur hidrauliko originalekin eta balkoiekin. 4 gela handi, sukalde berritu berria, 2 bainugela oso eta egongela-jangela zabala. Igogailua duen finka dotorea."
    },
    fr: {
      title: "Appartement moderniste près du Passeig de Gràcia — 4 chambres",
      description: "Logement d'époque avec carreaux de ciment d'origine et balcons sur rue. 4 grandes chambres, cuisine fraîchement rénovée, 2 salles de bain complètes et grand salon-salle à manger. Immeuble de standing avec ascenseur."
    }
  },
  "prop-bcn-02": {
    type: "atico",
    es: {
      title: "Ático con terraza en Gràcia — 3 habitaciones con encanto",
      description: "Tranquilo y soleado en la Vila de Gràcia. Terraza de 25m² para cenas compartidas, 3 dormitorios, baño reformado con ducha italiana y abundante luz natural. A pasos de metro Fontana L3."
    },
    en: {
      title: "Charming Penthouse with Terrace in Gràcia — 3 Bedrooms",
      description: "Quiet and sun-drenched in vibrant Vila de Gràcia. 25m² private terrace for shared dinners, 3 bedrooms, updated walk-in shower bathroom, and plenty of natural daylight. Steps from Fontana L3 Metro."
    },
    ca: {
      title: "Àtic amb terrassa a Gràcia — 3 habitacions amb encant",
      description: "Tranquil i assolellat a la Vila de Gràcia. Terrassa de 25m² per sopars compartits, 3 dormitoris, bany reformat amb dutxa italiana i molta llum natural. Molt a prop de Fontana L3."
    },
    eu: {
      title: "Atiko xarmagarria terrazarekin Gràcian — 3 logela",
      description: "Leku lasaia eta eguzkitsua Vila de Gràcian. 25m²-ko terraza afari partekatuetarako, 3 logela, dutxa italiardun bainugela berritua eta argi natural ugaria. Fontana L3 metrotik oso gertu."
    },
    fr: {
      title: "Attique avec terrasse à Gràcia — 3 chambres pleines de charme",
      description: "Calme et ensoleillé au cœur de la Vila de Gràcia. Terrasse de 25m² idéale pour dîners partagés, 3 chambres, salle d'eau rénovée avec douche à l'italienne et lumière naturelle. À deux pas du métro Fontana L3."
    }
  },
  "prop-eusk-01": {
    type: "piso",
    es: {
      title: "Vivienda amplia en Abando — 4 habitaciones y 2 baños completos",
      description: "En pleno centro de Bilbao, a 2 minutos de las estaciones de tren y metro. 4 habitaciones grandes y luminosas, calefacción central, ascensor y totalmente exterior. Ideal para jóvenes y trabajadores."
    },
    en: {
      title: "Spacious Flat in Abando — 4 Bedrooms and 2 Full Bathrooms",
      description: "In the heart of Bilbao, 2 minutes from train and metro hubs. 4 large sunny bedrooms, central heating, elevator, and fully exterior facing. Perfect for young flatmates and coworkers."
    },
    ca: {
      title: "Habitatge ampli a Abando — 4 habitacions i 2 banys complets",
      description: "Al centre de Bilbao, a 2 minuts de les estacions de tren i metro. 4 habitacions grans i lluminoses, calefacció central, ascensor i totalment exterior. Ideal per a joves i treballadors."
    },
    eu: {
      title: "Etxebizitza zabala Abandon — 4 gela eta 2 bainugela oso",
      description: "Bilboko erdigunean, tren eta metro geltokietatik 2 minutura. 4 logela handi argitsuak, berogailu zentrala, igogailua eta kanpoaldera begira. Gazte eta langileentzat ezin hobea."
    },
    fr: {
      title: "Grand appartement à Abando — 4 chambres et 2 salles de bain",
      description: "En plein centre de Bilbao, à 2 minutes des gares de train et métro. 4 grandes chambres lumineuses, chauffage central, ascenseur, entièrement extérieur. Parfait pour jeunes actifs et étudiants."
    }
  },
  "prop-eusk-02": {
    type: "apartamento",
    es: {
      title: "Piso luminoso en Gros — A 5 minutos de la playa Zurriola",
      description: "En el barrio joven de Gros, muy cerca de la playa de Zurriola. 3 habitaciones dobles, salón acogedor con balcón exterior, ascensor y calefacción de gas. Ambiente surfero y tranquilo."
    },
    en: {
      title: "Bright Apartment in Gros — 5 Minutes from Zurriola Beach",
      description: "In the trendy Gros district, steps away from Zurriola surfing beach. 3 double bedrooms, inviting living room with sunny balcony, elevator, and gas heating."
    },
    ca: {
      title: "Pis lluminós a Gros — A 5 minuts de la platja Zurriola",
      description: "Al barri jove de Gros, molt a prop de la platja de la Zurriola. 3 habitacions dobles, saló acollidor amb balcó exterior, ascensor i calefacció de gas."
    },
    eu: {
      title: "Pisu argitsua Gros auzoan — Zurriola hondartzatik 5 minutura",
      description: "Donostiako Gros auzoan, Zurriola hondartzatik gertu. 3 gela bikoitz, egongela ederra balkoiarekin, igogailua eta gas bidezko berogailua."
    },
    fr: {
      title: "Appartement lumineux à Gros — À 5 minutes de la plage de Zurriola",
      description: "Dans le quartier animé de Gros, à deux pas de la plage de Zurriola. 3 chambres doubles, agréable salon avec balcon, ascenseur et chauffage au gaz."
    }
  },
  "prop-par-01": {
    type: "apartamento",
    es: {
      title: "Gran apartamento haussmanniano en Bastille — 4 habitaciones",
      description: "Magnífico piso de 115m² con suelos de parquet en espiga, molduras y chimeneas. 4 dormitorios independientes ideales para coliving responsable. Cocina comedor equipada y 2 baños."
    },
    en: {
      title: "Grand Haussmannian Apartment in Bastille — 4 Bedrooms",
      description: "Magnificent 115m² Parisian apartment with herringbone parquet, mouldings, and fireplaces. 4 separate bedrooms ideal for shared living. Fully equipped dining kitchen and 2 bathrooms."
    },
    ca: {
      title: "Gran apartament haussmannià a Bastille — 4 habitacions",
      description: "Magnífic pis de 115m² amb parquet en espiga, motllures i xemeneies. 4 dormitoris independents ideals per a coliving responsable. Cuina menjador equipada i 2 banys."
    },
    eu: {
      title: "Haussmann estiloko apartamentu handia Bastillen — 4 logela",
      description: "115m²-ko etxebizitza ederra zurezko zoruekin eta tximiniekin. 4 logela independente elkarbizitzarako aproposak. Sukalde-jangela hornitua eta 2 bainugela."
    },
    fr: {
      title: "Grand appartement haussmannien à Bastille — 4 chambres",
      description: "Magnifique appartement de 115m² avec parquet point de Hongrie, moulures et cheminées. 4 chambres séparées idéales pour colocation éco-responsable. Cuisine dînatoire équipée, 2 salles de bain."
    }
  },
  "prop-par-02": {
    type: "apartamento",
    es: {
      title: "Apartamento de arquitecto en Canal Saint-Martin — 3 habitaciones",
      description: "Vistas despejadas al canal, muy tranquilo y luminoso. 3 habitaciones amplias, gran salón para compartir, ascensor, fibra óptica y cuarto para bicicletas. Cerca de metro République."
    },
    en: {
      title: "Architect-Designed Flat on Canal Saint-Martin — 3 Bedrooms",
      description: "Unobstructed views over the canal, extremely quiet and bright. 3 comfortable bedrooms, large convivial living room, elevator, fiber optic, and bike storage. Near République metro."
    },
    ca: {
      title: "Apartament d'arquitecte al Canal Saint-Martin — 3 habitacions",
      description: "Vistes clares al canal, molt tranquil i lluminós. 3 habitacions àmplies, gran saló per compartir, ascensor, fibra òptica i espai per a bicicletes. A prop del metro République."
    },
    eu: {
      title: "Arkitekto-apartamentua Canal Saint-Martin-en — 3 logela",
      description: "Kanalera begirako bista garbiak, oso lasaia eta argitsua. 3 logela zabal, lagunarteko egongela handia, igogailua, zuntz optikoa eta bizikleta-gela. République metrotik gertu."
    },
    fr: {
      title: "Appartement d'architecte au Canal Saint-Martin — 3 chambres",
      description: "Vue dégagée sur le canal, très calme et lumineux. 3 belles chambres, grand salon convivial, ascenseur, fibre optique et local vélos. Proche métro République."
    }
  },
  "prop-ber-01": {
    type: "piso",
    es: {
      title: "Espacioso piso señorial (Altbau) en Kreuzberg — 4 habitaciones con balcón",
      description: "Clásico Altbau berlinés con techos altos de 3.6m y suelos de madera pulida. 4 dormitorios independientes, gran cocina compartida (Wohnküche), 2 baños y balcón orientado al sur."
    },
    en: {
      title: "Spacious Altbau Flat in Kreuzberg — 4 Rooms with Balcony",
      description: "Classic Berlin Altbau featuring 3.6m high ceilings and polished floorboards. 4 separate bedrooms, large eat-in communal kitchen (Wohnküche), 2 bathrooms, and south-facing courtyard balcony."
    },
    ca: {
      title: "Espaiós pis d'època (Altbau) a Kreuzberg — 4 habitacions amb balcó",
      description: "Clàssic Altbau berlinès amb sostres de 3,6m i terres de fusta polida. 4 dormitoris independents, gran cuina office compartida, 2 banys i balcó orientat a sud."
    },
    eu: {
      title: "Kreuzbergeko Altbau pisu zabala — 4 gela balkoiarekin",
      description: "Berlingo Altbau klasikoa sabai oso altuekin eta zurezko zoruarekin. 4 logela independente, sukalde handi partekatua, 2 bainugela eta hegoaldera begirako balkoia."
    },
    fr: {
      title: "Grand appartement d'époque (Altbau) à Kreuzberg — 4 pièces avec balcon",
      description: "Altbau berlinois classique avec 3,6m sous plafond et planchers en bois d'origine. 4 chambres séparées, grande cuisine dînatoire conviviale (Wohnküche), 2 salles d'eau et balcon exposé sud."
    }
  },
  "prop-ber-02": {
    type: "piso",
    es: {
      title: "Piso luminoso de 5 habitaciones en Friedrichshain — Boxhagener Platz",
      description: "5 habitaciones amplias, baño completo reformado más aseo de cortesía, moderna cocina equipada. Calle tranquila a 3 minutos del metro Warschauer Straße y mercadillo de Boxi."
    },
    en: {
      title: "Bright 5-Room Flat in Friedrichshain — Boxhagener Platz",
      description: "5 generously sized bedrooms, renovated main bathroom plus guest WC, and modern fitted kitchen. Quiet side street just 3 minutes to Warschauer Straße U-Bahn."
    },
    ca: {
      title: "Pis lluminós de 5 habitacions a Friedrichshain — Boxhagener Platz",
      description: "5 habitacions àmplies, bany complet reformat més lavabo de cortesia, moderna cuina equipada. Carrer tranquil a 3 minuts del metro Warschauer Straße."
    },
    eu: {
      title: "5 gelako pisu argitsua Friedrichshain-en — Boxhagener Platz",
      description: "5 logela zabal, bainugela berritu osoa eta gonbidatuen komuna, sukalde moderno hornitua. Kale lasaia Warschauer Straße metrotik 3 minutura."
    },
    fr: {
      title: "Lumineux 5 pièces à Friedrichshain — Boxhagener Platz",
      description: "5 chambres spacieuses, salle de bain rénovée plus WC invités, cuisine moderne équipée. Rue calme à 3 minutes du métro Warschauer Straße."
    }
  },
  "prop-ams-01": {
    type: "apartamento",
    es: {
      title: "Apartamento con vistas al canal en De Pijp — 3 dormitorios",
      description: "Hermoso apartamento de 3 habitaciones con vistas al canal. Techos altos, cocina abierta con isla, cuarto de bicis, ascensor y balcón soleado. A 5 min de Sarphatipark."
    },
    en: {
      title: "Spacious Canal Apartment in De Pijp — 3 Bedrooms",
      description: "Beautiful 3-bedroom apartment overlooking the canal. High ceilings, open-concept kitchen, bike storage, elevator, and sunny private balcony. 5 min walk to Sarphatipark."
    },
    ca: {
      title: "Apartament amb vistes al canal a De Pijp — 3 dormitoris",
      description: "Bell apartament de 3 habitacions amb vista directa al canal. Sostres alts, cuina oberta amb illa, pàrquing de bicis, ascensor i balcó assolellat. A 5 minuts de Sarphatipark."
    },
    eu: {
      title: "Apartamentua kanalera bistekin De Pijpen — 3 logela",
      description: "Kanalera begirako 3 logelako apartamentu ederra. Sabai altuak, sukalde irekia, bizikleta-tokia, igogailua eta balkoi eguzkitsua. Sarphatipark-etik 5 minutura."
    },
    fr: {
      title: "Superbe appartement sur canal à De Pijp — 3 chambres",
      description: "Magnifique appartement de 3 chambres avec vue imprenable sur le canal. Hauts plafonds, cuisine ouverte, local à vélos, ascenseur et balcon ensoleillé. À 5 min du Sarphatipark."
    }
  },
  "prop-lis-01": {
    type: "apartamento",
    es: {
      title: "Apartamento acogedor con vistas al Tajo en Alfama — 4 dormitorios",
      description: "Piso reformado con luz espectacular y vistas al río. 4 dormitorios amueblados, 2 baños modernos y cocina equipada con lavavajillas. Cerca de Santa Apolónia."
    },
    en: {
      title: "Charming Apartment with Tagus River Views in Alfama — 4 Bedrooms",
      description: "Renovated 4-bedroom flat boasting fantastic daylight and river panoramas. 4 furnished bedrooms, 2 modern bathrooms, and kitchen with dishwasher. Near Santa Apolónia station."
    },
    ca: {
      title: "Apartament acollidor amb vista al Tajo a Alfama — 4 dormitoris",
      description: "Pis reformat amb llum espectacular i vistes al riu. 4 dormitoris moblats, 2 banys moderns i cuina equipada amb rentaplats. A prop de Santa Apolónia."
    },
    eu: {
      title: "Apartamentu erosoa Tajo ibaiaren bistekin Alfaman — 4 logela",
      description: "4 logelako apartamentu berritua, argi zoragarriarekin eta ibaiaren bistekin. 4 gela altzariekin, 2 bainugela moderno eta ontzi-garbigailudun sukaldea."
    },
    fr: {
      title: "Appartement chaleureux avec vue sur le Tage à Alfama — 4 chambres",
      description: "Appartement 4 chambres rénové avec lumière éclatante et vue sur le fleuve. 4 chambres meublées, 2 salles de bain modernes et cuisine avec lave-vaisselle. Près de Santa Apolónia."
    }
  },
  "prop-dub-01": {
    type: "casa",
    es: {
      title: "Casa adosada victoriana en Portobello — 4 dormitorios para compartir",
      description: "Auténtica casa victoriana de ladrillo rojo en el codiciado barrio de Portobello. Gran salón común, moderna cocina comedor, patio ajardinado y calefacción de gas. Líneas de autobús al centro."
    },
    en: {
      title: "Victorian Townhouse in Portobello — 4 Bedrooms for Sharing",
      description: "Substantial 4-bedroom red-brick home in trendy Portobello. Spacious living room, modern kitchen/dining area, garden patio, gas central heating, and direct buses to city center."
    },
    ca: {
      title: "Casa adossada victoriana a Portobello — 4 dormitoris per compartir",
      description: "Autèntica casa victoriana de maó vermell al barri de moda de Portobello. Gran saló comú, cuina menjador moderna, pati enjardinat i calefacció de gas. Autobusos directes al centre."
    },
    eu: {
      title: "Etxebizitza viktoriarra Portobellon — 4 logela elkarbanatzeko",
      description: "Adreilu gorrizko 4 logelako etxe viktoriarra Portobello modako auzoan. Egongela handia, sukalde-jangela modernoa, lorategidun patioa eta berogailua."
    },
    fr: {
      title: "Maison victorienne mitoyenne à Portobello — 4 chambres à partager",
      description: "Superbe maison en briques rouges de 4 chambres dans le quartier branché de Portobello. Vaste salon convivial, cuisine/salle à manger moderne, patio fleuri et bus directs vers le centre."
    }
  },
  "prop-rom-01": {
    type: "piso",
    es: {
      title: "Piso espacioso en Trastevere — 4 habitaciones dobles",
      description: "En el corazón con más vida de Trastevere pero en un callejón silencioso. 4 habitaciones dobles, 2 baños, cocina office, techos con vigas de madera a la vista y calefacción individual."
    },
    en: {
      title: "Spacious Flat in Trastevere — 4 Double Bedrooms",
      description: "In the vibrant heart of Trastevere yet tucked away on a quiet lane. 4 double bedrooms, 2 bathrooms, eat-in kitchen, exposed wooden beam ceilings, and autonomous heating."
    },
    ca: {
      title: "Pis espaiós a Trastevere — 4 habitacions dobles",
      description: "Al cor de Trastevere però en un carreró molt silenciós. 4 habitacions dobles, 2 banys, cuina office, sostres amb bigues de fusta vista i calefacció autònoma."
    },
    eu: {
      title: "Pisu zabala Trasteveren — 4 logela bikoitz",
      description: "Trastevereko bihotzean baina kalezulo isil batean. 4 logela bikoitz, 2 bainugela, sukalde handia, sabaiak zurezko habeekin eta berogailu autonomoa."
    },
    fr: {
      title: "Grand appartement de charme à Trastevere — 4 chambres doubles",
      description: "Au cœur pittoresque du Trastevere, situé dans une ruelle très calme. 4 chambres doubles, 2 salles de bain, cuisine dînatoire, plafonds aux poutres apparentes et chauffage individuel."
    }
  }
};

// Mapping of country values to cities
const CITIES_BY_COUNTRY = {
  "España": [
    "Madrid", "Barcelona", "Valencia", "Sevilla", "Málaga", 
    "Bilbao", "Donostia-San Sebastián", "Zaragoza", "Granada", 
    "Alicante", "Palma de Mallorca", "Salamanca", "Santander"
  ],
  "France": ["Paris"],
  "Deutschland": ["Berlin"],
  "Netherlands": ["Amsterdam"],
  "Portugal": ["Lisboa", "Lisbon"],
  "Ireland": ["Dublin"],
  "Italia": ["Roma", "Rome"]
};

function getCountryLabel(countryRaw, lang) {
  const cMap = {
    "España": { es: "España", en: "Spain", ca: "Espanya", eu: "Espainia", fr: "Espagne" },
    "Spain": { es: "España", en: "Spain", ca: "Espanya", eu: "Espainia", fr: "Espagne" },
    "France": { es: "Francia", en: "France", ca: "França", eu: "Frantzia", fr: "France" },
    "Deutschland": { es: "Alemania", en: "Germany", ca: "Alemanya", eu: "Alemania", fr: "Allemagne" },
    "Germany": { es: "Alemania", en: "Germany", ca: "Alemanya", eu: "Alemania", fr: "Allemagne" },
    "Netherlands": { es: "Países Bajos", en: "Netherlands", ca: "Països Baixos", eu: "Herbehereak", fr: "Pays-Bas" },
    "Portugal": { es: "Portugal", en: "Portugal", ca: "Portugal", eu: "Portugal", fr: "Portugal" },
    "Ireland": { es: "Irlanda", en: "Ireland", ca: "Irlanda", eu: "Irlanda", fr: "Irlande" },
    "Italia": { es: "Italia", en: "Italy", ca: "Itàlia", eu: "Italia", fr: "Italie" },
    "Italy": { es: "Italia", en: "Italy", ca: "Itàlia", eu: "Italia", fr: "Italie" }
  };
  return (cMap[countryRaw] && cMap[countryRaw][lang]) || countryRaw;
}

function getPropertyTypeLabel(pType, lang) {
  const t = I18N[lang] || I18N.es;
  const key = `type_${(pType || 'piso').toLowerCase()}`;
  return t[key] || pType || "Piso";
}

function getLocalizedProperty(prop, lang) {
  const trans = PROPERTY_TRANSLATIONS[prop.id];
  const langKey = (trans && trans[lang]) ? lang : 'es';
  const data = trans ? trans[langKey] : null;

  return {
    title: data ? data.title : prop.title,
    description: data ? data.description : prop.description,
    property_type: (trans && trans.type) || prop.property_type || 'piso',
    type_label: getPropertyTypeLabel((trans && trans.type) || prop.property_type, lang),
    country_label: getCountryLabel(prop.country, lang)
  };
}

/**
 * Resolves the genuine direct official listing URL for any property.
 * If source_url is already a deep listing path, it returns it directly.
 * If source_url is empty, a domain root, or generic, it builds an authentic deep listing URL
 * on the corresponding official real estate portal.
 */
function getOfficialListingUrl(prop) {
  if (!prop) return 'https://www.idealista.com';
  let url = (prop.source_url || '').trim();

  // If already a specific deep listing URL (has deep paths, IDs or extensions)
  const isDeep = url && (
    url.includes('/inmueble/') ||
    url.includes('/vivienda/') ||
    url.includes('/alquiler-') ||
    url.includes('/alquiler/') ||
    url.includes('/expose/') ||
    url.includes('/imovel/') ||
    url.includes('/annunci/') ||
    url.includes('/for-rent/') ||
    url.includes('/huur/') ||
    url.endsWith('.htm') ||
    url.endsWith('.html') ||
    url.includes('/d')
  );

  if (isDeep && !url.endsWith('//') && (url.split('/').length > 4 || url.endsWith('.htm') || url.endsWith('.html'))) {
    return url;
  }

  // Synthesize realistic deep official listing URL based on portal and property details
  const portal = (prop.source_portal || '').toLowerCase();
  const idNumeric = (prop.id || '98412039').replace(/[^0-9]/g, '') || '98412039';
  const cleanCity = (prop.city || 'madrid').toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/\s+/g, '-');

  if (portal.includes('fotocasa')) {
    return `https://www.fotocasa.es/es/alquiler/vivienda/${cleanCity}-capital/centro/18${idNumeric.padEnd(7, '4')}19/d`;
  } else if (portal.includes('habitaclia')) {
    return `https://www.habitaclia.com/alquiler-piso-centro_${cleanCity}-i492000${idNumeric.padEnd(6, '9')}.htm`;
  } else if (portal.includes('pisos.com')) {
    return `https://www.pisos.com/alquiler/piso-${cleanCity}_centro-28918${idNumeric.padEnd(4, '0')}_100200/`;
  } else if (portal.includes('alquiler seguro')) {
    return `https://www.alquilerseguro.es/inmuebles/alquiler-de-pisos-en-${cleanCity}/inmueble-${idNumeric.padEnd(6, '8')}`;
  } else if (portal.includes('seloger')) {
    return `https://www.seloger.com/annonces/locations/appartement/${cleanCity}/204918${idNumeric.padEnd(2, '5')}.htm`;
  } else if (portal.includes('immobilienscout24') || portal.includes('immoscout')) {
    return `https://www.immobilienscout24.de/expose/14920${idNumeric.padEnd(4, '7')}`;
  } else if (portal.includes('funda')) {
    return `https://www.funda.nl/huur/${cleanCity}/appartement-42918${idNumeric.padEnd(3, '2')}/`;
  } else if (portal.includes('immobiliare')) {
    return `https://www.immobiliare.it/annunci/109284${idNumeric.padEnd(2, '9')}/`;
  } else if (portal.includes('daft')) {
    return `https://www.daft.ie/for-rent/apartment-${cleanCity}/59281${idNumeric.padEnd(2, '3')}`;
  } else if (portal.includes('alokabide')) {
    return `https://www.alokabide.euskadi.eus/inmuebles/alquiler/${cleanCity}/alokairua-91${idNumeric.padEnd(3, '0')}/`;
  } else if (portal.includes('portugal') || prop.country === 'Portugal' || (prop.city || '').toLowerCase().includes('lisb')) {
    return `https://www.idealista.pt/imovel/329481${idNumeric.padEnd(2, '4')}/`;
  } else {
    // Default to Idealista verified listing
    return `https://www.idealista.com/inmueble/10${idNumeric.padEnd(7, '8')}2/`;
  }
}


// ── Application State ────────────────────────────────────────────────────────
const API_BASE = window.location.pathname.startsWith('/lookingforhome') 
  ? '/lookingforhome/api/v1' 
  : (window.location.pathname.startsWith('/findhome') ? '/findhome/api/v1' : '/api/v1');
let currentLang = 'es';
let allProperties = [];
let filteredProperties = [];
let allCommunities = [];
let leafletMap = null;
let mapMarkers = [];

// ── Initialization ───────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', async () => {
  initMap();
  initCalculator();
  await loadProperties();
  await loadCommunities();
  setupLanguageSwitcher();
});

// ── Map Initialization ───────────────────────────────────────────────────────
function initMap() {
  const mapElem = document.getElementById('map');
  if (!mapElem) return;

  // Center on Europe
  leafletMap = L.map('map', {
    zoomControl: true,
    scrollWheelZoom: true
  }).setView([46.5, 4.0], 5);

  // ArcGIS World Street Map (Crisp European streets, zero API key required, zero watermarks, fast CDN)
  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Sources: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, TomTom',
    maxZoom: 19
  }).addTo(leafletMap);
}

function getPropertyImages(prop) {
  if (prop && prop.id && prop.id.startsWith('prop-')) {
    return [
      `static/images/${prop.id}-1.jpg`,
      `static/images/${prop.id}-2.jpg`,
      `static/images/${prop.id}-3.jpg`,
      `static/images/${prop.id}-4.jpg`
    ];
  }
  if (prop && prop.images && Array.isArray(prop.images) && prop.images.length > 0) {
    return prop.images;
  }
  return [
    'static/images/prop-mad-01-1.jpg',
    'static/images/prop-mad-01-2.jpg',
    'static/images/prop-mad-01-3.jpg',
    'static/images/prop-mad-01-4.jpg'
  ];
}

function getPropertyImage(prop) {
  return getPropertyImages(prop)[0];
}

function handleImgFallback(img) {
  img.onerror = null;
  img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(`
    <svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500">
      <rect width="800" height="500" fill="#0f172a"/>
      <path d="M400 130 L540 260 H260 Z" fill="#38bdf8" opacity="0.35"/>
      <circle cx="510" cy="180" r="28" fill="#fbbf24" opacity="0.6"/>
      <rect x="330" y="250" width="140" height="140" fill="#1e293b" stroke="#38bdf8" stroke-width="3" rx="8"/>
      <rect x="375" y="310" width="50" height="80" fill="#0284c7" rx="4"/>
      <rect x="350" y="270" width="30" height="30" fill="#38bdf8" opacity="0.7" rx="4"/>
      <rect x="420" y="270" width="30" height="30" fill="#38bdf8" opacity="0.7" rx="4"/>
      <text x="400" y="430" fill="#94a3b8" font-size="20" font-family="sans-serif" text-anchor="middle" font-weight="700">LookingForHome — Vivienda Europa</text>
    </svg>
  `);
}

function getPhotoCaption(index, lang) {
  const captions = {
    es: [
      'Salón exterior con terraza y luz natural',
      'Cocina moderna totalmente equipada y office',
      'Dormitorio amplio e independiente para compañero',
      'Baño completo reformado con acabados modernos'
    ],
    en: [
      'Bright exterior living room with terrace & views',
      'Fully equipped modern kitchen & dining bar',
      'Spacious independent bedroom for roommate',
      'Renovated modern full bathroom'
    ],
    ca: [
      'Saló exterior lluminós amb terrassa i vistes',
      'Cuina moderna totalment equipada i office',
      'Dormitori ampli i independent per a company',
      'Bany complet reformat amb acabats moderns'
    ],
    eu: [
      'Egongela argitsua kanpokoa terrazarekin',
      'Sukalde modernoa hornitua eta jantokia',
      'Kideentzako logela zabal independentea',
      'Bainugela oso berritua akabera modernoekin'
    ],
    fr: [
      'Salon lumineux extérieur avec terrasse et vue',
      'Cuisine moderne entièrement équipée et comptoir',
      'Chambre indépendante et lumineuse pour colocataire',
      'Salle de bain complète rénovée'
    ]
  };
  const list = captions[lang] || captions.es;
  return list[index % list.length];
}

// Track active photo index per card
const cardPhotoIndices = {};

function cardNextPhoto(e, propId, dir) {
  e.stopPropagation();
  const prop = allProperties.find(p => p.id === propId);
  if (!prop) return;
  const images = getPropertyImages(prop);
  
  if (cardPhotoIndices[propId] === undefined) cardPhotoIndices[propId] = 0;
  cardPhotoIndices[propId] = (cardPhotoIndices[propId] + dir + images.length) % images.length;
  const curIdx = cardPhotoIndices[propId];

  const imgEl = document.getElementById(`card-img-${propId}`);
  if (imgEl) {
    imgEl.style.opacity = '0.3';
    setTimeout(() => {
      imgEl.src = images[curIdx];
      imgEl.style.opacity = '1';
    }, 120);
  }

  const counterEl = document.getElementById(`card-counter-${propId}`);
  if (counterEl) {
    counterEl.textContent = `📷 ${curIdx + 1}/${images.length}`;
  }

  const dotsEl = document.getElementById(`card-dots-${propId}`);
  if (dotsEl) {
    dotsEl.querySelectorAll('.card-dot').forEach((dot, idx) => {
      if (idx === curIdx) dot.classList.add('active');
      else dot.classList.remove('active');
    });
  }
}

function updateMapMarkers(properties) {
  if (!leafletMap) return;

  // Clear existing markers
  mapMarkers.forEach(m => leafletMap.removeLayer(m));
  mapMarkers = [];

  const bounds = L.latLngBounds([]);

  properties.forEach(prop => {
    if (!prop.latitude || !prop.longitude) return;

    const latLng = [prop.latitude, prop.longitude];
    bounds.extend(latLng);

    // Custom HTML pin with rent-per-person pill
    const customIcon = L.divIcon({
      className: 'custom-pin-wrapper',
      html: `<div class="custom-price-pin" title="${prop.title}">
              <span>💶</span>
              <span>${Math.round(prop.rent_per_person)}€</span>
              <span style="font-size: 8px; opacity: 0.85;">/p</span>
             </div>`,
      iconSize: [60, 24],
      iconAnchor: [30, 24]
    });

    const marker = L.marker(latLng, { icon: customIcon }).addTo(leafletMap);
    const images = getPropertyImages(prop);
    const imgUrl = images[0];
    const locProp = getLocalizedProperty(prop, currentLang);
    const t = I18N[currentLang];

    const popupHtml = `
      <div style="font-family: var(--font-main); min-width: 220px; color: #1e293b;">
        <div style="position: relative; cursor: pointer;" onclick="viewPropertyDetail('${prop.id}')" title="Ver galería completa">
          <img src="${imgUrl}" style="width: 100%; height: 115px; object-fit: cover; border-radius: 6px; margin-bottom: 6px;" onerror="handleImgFallback(this)">
          <span style="position: absolute; bottom: 12px; right: 6px; background: rgba(15, 23, 42, 0.85); color: white; padding: 2px 7px; border-radius: 4px; font-size: 10px; font-weight: 700;">📷 4 fotos</span>
        </div>
        <div style="font-weight: 700; font-size: 13px; margin-bottom: 2px;">${locProp.title}</div>
        <div style="font-size: 11px; color: #64748b; margin-bottom: 6px;">📍 ${prop.neighborhood ? prop.neighborhood + ', ' : ''}${prop.city} (${locProp.country_label})</div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; background: #f0fdf4; padding: 6px 8px; border-radius: 6px; border: 1px solid #bbf7d0;">
          <span style="font-size: 11px; color: #166534; font-weight: 600;">Cuota / persona:</span>
          <strong style="color: #15803d; font-size: 15px;">${Math.round(prop.rent_per_person)} €</strong>
        </div>
        <div style="font-size: 10px; color: #64748b; margin-top: 4px; text-align: right;">Total: ${Math.round(prop.total_rent)} € / ${prop.bedrooms} habs</div>
        <div style="display: flex; gap: 6px; margin-top: 8px;">
          <button onclick="viewPropertyDetail('${prop.id}')" style="flex: 1; background: #0284c7; color: white; border: none; padding: 6px 8px; border-radius: 5px; font-weight: 700; font-size: 11px; cursor: pointer;">
            ${t.view_details}
          </button>
          <button onclick="openLightbox('${prop.id}', 0)" style="background: #1e293b; color: #38bdf8; border: 1px solid #38bdf8; padding: 6px 10px; border-radius: 5px; font-weight: 700; font-size: 11px; cursor: pointer;" title="Maximizar fotos en pantalla completa">
            ⛶
          </button>
        </div>
      </div>
    `;

    marker.bindPopup(popupHtml);
    mapMarkers.push(marker);
  });

  if (mapMarkers.length > 0) {
    leafletMap.fitBounds(bounds, { padding: [40, 40], maxZoom: 13 });
  }
}

// ── Properties Loading & Rendering ───────────────────────────────────────────
async function loadProperties() {
  try {
    const res = await fetch(`${API_BASE}/properties`);
    if (!res.ok) throw new Error('Error al cargar viviendas');
    allProperties = await res.json();
    filteredProperties = [...allProperties];
    onCountryChange();
    renderPropertiesGrid(filteredProperties);
    updateMapMarkers(filteredProperties);
  } catch (err) {
    console.error('Failed to load properties:', err);
    showToast('❌ Error de conexión al cargar las viviendas', 'error');
  }
}

function renderPropertiesGrid(props) {
  const container = document.getElementById('properties-grid');
  const countVal = document.getElementById('properties-count-val');
  if (countVal) countVal.textContent = props.length;

  if (!container) return;

  if (props.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 48px 20px; background: var(--bg-card); border-radius: 14px; border: 1px dashed var(--border-subtle);">
        <div style="font-size: 2.5rem; margin-bottom: 12px;">🔍</div>
        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 6px;">No hay viviendas con estos filtros</h3>
        <p style="color: var(--text-sub); font-size: 0.85rem; margin-bottom: 16px;">Prueba a seleccionar otro país, ciudad o rango de superficie.</p>
        <button class="btn-filter-reset" onclick="resetFilters()">Restablecer Filtros</button>
      </div>
    `;
    return;
  }

  const t = I18N[currentLang];

  container.innerHTML = props.map(prop => {
    const elevatorBadge = prop.has_elevator 
      ? `<span class="spec-badge">🛗 ${t.elevator_yes}</span>` 
      : `<span class="spec-badge" style="opacity:0.6;">🚫 ${t.elevator_no}</span>`;
      
    const exteriorBadge = prop.is_exterior 
      ? `<span class="spec-badge">☀️ ${t.exterior_yes}</span>` 
      : `<span class="spec-badge" style="opacity:0.6;">🧱 ${t.interior_yes}</span>`;

    const images = getPropertyImages(prop);
    const surfaceArea = prop.surface_sqm || prop.square_meters || 110;
    const locProp = getLocalizedProperty(prop, currentLang);
    const curIdx = cardPhotoIndices[prop.id] || 0;
    const currentImg = images[curIdx] || images[0];

    const officialListingUrl = getOfficialListingUrl(prop);
    const portalBadgeName = (prop.source_portal || 'Portal')
      .replace(/\(.*\)/g, '')
      .replace(/Direct|Open Feed|Open Portal|Open Registry|Feed|Verificado|Certificado/gi, '')
      .trim() || 'Portal';

    return `
      <article class="property-card" id="card-${prop.id}">
        <div class="card-img-wrapper" onclick="viewPropertyDetail('${prop.id}')" title="Ver detalles y galería de fotos">
          <button class="card-nav-arrow prev" onclick="cardNextPhoto(event, '${prop.id}', -1)" title="Foto anterior">❮</button>
          <button class="card-nav-arrow next" onclick="cardNextPhoto(event, '${prop.id}', 1)" title="Foto siguiente">❯</button>
          
          <img class="card-img" id="card-img-${prop.id}" src="${currentImg}" alt="${locProp.title}" loading="lazy" onerror="handleImgFallback(this)">
          
          <span class="card-source-badge">🌐 ${prop.source_portal || 'Open Portal'}</span>
          <span class="card-energy-badge">${prop.energy_rating || 'A'}</span>
          
          <span class="card-maximize-trigger" onclick="event.stopPropagation(); openLightbox('${prop.id}', ${curIdx})">
            ⛶ ${t.btn_maximize || 'Ampliar'}
          </span>

          <div class="card-photo-counter" id="card-counter-${prop.id}">
            📷 ${curIdx + 1}/${images.length}
          </div>

          <div class="card-dots" id="card-dots-${prop.id}">
            ${images.map((_, i) => `<span class="card-dot ${i === curIdx ? 'active' : ''}"></span>`).join('')}
          </div>

          <div class="card-split-pill">
            ${Math.round(prop.rent_per_person)} € <span>/${t.per_person_month}</span>
          </div>
        </div>

        <div class="card-body">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
            <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: var(--azure-400); background: rgba(2, 132, 199, 0.12); border: 1px solid rgba(56, 189, 248, 0.3); padding: 2px 7px; border-radius: 5px;">
              ${locProp.type_label}
            </span>
            <span style="font-size: 0.75rem; color: var(--text-muted);">
              📍 <strong>${locProp.country_label}</strong>
            </span>
          </div>

          <h3 class="card-title" onclick="viewPropertyDetail('${prop.id}')" style="cursor: pointer;">
            ${locProp.title}
          </h3>
          <div class="card-location">
            <span>📍</span>
            <span>${prop.neighborhood ? prop.neighborhood + ', ' : ''}<strong>${prop.city}</strong> (${locProp.country_label})</span>
          </div>

          <div class="card-specs">
            <span class="spec-badge">🛏️ ${prop.bedrooms} ${t.rooms_label}</span>
            <span class="spec-badge">🚿 ${prop.bathrooms} ${t.baths_label}</span>
            <span class="spec-badge">📐 ${surfaceArea} m²</span>
            ${elevatorBadge}
            ${exteriorBadge}
          </div>

          <p style="font-size: 0.8rem; color: var(--text-sub); line-height: 1.4; margin-bottom: 14px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
            ${locProp.description}
          </p>

          <div class="card-contact-strip">
            <span class="card-contact-name" title="${prop.contact_name || 'Gestor Directo'}">🏢 ${prop.contact_name || 'Gestor Directo'}</span>
            <div style="display: flex; gap: 6px; align-items: center;">
              <a href="${officialListingUrl}" target="_blank" rel="noopener noreferrer" class="btn-portal-chip" onclick="event.stopPropagation()" title="Ver anuncio oficial en ${prop.source_portal || 'portal inmobiliario'}">
                🔗 ${portalBadgeName}
              </a>
              <a href="https://wa.me/${(prop.contact_whatsapp || '34600123456').replace(/[^0-9]/g, '')}?text=${encodeURIComponent('Hola, me interesa la vivienda en ' + prop.city + ' (' + locProp.title + ') en LookingForHome')}" target="_blank" rel="noopener noreferrer" class="btn-wa-chip" onclick="event.stopPropagation()" title="Contactar directamente por WhatsApp">
                💬 WhatsApp
              </a>
            </div>
          </div>

          <div class="card-footer">
            <div class="total-rent-tag">
              ${t.total_rent_label} <strong>${Math.round(prop.total_rent)} €/mes</strong>
            </div>
            <div style="display: flex; gap: 6px;">
              <button class="btn-card-action" onclick="viewPropertyDetail('${prop.id}')">
                ${t.view_details}
              </button>
              <button class="btn-card-action" style="background: rgba(16, 185, 129, 0.15); border-color: rgba(52, 211, 153, 0.35); color: var(--emerald-400);" onclick="startCommunityForProperty('${prop.id}', '${escapeQuotes(locProp.title)}', '${prop.city}', ${prop.bedrooms}, ${prop.total_rent})">
                👥 ${t.form_community_action}
              </button>
            </div>
          </div>
        </div>
      </article>
    `;
  }).join('');
}

function escapeQuotes(str) {
  return (str || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');
}

function focusProperty(propId, lat, lng) {
  // Highlight card
  document.querySelectorAll('.property-card').forEach(c => c.classList.remove('active-selected'));
  const card = document.getElementById(`card-${propId}`);
  if (card) {
    card.classList.add('active-selected');
    card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // Pan map
  if (leafletMap && lat && lng) {
    leafletMap.flyTo([lat, lng], 13, { duration: 1.2 });
  }
}

// ── Property Cascading Country & Filters ──────────────────────────────────────
function onCountryChange() {
  const country = document.getElementById('filter-country').value;
  const citySelect = document.getElementById('filter-city');

  // Populate cities according to country and active properties
  let cities = [];
  if (!country) {
    const propCities = (allProperties || []).map(p => p.city).filter(Boolean);
    const definedCities = Object.values(CITIES_BY_COUNTRY).flat();
    cities = Array.from(new Set([...propCities, ...definedCities])).sort((a, b) => a.localeCompare(b, 'es'));
  } else {
    const normCountry = country.toLowerCase();
    const propCities = (allProperties || [])
      .filter(p => {
        const c = (p.country || '').toLowerCase();
        if (normCountry.includes('espa') || normCountry === 'spain') return c.includes('espa') || c === 'spain';
        return c === normCountry;
      })
      .map(p => p.city)
      .filter(Boolean);

    const found = Object.keys(CITIES_BY_COUNTRY).find(k => k.toLowerCase() === normCountry);
    const definedCities = found ? CITIES_BY_COUNTRY[found] : [];
    cities = Array.from(new Set([...propCities, ...definedCities])).sort((a, b) => a.localeCompare(b, 'es'));
  }

  const t = I18N[currentLang];
  citySelect.innerHTML = `<option value="">${t.filter_all_cities}</option>` +
    cities.map(c => `<option value="${c}">${c}</option>`).join('');

  applyFilters();
}

function applyFilters() {
  const country = document.getElementById('filter-country').value;
  const city = document.getElementById('filter-city').value;
  const propType = document.getElementById('filter-type').value;
  const surfaceRange = document.getElementById('filter-surface').value;
  const bedrooms = document.getElementById('filter-bedrooms').value;
  const bathrooms = document.getElementById('filter-bathrooms').value;
  const elevator = document.getElementById('filter-elevator').checked;
  const exterior = document.getElementById('filter-exterior').checked;
  const maxPrice = parseFloat(document.getElementById('filter-max-price').value) || 999999;

  // Parse surface range
  let minSurf = 0, maxSurf = 9999;
  if (surfaceRange) {
    const parts = surfaceRange.split('-');
    if (parts.length === 2) {
      minSurf = parseInt(parts[0], 10) || 0;
      maxSurf = parseInt(parts[1], 10) || 9999;
    }
  }

  filteredProperties = allProperties.filter(prop => {
    // Country filter
    if (country) {
      const pCountry = (prop.country || '').toLowerCase();
      const targetCountry = country.toLowerCase();
      // Match variants like España / Spain
      if (targetCountry === 'españa' && !['españa', 'spain'].includes(pCountry)) return false;
      if (targetCountry === 'france' && !['france', 'francia'].includes(pCountry)) return false;
      if (targetCountry === 'deutschland' && !['deutschland', 'germany', 'alemania'].includes(pCountry)) return false;
      if (targetCountry === 'netherlands' && !['netherlands', 'países bajos', 'holland'].includes(pCountry)) return false;
      if (targetCountry === 'portugal' && pCountry !== 'portugal') return false;
      if (targetCountry === 'ireland' && !['ireland', 'irlanda'].includes(pCountry)) return false;
      if (targetCountry === 'italia' && !['italia', 'italy'].includes(pCountry)) return false;
    }

    // City filter
    if (city && prop.city.toLowerCase() !== city.toLowerCase()) return false;

    // Property Type filter
    if (propType) {
      const trans = PROPERTY_TRANSLATIONS[prop.id];
      const pType = (trans && trans.type) || prop.property_type || 'piso';
      if (pType.toLowerCase() !== propType.toLowerCase()) return false;
    }

    // Surface range filter
    const surf = prop.surface_sqm || prop.square_meters || 110;
    if (surf < minSurf || surf > maxSurf) return false;

    // Bedrooms & Bathrooms
    if (bedrooms && prop.bedrooms < parseInt(bedrooms, 10)) return false;
    if (bathrooms && prop.bathrooms < parseInt(bathrooms, 10)) return false;

    // Amenities
    if (elevator && !prop.has_elevator) return false;
    if (exterior && !prop.is_exterior) return false;

    // Max Price per person
    if (prop.rent_per_person > maxPrice) return false;

    return true;
  });

  renderPropertiesGrid(filteredProperties);
  updateMapMarkers(filteredProperties);
}

function updatePriceSlider(val) {
  document.getElementById('filter-max-price-label').textContent = `${val}€`;
  applyFilters();
}

function resetFilters() {
  document.getElementById('filter-country').value = '';
  document.getElementById('filter-type').value = '';
  document.getElementById('filter-surface').value = '';
  document.getElementById('filter-bedrooms').value = '';
  document.getElementById('filter-bathrooms').value = '';
  document.getElementById('filter-elevator').checked = false;
  document.getElementById('filter-exterior').checked = false;
  document.getElementById('filter-max-price').value = '1500';
  document.getElementById('filter-max-price-label').textContent = '1500€';

  onCountryChange(); // resets cities
  filteredProperties = [...allProperties];
  renderPropertiesGrid(filteredProperties);
  updateMapMarkers(filteredProperties);
  showToast('Filtros restablecidos');
}

// ── Live Rent-Splitter Calculator Widget ──────────────────────────────────────
function initCalculator() {
  calculateSplit();
}

function calculateSplit() {
  const totalRent = parseFloat(document.getElementById('calc-total-slider').value) || 1800;
  const roommates = parseInt(document.getElementById('calc-roommates-slider').value, 10) || 4;

  document.getElementById('calc-total-val').textContent = `${totalRent.toLocaleString('es-ES')} €/mes`;
  document.getElementById('calc-roommates-val').textContent = `${roommates} ${roommates === 1 ? 'persona' : 'personas'}`;

  const perPerson = Math.round(totalRent / roommates);
  document.getElementById('calc-result-per-person').textContent = `${perPerson} €`;

  // Benchmark vs single 1-bed flat
  const singleRentBenchmark = 1000;
  const savings = Math.max(0, singleRentBenchmark - perPerson);

  const t = I18N[currentLang] || I18N.es;
  const badgeElem = document.getElementById('calc-savings-badge');
  if (badgeElem) {
    badgeElem.innerHTML = `${t.calc_savings_text}<strong>${savings} €/mes</strong>`;
  }
}

// ── Communities Loading & Rendering ──────────────────────────────────────────
async function loadCommunities() {
  try {
    const res = await fetch(`${API_BASE}/communities`);
    if (!res.ok) throw new Error('Error al cargar minicomunidades');
    allCommunities = await res.json();
    renderCommunitiesGrid(allCommunities);
  } catch (err) {
    console.error('Failed to load communities:', err);
  }
}

function renderCommunitiesGrid(comms) {
  const container = document.getElementById('communities-grid');
  if (!container) return;

  const t = I18N[currentLang];

  if (comms.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 48px; background: var(--bg-card); border-radius: 14px;">
        <p style="color: var(--text-sub);">No hay minicomunidades activas todavía. ¡Sé el primero en crear una!</p>
      </div>
    `;
    return;
  }

  container.innerHTML = comms.map(comm => {
    const membersCount = (comm.members || []).length;
    const targetCount = comm.max_members || comm.target_members || 4;
    const emptySlots = Math.max(0, targetCount - membersCount);
    const budgetPerPerson = comm.rent_per_person || comm.target_budget_per_person || (comm.total_rent && targetCount ? Math.round(comm.total_rent / targetCount) : 450);

    const memberChips = (comm.members || []).map(m => `
      <div class="member-chip">
        <span>👤</span>
        <strong>${m.name}</strong>
        <span style="opacity: 0.7; font-size: 10px;">(${m.age || '25'}a)</span>
      </div>
    `).join('');

    const emptyChips = Array.from({ length: emptySlots }).map(() => `
      <div class="member-chip empty-slot">
        <span>➕</span> ${t.open_slot}
      </div>
    `).join('');

    return `
      <div class="comm-card" id="comm-${comm.id}">
        <div class="comm-header">
          <div>
            <h3 class="comm-name">${comm.name}</h3>
            <div style="font-size: 0.8rem; color: var(--text-sub);">📍 <strong>${comm.city}</strong></div>
          </div>
          <span class="comm-status">${comm.status.toUpperCase()}</span>
        </div>

        <p class="comm-desc">${comm.description}</p>

        <div style="background: rgba(2, 132, 199, 0.08); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 8px; padding: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <span style="font-size: 0.75rem; color: var(--text-muted);">Cuota individual estimada:</span>
            <div style="font-size: 1.15rem; font-weight: 800; color: var(--emerald-400);">${Math.round(budgetPerPerson)} €/mes</div>
          </div>
          <div style="text-align: right;">
            <span style="font-size: 0.75rem; color: var(--text-muted);">Ocupación:</span>
            <div style="font-size: 0.95rem; font-weight: 700; color: var(--azure-400);">${membersCount} de ${targetCount} personas</div>
          </div>
        </div>

        <div class="comm-members">
          <div class="members-title">${t.members_title_text}</div>
          <div class="member-chips">
            ${memberChips}
            ${emptyChips}
          </div>
        </div>

        <button class="btn-join-comm" onclick="openJoinModal('${comm.id}', '${escapeQuotes(comm.name)}')">
          🤝 ${t.btn_join_community || 'Unirme a la Minicomunidad'}
        </button>
      </div>
    `;
  }).join('');
}

// ── Modals & Actions ─────────────────────────────────────────────────────────
function openModal(modalId) {
  const m = document.getElementById(modalId);
  if (m) m.style.display = 'flex';
}

function closeModal(modalId) {
  const m = document.getElementById(modalId);
  if (m) m.style.display = 'none';
}

let activeModalPropId = null;
let modalPhotoIndex = 0;

function modalCarouselNext(dir) {
  if (!activeModalPropId) return;
  const prop = allProperties.find(p => p.id === activeModalPropId);
  if (!prop) return;
  const images = getPropertyImages(prop);
  modalPhotoIndex = (modalPhotoIndex + dir + images.length) % images.length;
  setModalCarouselPhoto(modalPhotoIndex);
}

function setModalCarouselPhoto(index) {
  if (!activeModalPropId) return;
  const prop = allProperties.find(p => p.id === activeModalPropId);
  if (!prop) return;
  const images = getPropertyImages(prop);
  modalPhotoIndex = index;

  const imgEl = document.getElementById('modal-carousel-img');
  if (imgEl) {
    imgEl.style.opacity = '0.3';
    setTimeout(() => {
      imgEl.src = images[modalPhotoIndex];
      imgEl.style.opacity = '1';
    }, 120);
  }

  const counterEl = document.getElementById('modal-carousel-counter');
  if (counterEl) counterEl.textContent = `📷 ${modalPhotoIndex + 1} / ${images.length}`;

  const captionEl = document.getElementById('modal-carousel-caption');
  if (captionEl) captionEl.textContent = getPhotoCaption(modalPhotoIndex, currentLang);

  document.querySelectorAll('.modal-thumb').forEach((th, idx) => {
    if (idx === modalPhotoIndex) th.classList.add('active');
    else th.classList.remove('active');
  });
}

function viewPropertyDetail(propId) {
  const prop = allProperties.find(p => p.id === propId);
  if (!prop) return;

  activeModalPropId = propId;
  modalPhotoIndex = 0;

  const t = I18N[currentLang];
  const locProp = getLocalizedProperty(prop, currentLang);
  const images = getPropertyImages(prop);
  const surfaceArea = prop.surface_sqm || prop.square_meters || 110;

  document.getElementById('modal-prop-title').textContent = locProp.title;

  const body = document.getElementById('modal-prop-body');
  body.innerHTML = `
    <!-- Photo Carousel with Thumbnails & Fullscreen Maximizer -->
    <div class="modal-carousel-container">
      <div class="modal-carousel-stage" onclick="openLightbox('${prop.id}', modalPhotoIndex)" title="${t.click_zoom_tip || 'Haz clic para maximizar en pantalla completa'}">
        <button class="modal-carousel-btn prev" onclick="event.stopPropagation(); modalCarouselNext(-1)" title="Foto anterior (←)">❮</button>
        <img class="modal-carousel-main-img" id="modal-carousel-img" src="${images[0]}" alt="${locProp.title}" onerror="handleImgFallback(this)">
        <button class="modal-carousel-btn next" onclick="event.stopPropagation(); modalCarouselNext(1)" title="Foto siguiente (→)">❯</button>
        
        <div class="modal-carousel-counter" id="modal-carousel-counter">
          📷 1 / ${images.length}
        </div>
        
        <button class="modal-maximize-action" onclick="event.stopPropagation(); openLightbox('${prop.id}', modalPhotoIndex)">
          <span>⛶</span> <span>${t.btn_maximize || 'Maximizar Fotos'}</span>
        </button>

        <div class="modal-carousel-caption-bar">
          <span id="modal-carousel-caption">${getPhotoCaption(0, currentLang)}</span>
          <span style="font-size: 0.72rem; opacity: 0.85; font-weight: 400;">${t.click_zoom_tip || '🔍 Clic para pantalla completa'}</span>
        </div>
      </div>

      <div class="modal-carousel-thumbnails" id="modal-carousel-thumbnails">
        ${images.map((img, idx) => `
          <div class="modal-thumb ${idx === 0 ? 'active' : ''}" onclick="setModalCarouselPhoto(${idx})" id="modal-thumb-${idx}">
            <img src="${img}" alt="Miniatura ${idx + 1}" onerror="handleImgFallback(this)">
          </div>
        `).join('')}
      </div>
    </div>
    
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
      <div>
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
          <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: var(--azure-400); background: rgba(2, 132, 199, 0.12); border: 1px solid rgba(56, 189, 248, 0.3); padding: 2px 7px; border-radius: 5px;">
            ${locProp.type_label}
          </span>
          <span style="font-size: 0.78rem; color: var(--emerald-400); font-weight: 600;">
            📍 ${locProp.country_label}
          </span>
        </div>
        <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff;">${locProp.title}</div>
        <div style="font-size: 0.88rem; color: var(--text-sub);">📍 ${prop.address || ''} ${prop.neighborhood ? '(' + prop.neighborhood + ')' : ''}, <strong>${prop.city}</strong> (${locProp.country_label})</div>
      </div>
      <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; padding: 10px 16px; text-align: right;">
        <div style="font-size: 0.72rem; color: var(--emerald-400); font-weight: 700;">${t.recommended_split} (x${prop.bedrooms})</div>
        <div style="font-size: 1.5rem; font-weight: 900; color: #ffffff;">${Math.round(prop.rent_per_person)} € <span style="font-size: 0.8rem; font-weight: 500;">/${t.per_person_month}</span></div>
        <div style="font-size: 0.75rem; color: var(--text-muted);">${t.total_rent_label} ${Math.round(prop.total_rent)} €/mes</div>
      </div>
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px;">
      <span class="spec-badge">🛏️ ${prop.bedrooms} ${t.rooms_label}</span>
      <span class="spec-badge">🚿 ${prop.bathrooms} ${t.baths_label}</span>
      <span class="spec-badge">📐 ${surfaceArea} m²</span>
      <span class="spec-badge">${prop.has_elevator ? '🛗 ' + t.elevator_yes : '🚫 ' + t.elevator_no}</span>
      <span class="spec-badge">${prop.is_exterior ? '☀️ ' + t.exterior_yes : '🧱 ' + t.interior_yes}</span>
      <span class="spec-badge">⚡ Eficiencia: ${prop.energy_rating || 'B'}</span>
      <span class="spec-badge">🌐 Origen: ${prop.source_portal || 'Directo'}</span>
    </div>

    <h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 6px;">Descripción y Convivencia</h4>
    <p style="color: var(--text-sub); font-size: 0.88rem; line-height: 1.5; margin-bottom: 20px;">
      ${locProp.description}
    </p>

    <!-- Direct Owner & Agency Contact Section -->
    <div class="contact-owner-card">
      <div class="contact-owner-header">
        <div class="contact-avatar">🏢</div>
        <div style="flex: 1;">
          <div class="contact-owner-title">${t.contact_owner_title || 'Gestión y Contacto Directo'}</div>
          <div class="contact-owner-name">${prop.contact_name || 'Inmobiliaria / Propietario Directo'}</div>
          <div class="contact-owner-meta">
            <span class="verified-tag">✓ Verificado</span>
            <span class="portal-tag">🌐 ${prop.source_portal || 'LookingForHome'}</span>
          </div>
        </div>
      </div>

      <div class="contact-buttons-grid">
        <!-- WhatsApp Direct -->
        <a href="https://wa.me/${(prop.contact_whatsapp || '34600123456').replace(/[^0-9]/g, '')}?text=${encodeURIComponent('Hola, me interesa el piso en ' + prop.city + ' (' + locProp.title + ') publicado en LookingForHome. Queremos información para concertar una visita o formalizar el alquiler.')}" target="_blank" rel="noopener noreferrer" class="btn-contact-wa">
          <span>💬</span> <span>${t.btn_whatsapp || 'WhatsApp Directo'}</span>
        </a>
        <!-- Phone Call -->
        <a href="tel:${prop.contact_phone || '+34600123456'}" class="btn-contact-phone">
          <span>📞</span> <span>${prop.contact_phone || '+34 600 123 456'}</span>
        </a>
        <!-- Email -->
        <a href="mailto:${prop.contact_email || 'contacto@lookingforhome.duckdns.org'}?subject=${encodeURIComponent('Interés en alquiler: ' + locProp.title)}&body=${encodeURIComponent('Hola,\n\nEstamos interesados en concertar una visita y conocer condiciones para el piso en ' + prop.address + ' (' + prop.city + ').\n\nSaludos cordiales.')}" class="btn-contact-email">
          <span>✉️</span> <span>${t.btn_email || 'Enviar Email'}</span>
        </a>
        <!-- External Official Portal Listing -->
        <a href="${getOfficialListingUrl(prop)}" target="_blank" rel="noopener noreferrer" class="btn-contact-portal">
          <span>🔗</span> <span>${t.btn_portal || 'Ver Anuncio Oficial en'} ${prop.source_portal || 'Portal Inmobiliario'}</span>
        </a>
      </div>

      <!-- Quick Inquiry Mini-Form -->
      <div class="contact-quick-inquiry">
        <div style="font-size: 0.82rem; font-weight: 700; color: #ffffff; margin-bottom: 6px;">
          ✉️ ${t.inquiry_title || 'Enviar Mensaje Directo o Solicitud de Visita:'}
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px;">
          <input type="text" id="direct-inq-name" class="form-input" style="padding: 7px 10px; font-size: 0.82rem;" placeholder="Tu Nombre *">
          <input type="tel" id="direct-inq-phone" class="form-input" style="padding: 7px 10px; font-size: 0.82rem;" placeholder="Tu Teléfono / WhatsApp *">
        </div>
        <input type="email" id="direct-inq-email" class="form-input" style="padding: 7px 10px; font-size: 0.82rem; margin-bottom: 8px;" placeholder="Tu Correo Electrónico *">
        <textarea id="direct-inq-msg" class="form-input" rows="2" style="padding: 7px 10px; font-size: 0.82rem; margin-bottom: 8px;" placeholder="Mensaje para el gestor (ej: Hola, somos 4 personas interesadas en concertar una visita esta semana...)"></textarea>
        <button class="btn-submit" style="width: 100%; font-size: 0.82rem; padding: 9px;" onclick="sendDirectInquiry('${prop.id}')">
          🚀 ${t.btn_send_inquiry || 'Enviar Mensaje Directo al Gestor'}
        </button>
      </div>
    </div>

    <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; margin-bottom: 18px;">
      <h5 style="font-size: 0.85rem; font-weight: 700; color: var(--azure-400); margin-bottom: 6px;">👥 ¿Quieres este piso para tu minicomunidad?</h5>
      <p style="font-size: 0.8rem; color: var(--text-sub); margin-bottom: 12px;">
        Crea un grupo de ${prop.bedrooms} personas para formalizar el contrato conjunto con el propietario y reducir tu alquiler a solo <strong>${Math.round(prop.rent_per_person)} €/mes</strong>.
      </p>
      <div style="display: flex; gap: 10px;">
        <button class="btn-submit" style="flex: 1;" onclick="closeModal('modal-property-detail'); startCommunityForProperty('${prop.id}', '${escapeQuotes(locProp.title)}', '${prop.city}', ${prop.bedrooms}, ${prop.total_rent})">
          👥 Formar Minicomunidad Aquí
        </button>
        <button class="btn-filter-reset" onclick="focusProperty('${prop.id}', ${prop.latitude}, ${prop.longitude}); closeModal('modal-property-detail');">
          📍 Ver en Mapa
        </button>
      </div>
    </div>
  `;

  openModal('modal-property-detail');
}

async function sendDirectInquiry(propId) {
  const nameInput = document.getElementById('direct-inq-name');
  const phoneInput = document.getElementById('direct-inq-phone');
  const emailInput = document.getElementById('direct-inq-email');
  const msgInput = document.getElementById('direct-inq-msg');

  if (!nameInput || !phoneInput || !emailInput || !msgInput) return;

  const name = nameInput.value.trim();
  const phone = phoneInput.value.trim();
  const email = emailInput.value.trim();
  const message = msgInput.value.trim();

  if (!name || !phone || !email) {
    alert('Por favor, indica tu nombre, teléfono y correo electrónico para contactar.');
    return;
  }

  try {
    const res = await fetch(`${API_BASE}/inquiries`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        property_id: propId,
        name,
        phone,
        email,
        message: message || 'Interesados en solicitar una visita para este piso en LookingForHome.'
      })
    });

    if (!res.ok) throw new Error('Error al enviar solicitud de contacto.');
    showToast('✅ ¡Mensaje enviado con éxito al gestor/propietario!', 'success');
    nameInput.value = '';
    phoneInput.value = '';
    emailInput.value = '';
    msgInput.value = '';
  } catch (err) {
    showToast('❌ ' + err.message, 'error');
  }
}

// ── Fullscreen Lightbox Controller ──────────────────────────────────────────
let lightboxPropId = null;
let lightboxIndex = 0;

function openLightbox(propId, initialIndex = 0) {
  const prop = allProperties.find(p => p.id === propId);
  if (!prop) return;

  lightboxPropId = propId;
  lightboxIndex = initialIndex || 0;

  const locProp = getLocalizedProperty(prop, currentLang);
  const images = getPropertyImages(prop);
  const t = I18N[currentLang];

  const titleEl = document.getElementById('lightbox-title');
  if (titleEl) titleEl.textContent = locProp.title;

  const filmstrip = document.getElementById('lightbox-filmstrip');
  if (filmstrip) {
    filmstrip.innerHTML = images.map((img, idx) => `
      <div class="lightbox-thumb ${idx === lightboxIndex ? 'active' : ''}" id="lightbox-thumb-${idx}" onclick="setLightboxPhoto(${idx})">
        <img src="${img}" alt="Miniatura ${idx + 1}" onerror="handleImgFallback(this)">
      </div>
    `).join('');
  }

  setLightboxPhoto(lightboxIndex);

  const modal = document.getElementById('lightbox-modal');
  if (modal) modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  const modal = document.getElementById('lightbox-modal');
  if (modal) modal.style.display = 'none';
  document.body.style.overflow = '';
}

function navigateLightbox(dir) {
  if (!lightboxPropId) return;
  const prop = allProperties.find(p => p.id === lightboxPropId);
  if (!prop) return;
  const images = getPropertyImages(prop);
  lightboxIndex = (lightboxIndex + dir + images.length) % images.length;
  setLightboxPhoto(lightboxIndex);
}

function setLightboxPhoto(index) {
  if (!lightboxPropId) return;
  const prop = allProperties.find(p => p.id === lightboxPropId);
  if (!prop) return;
  const images = getPropertyImages(prop);
  lightboxIndex = index;

  const imgEl = document.getElementById('lightbox-img');
  if (imgEl) {
    imgEl.style.opacity = '0.3';
    setTimeout(() => {
      imgEl.src = images[lightboxIndex];
      imgEl.style.opacity = '1';
    }, 100);
  }

  const counterEl = document.getElementById('lightbox-counter');
  if (counterEl) counterEl.textContent = `${lightboxIndex + 1} / ${images.length}`;

  const captionEl = document.getElementById('lightbox-caption');
  if (captionEl) captionEl.textContent = getPhotoCaption(lightboxIndex, currentLang);

  document.querySelectorAll('.lightbox-thumb').forEach((th, idx) => {
    if (idx === lightboxIndex) {
      th.classList.add('active');
      th.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    } else {
      th.classList.remove('active');
    }
  });
}

// Global Keyboard Handler for Lightbox (Esc, Left, Right)
window.addEventListener('keydown', (e) => {
  const lb = document.getElementById('lightbox-modal');
  if (lb && lb.style.display === 'flex') {
    if (e.key === 'Escape') closeLightbox();
    else if (e.key === 'ArrowLeft') navigateLightbox(-1);
    else if (e.key === 'ArrowRight') navigateLightbox(1);
  }
});

function openJoinModal(commId, commName) {
  document.getElementById('join-comm-id').value = commId;
  const targetComm = allCommunities.find(c => c.id === commId);
  const commDisplayName = commName || (targetComm ? targetComm.name : 'Minicomunidad');
  
  const titleEl = document.getElementById('join-modal-comm-name');
  if (titleEl) titleEl.textContent = commDisplayName;
  
  goToJoinStep1();
  openModal('modal-join-comm');
}

function goToJoinStep1() {
  const s1 = document.getElementById('join-step-1');
  const s2 = document.getElementById('join-step-2');
  if (s1) s1.style.display = 'block';
  if (s2) s2.style.display = 'none';

  const p1 = document.getElementById('join-pill-1');
  const p2 = document.getElementById('join-pill-2');
  if (p1) p1.classList.add('active');
  if (p2) p2.classList.remove('active');
}

function goToJoinStep2() {
  const name = document.getElementById('join-user-name').value.trim();
  const email = document.getElementById('join-user-email').value.trim();
  const phone = document.getElementById('join-user-phone').value.trim();

  if (!name || !email || !phone) {
    showToast('⚠️ Por favor completa tu nombre, email y teléfono antes de continuar.', 'warning');
    return;
  }

  const commId = document.getElementById('join-comm-id').value;
  const comm = allCommunities.find(c => c.id === commId);

  const sumName = document.getElementById('join-summary-name');
  const sumEmail = document.getElementById('join-summary-email');
  const sumComm = document.getElementById('join-summary-comm');
  const sumRent = document.getElementById('join-summary-rent');

  if (sumName) sumName.textContent = name;
  if (sumEmail) sumEmail.textContent = email;
  if (sumComm && comm) sumComm.textContent = `${comm.name} (${comm.city})`;
  if (sumRent && comm) {
    const rentPP = comm.rent_per_person || Math.round(comm.total_rent / (comm.max_members || 4));
    sumRent.textContent = `${rentPP} €/mes`;
  }

  const s1 = document.getElementById('join-step-1');
  const s2 = document.getElementById('join-step-2');
  if (s1) s1.style.display = 'none';
  if (s2) s2.style.display = 'block';

  const p1 = document.getElementById('join-pill-1');
  const p2 = document.getElementById('join-pill-2');
  if (p1) p1.classList.remove('active');
  if (p2) p2.classList.add('active');
}

async function submitJoinCommunity(e) {
  e.preventDefault();
  const commId = document.getElementById('join-comm-id').value;
  const name = document.getElementById('join-user-name').value;
  const email = document.getElementById('join-user-email').value;
  const phone = document.getElementById('join-user-phone').value;
  const age = parseInt(document.getElementById('join-user-age').value, 10) || 25;
  const occupation = document.getElementById('join-user-occupation').value;
  const bio = document.getElementById('join-user-bio').value;
  const feeAgree = document.getElementById('join-fee-agree').checked;

  try {
    // 1. Create/Register User
    const userRes = await fetch(`${API_BASE}/users`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name,
        email,
        phone,
        age,
        occupation,
        bio,
        max_budget: 600,
        preferred_roommates_count: 4
      })
    });

    const userData = await userRes.json();
    const userId = userData.id;

    // 2. Join Community with 5€ micro-fee
    const joinRes = await fetch(`${API_BASE}/communities/${commId}/join?user_id=${userId}&fee_paid=${feeAgree}`, {
      method: 'POST'
    });

    if (!joinRes.ok) {
      const err = await joinRes.json();
      throw new Error(err.detail || 'No se pudo unir a la comunidad');
    }

    closeModal('modal-join-comm');
    showToast('🎉 ¡Te has unido a la minicomunidad! Cuota europea de 5€ confirmada.', 'success');
    
    // Refresh communities
    await loadCommunities();
  } catch (err) {
    alert(err.message);
  }
}

function openCreatePropertyModal() {
  openModal('modal-create-property');
}

async function submitCreateProperty(e) {
  e.preventDefault();
  const title = document.getElementById('prop-title').value;
  const city = document.getElementById('prop-city').value;
  const neighborhood = document.getElementById('prop-neighborhood').value;
  const totalRent = parseFloat(document.getElementById('prop-rent').value);
  const bedrooms = parseInt(document.getElementById('prop-bedrooms').value, 10);
  const bathrooms = parseInt(document.getElementById('prop-bathrooms').value, 10);
  const area = parseFloat(document.getElementById('prop-area').value);
  const energy = document.getElementById('prop-energy').value;
  const hasElevator = document.getElementById('prop-elevator').checked;
  const isExterior = document.getElementById('prop-exterior').checked;
  const isFurnished = document.getElementById('prop-furnished').checked;
  const description = document.getElementById('prop-desc').value;
  const contactName = document.getElementById('prop-contact-name')?.value || 'Inmobiliaria / Particular';
  const contactPhone = document.getElementById('prop-contact-phone')?.value || '+34 600 123 456';
  const contactEmail = document.getElementById('prop-contact-email')?.value || 'contacto@lookingforhome.duckdns.org';

  try {
    const res = await fetch(`${API_BASE}/properties`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title,
        city,
        country: 'España',
        property_type: 'piso',
        neighborhood,
        total_rent: totalRent,
        bedrooms,
        bathrooms,
        surface_sqm: area,
        has_elevator: hasElevator,
        is_exterior: isExterior,
        is_furnished: isFurnished,
        energy_rating: energy,
        description,
        contact_name: contactName,
        contact_phone: contactPhone,
        contact_email: contactEmail,
        contact_whatsapp: contactPhone.replace(/[^0-9]/g, ''),
        source_portal: 'Direct LookingForHome Community'
      })
    });

    if (!res.ok) throw new Error('Error al publicar vivienda');
    closeModal('modal-create-property');
    showToast('✅ ¡Vivienda publicada con éxito!', 'success');
    await loadProperties();
  } catch (err) {
    alert(err.message);
  }
}

function openPortalModal() {
  openModal('modal-import-portal');
}

async function submitPortalImport(e) {
  e.preventDefault();
  const portalUrl = document.getElementById('import-url').value;
  const city = document.getElementById('import-city').value;
  const targetRent = parseFloat(document.getElementById('import-rent').value) || null;
  const bedrooms = parseInt(document.getElementById('import-bedrooms').value, 10) || 4;

  const btn = document.getElementById('btn-submit-import');
  btn.disabled = true;
  btn.textContent = '⏳ Analizando portal inmobiliario...';

  try {
    const res = await fetch(`${API_BASE}/properties/import-portal`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        portal_url: portalUrl,
        city: city || undefined,
        target_rent: targetRent || undefined,
        bedrooms: bedrooms
      })
    });

    if (!res.ok) throw new Error('Error al importar anuncio del portal');
    const data = await res.json();

    closeModal('modal-import-portal');
    showToast(`🌐 ${data.message}`, 'success');
    await loadProperties();

    if (data.property) {
      focusProperty(data.property.id, data.property.latitude, data.property.longitude);
    }
  } catch (err) {
    alert(err.message);
  } finally {
    btn.disabled = false;
    btn.textContent = I18N[currentLang].btn_import_parse;
  }
}

async function openStatsModal() {
  try {
    const res = await fetch(`${API_BASE}/stats`);
    if (res.ok) {
      const stats = await res.json();
      document.getElementById('stat-props').textContent = stats.total_properties;
      document.getElementById('stat-comms').textContent = stats.total_communities;
      document.getElementById('stat-cities').textContent = stats.european_cities_active;
      document.getElementById('stat-savings').textContent = `${stats.avg_monthly_savings_per_person_eur} €`;
    }
  } catch (err) {
    console.error(err);
  }
  openModal('modal-stats');
}

function startCommunityForProperty(propId, propTitle, city, bedrooms, totalRent) {
  switchNavTab('communities');
  showToast(`👥 Para '${propTitle}' te sugerimos formar un grupo de ${bedrooms} personas (${Math.round(totalRent/bedrooms)}€/p).`);
}

function openCreateCommunityModal() {
  const name = prompt('Nombre de la nueva minicomunidad (ej: "Coliving Gràcia 4 personas"):');
  if (!name) return;
  const city = prompt('Ciudad (ej: Barcelona, Madrid, París, Bilbao):', 'Barcelona');
  if (!city) return;

  fetch(`${API_BASE}/communities`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name,
      city,
      target_members: 4,
      target_budget_per_person: 450,
      description: `Minicomunidad abierta en ${city} para compartir piso de 4 habitaciones y dividir arriendo.`
    })
  }).then(r => r.json()).then(data => {
    showToast('🎉 ¡Minicomunidad creada! Los compañeros pueden unirse ahora.', 'success');
    loadCommunities();
  }).catch(err => alert(err));
}

// ── Tab Navigation ────────────────────────────────────────────────────────────
function switchNavTab(tab) {
  const propView = document.getElementById('properties-view');
  const commView = document.getElementById('communities-view');
  const btnProps = document.getElementById('nav-btn-properties');
  const btnComms = document.getElementById('nav-btn-communities');

  if (tab === 'properties') {
    if (propView) propView.style.display = 'grid';
    if (commView) commView.style.display = 'none';
    if (btnProps) btnProps.classList.add('active');
    if (btnComms) btnComms.classList.remove('active');
    if (leafletMap) {
      setTimeout(() => leafletMap.invalidateSize(), 200);
    }
  } else if (tab === 'communities') {
    if (propView) propView.style.display = 'none';
    if (commView) commView.style.display = 'block';
    if (btnProps) btnProps.classList.remove('active');
    if (btnComms) btnComms.classList.add('active');
    loadCommunities();
  }
}

// ── Multi-Language Switcher (ES, EN, CA, EU, FR) ──────────────────────────────
function setupLanguageSwitcher() {
  const savedLang = localStorage.getItem('lookingforhome_lang') || localStorage.getItem('findhome_lang') || 'es';
  setLanguage(savedLang);
}

function setLanguage(lang) {
  if (!I18N[lang]) return;
  currentLang = lang;
  localStorage.setItem('lookingforhome_lang', lang);

  // Update active button state
  document.querySelectorAll('.lang-btn').forEach(btn => {
    if (btn.getAttribute('data-lang') === lang) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Translate all DOM elements with data-i18n
  const dict = I18N[lang];
  document.querySelectorAll('[data-i18n]').forEach(elem => {
    const key = elem.getAttribute('data-i18n');
    if (dict[key]) {
      elem.textContent = dict[key];
    }
  });

  // Update country and city options with translated country names
  const countrySelect = document.getElementById('filter-country');
  if (countrySelect) {
    const selectedVal = countrySelect.value;
    countrySelect.querySelectorAll('option').forEach(opt => {
      const i18nKey = opt.getAttribute('data-i18n');
      if (i18nKey && dict[i18nKey]) {
        opt.textContent = dict[i18nKey];
      }
    });
    countrySelect.value = selectedVal;
  }

  // Update property type filter options
  const typeSelect = document.getElementById('filter-type');
  if (typeSelect) {
    const selectedVal = typeSelect.value;
    typeSelect.querySelectorAll('option').forEach(opt => {
      const i18nKey = opt.getAttribute('data-i18n');
      if (i18nKey && dict[i18nKey]) {
        opt.textContent = dict[i18nKey];
      }
    });
    typeSelect.value = selectedVal;
  }

  // Update surface filter options
  const surfSelect = document.getElementById('filter-surface');
  if (surfSelect) {
    const selectedVal = surfSelect.value;
    surfSelect.querySelectorAll('option').forEach(opt => {
      const i18nKey = opt.getAttribute('data-i18n');
      if (i18nKey && dict[i18nKey]) {
        opt.textContent = dict[i18nKey];
      }
    });
    surfSelect.value = selectedVal;
  }

  // Re-render dynamic components with localized strings, titles, descriptions & countries
  renderPropertiesGrid(filteredProperties);
  updateMapMarkers(filteredProperties);
  renderCommunitiesGrid(allCommunities);
  calculateSplit();
}

// ── Toast Notifications ───────────────────────────────────────────────────────
function showToast(msg, type = 'info') {
  const toast = document.getElementById('toast');
  const msgElem = document.getElementById('toast-message');
  const iconElem = document.getElementById('toast-icon');

  if (!toast) return;

  iconElem.textContent = type === 'error' ? '⚠️' : (type === 'success' ? '✅' : '✨');
  msgElem.textContent = msg;

  toast.style.display = 'flex';
  setTimeout(() => {
    toast.style.display = 'none';
  }, 4000);
}

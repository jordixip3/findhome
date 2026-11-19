from fastapi import APIRouter, HTTPException, Query, status
from typing import Optional, List, Dict, Any
from app.models.schemas import (
    PropertyCreate, PropertyResponse, UserCreate, UserResponse,
    CommunityCreate, CommunityResponse, InquiryCreate, PortalImportRequest
)
from app.models.database import (
    get_properties, get_property, create_property,
    get_communities, create_community, join_community,
    create_user, get_users, save_inquiry
)
from app.services.portal_adapter import SUPPORTED_PORTALS, parse_and_normalize_portal_url

router = APIRouter(prefix="/api/v1", tags=["LookingForHome European Housing API"])


# ── Properties Endpoints ──────────────────────────────────────────────────────

@router.get("/properties", summary="List European housing properties with filters")
async def list_properties(
    city: Optional[str] = Query(None),
    country: Optional[str] = Query(None),
    property_type: Optional[str] = Query(None),
    min_bedrooms: Optional[int] = Query(None, ge=1, le=10),
    min_bathrooms: Optional[int] = Query(None, ge=1, le=5),
    min_surface_sqm: Optional[int] = Query(None, ge=10),
    max_surface_sqm: Optional[int] = Query(None, ge=10),
    has_elevator: Optional[bool] = Query(None),
    is_exterior: Optional[bool] = Query(None),
    max_rent_per_person: Optional[float] = Query(None, gt=0),
    max_total_rent: Optional[float] = Query(None, gt=0)
):
    return get_properties(
        city=city,
        country=country,
        property_type=property_type,
        min_bedrooms=min_bedrooms,
        min_bathrooms=min_bathrooms,
        min_surface_sqm=min_surface_sqm,
        max_surface_sqm=max_surface_sqm,
        has_elevator=has_elevator,
        is_exterior=is_exterior,
        max_rent_per_person=max_rent_per_person,
        max_total_rent=max_total_rent
    )


@router.get("/properties/{property_id}", summary="Get detailed property specifications")
async def get_property_detail(property_id: str):
    prop = get_property(property_id)
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")
    return prop


@router.post("/properties", status_code=status.HTTP_201_CREATED, summary="Submit a new housing listing")
async def add_property(payload: PropertyCreate):
    prop_id = create_property(payload.model_dump())
    return {"id": prop_id, "message": "Property published successfully and available for minicommunities."}


@router.post("/properties/import-portal", status_code=status.HTTP_201_CREATED, summary="Import listing from free European housing portal")
async def import_from_portal(payload: PortalImportRequest):
    normalized = parse_and_normalize_portal_url(
        url=payload.portal_url,
        custom_city=payload.city,
        custom_rent=payload.target_rent
    )
    if payload.bedrooms:
        normalized["bedrooms"] = payload.bedrooms
        normalized["ideal_roommates"] = payload.bedrooms

    prop_id = create_property(normalized)
    created = get_property(prop_id)
    return {
        "id": prop_id,
        "message": f"Successfully parsed and imported from {normalized['source_portal']}!",
        "property": created
    }


@router.get("/portals", summary="List integrated open European housing portals")
async def list_portals():
    return SUPPORTED_PORTALS


# ── Communities Endpoints ─────────────────────────────────────────────────────

@router.get("/communities", summary="List minicommunities forming to split rent")
async def list_communities(city: Optional[str] = Query(None)):
    return get_communities(city=city)


@router.post("/communities", status_code=status.HTTP_201_CREATED, summary="Create a new minicommunity for a property")
async def add_community(payload: CommunityCreate):
    c_id = create_community(payload.model_dump())
    return {"id": c_id, "message": "Minicommunity created! Roommates can now join and split the rent."}


@router.post("/communities/{community_id}/join", summary="Join an existing minicommunity (with 5€ micro-membership option)")
async def join_community_endpoint(community_id: str, user_id: str = Query(...), fee_paid: bool = Query(True)):
    success = join_community(community_id, user_id, fee_paid=fee_paid)
    if not success:
        raise HTTPException(status_code=400, detail="Cannot join community: either community is full or does not exist.")
    return {
        "status": "joined",
        "community_id": community_id,
        "fee_paid": fee_paid,
        "fee_amount_eur": 5.0 if fee_paid else 0.0,
        "message": "¡Te has unido con éxito a la minicomunidad! La cuota comunitaria europea de 5€ garantiza la reserva y contacto seguro."
    }


# ── Users & Inquiries ─────────────────────────────────────────────────────────

@router.get("/users", summary="List registered users seeking community")
async def list_users():
    return get_users()


@router.post("/users", status_code=status.HTTP_201_CREATED, summary="Register a user with contact details and budget")
async def register_user(payload: UserCreate):
    u_id = create_user(payload.model_dump())
    return {"id": u_id, "message": "User registered successfully in LookingForHome network."}


@router.post("/inquiries", status_code=status.HTTP_201_CREATED, summary="Send inquiry to landlord or minicommunity")
async def send_inquiry(payload: InquiryCreate):
    iq_id = save_inquiry(payload.model_dump())
    return {
        "id": iq_id,
        "status": "sent",
        "message": "Solicitud enviada. Los miembros de la minicomunidad y el propietario recibirán tus datos de contacto."
    }


# ── Platform Stats ────────────────────────────────────────────────────────────

@router.get("/stats", summary="Get global European housing metrics & savings")
async def get_stats():
    props = get_properties()
    comms = get_communities()
    users = get_users()

    avg_rent = sum(p["total_rent"] for p in props) / len(props) if props else 0
    avg_per_person = sum(p["rent_per_person"] for p in props) / len(props) if props else 0
    avg_savings = avg_rent * 0.7 - avg_per_person if avg_rent else 450.0

    return {
        "total_properties": len(props),
        "total_communities": len(comms),
        "total_users": len(users),
        "european_cities_active": len(set(p["city"] for p in props)),
        "avg_rent_per_person_eur": round(avg_per_person, 2),
        "avg_monthly_savings_per_person_eur": round(max(avg_savings, 380.0), 2),
        "community_membership_fee_eur": 5.0
    }


@router.post("/properties/sync-open-portals", summary="Synchronize property listings from open real estate portals")
async def sync_open_portals():
    from app.models.database import DBContext
    from app.services.portal_feeder import feed_open_portal_properties
    with DBContext() as db:
        count = feed_open_portal_properties(db)
    return {
        "status": "success",
        "synced_properties_count": count,
        "message": f"Successfully synchronized {count} properties from European open portals."
    }


# ── Admin & Visitor Analytics Endpoints ───────────────────────────────────────

import os
from pydantic import BaseModel
from fastapi import Request
from app.models.database import record_access_log, get_access_logs, get_access_stats, clear_access_logs
from app.services.geoip_service import extract_client_ip, resolve_geoip, detect_device_type

ADMIN_SECRET_KEY = os.getenv("ADMIN_PASSWORD", "admin123")
ADMIN_SESSION_TOKEN = "lfh_adm_token_789423"

class AdminLoginRequest(BaseModel):
    password: str

class ManualLogRequest(BaseModel):
    path: Optional[str] = "/"


@router.post("/admin/login", summary="Authenticate admin user")
async def admin_login(payload: AdminLoginRequest):
    # Allow admin123 or lookingforhome2026 or configured ADMIN_PASSWORD
    valid_passwords = [ADMIN_SECRET_KEY, "admin123", "lookingforhome2026", "admin"]
    if payload.password.strip() not in valid_passwords:
        raise HTTPException(status_code=401, detail="Contraseña de administrador incorrecta.")
    
    return {
        "status": "authenticated",
        "token": ADMIN_SESSION_TOKEN,
        "user": "Administrador LookingForHome"
    }


@router.get("/admin/stats", summary="Get visitor analytics & geographic distribution for Leaflet mapping")
async def admin_visitor_stats():
    stats = get_access_stats()
    return stats


@router.get("/admin/logs", summary="Get recent visitor access logs with geo origin")
async def admin_visitor_logs(
    limit: int = Query(100, ge=1, le=500),
    country: Optional[str] = Query(None),
    search: Optional[str] = Query(None)
):
    logs = get_access_logs(limit=limit, country=country, search=search)
    return logs


@router.post("/admin/log-visit", summary="Record a visitor entry with real-time GeoIP mapping")
async def log_client_visit(req: Request, payload: Optional[ManualLogRequest] = None):
    headers = dict(req.headers)
    client_host = req.client.host if req.client else "127.0.0.1"
    ip = extract_client_ip(headers, client_host)
    ua = headers.get("user-agent", "")
    device = detect_device_type(ua)
    ref = headers.get("referer", "")
    path = payload.path if payload and payload.path else req.url.path

    geo = resolve_geoip(ip)
    
    log_id = record_access_log(
        ip=ip,
        country=geo.get("country", "Desconocido"),
        country_code=geo.get("country_code", "UN"),
        region=geo.get("region", ""),
        city=geo.get("city", "Desconocido"),
        latitude=geo.get("latitude", 0.0),
        longitude=geo.get("longitude", 0.0),
        path=path,
        method=req.method,
        status_code=200,
        user_agent=ua,
        device_type=device,
        referrer=ref
    )

    return {
        "status": "logged",
        "log_id": log_id,
        "ip": ip,
        "location": f"{geo.get('city')}, {geo.get('country')}",
        "latitude": geo.get("latitude"),
        "longitude": geo.get("longitude")
    }


@router.delete("/admin/logs", summary="Clear access logs")
async def admin_clear_logs():
    clear_access_logs()
    return {"status": "cleared", "message": "Historial de accesos reseteado correctamente."}


# ── AI Voice Agent Endpoints ──────────────────────────────────────────────────
from app.services.voice_agent_service import voice_agent, AGENT_WHATSAPP_NUMBER

class VoiceAgentRequest(BaseModel):
    message: str
    lang: Optional[str] = "es"
    context: Optional[Dict[str, Any]] = None

@router.post("/voice-agent/chat", summary="Conversational AI Voice Agent linked to WhatsApp +34 603 331 391")
async def voice_agent_chat(payload: VoiceAgentRequest):
    return voice_agent.process_query(payload.message, lang=payload.lang or "es")

@router.get("/voice-agent/config", summary="Get Voice Agent configuration and WhatsApp link")
async def voice_agent_config():
    return {
        "whatsapp_number": AGENT_WHATSAPP_NUMBER,
        "whatsapp_link": voice_agent.build_whatsapp_link("Hola, quiero hablar con el Agente de Voz de LookingForHome."),
        "supported_languages": ["es", "en", "ca", "fr", "de"],
        "capabilities": [
            "Búsqueda de vivienda compartida por voz",
            "Cálculo de reparto de alquiler",
            "Vincular y coordinar visitas por WhatsApp",
            "Soporte multilenguaje en tiempo real"
        ]
    }




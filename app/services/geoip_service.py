"""
LookingForHome — GeoIP & Visitor Analytics Service
Extracts real visitor IP addresses, performs fast geolocation lookups (with in-memory cache),
and categorizes client devices and browsers.
"""
import urllib.request
import json
import re
from datetime import datetime, timezone
from typing import Dict, Any, Optional

# In-memory GeoIP cache to avoid repeated network lookups for frequent visitor IPs
IP_GEO_CACHE: Dict[str, Dict[str, Any]] = {}

# Known fallback coordinates for local development / internal networks
LOCAL_FALLBACK = {
    "country": "España",
    "country_code": "ES",
    "region": "Comunidad de Madrid",
    "city": "Madrid (Local Dev)",
    "latitude": 40.4168,
    "longitude": -3.7038
}

COUNTRY_COORDINATES = {
    "ES": (40.4637, -3.7492, "España"),
    "FR": (46.2276, 2.2137, "Francia"),
    "DE": (51.1657, 10.4515, "Alemania"),
    "IT": (41.8719, 12.5674, "Italia"),
    "PT": (39.3999, -8.2245, "Portugal"),
    "NL": (52.1326, 5.2913, "Países Bajos"),
    "IE": (53.1424, -7.6921, "Irlanda"),
    "GB": (55.3781, -3.4360, "Reino Unido"),
    "US": (37.0902, -95.7129, "Estados Unidos"),
    "MX": (23.6345, -102.5528, "México"),
    "AR": (-38.4161, -63.6167, "Argentina"),
    "CO": (4.5709, -74.2973, "Colombia"),
    "CL": (-35.6751, -71.5430, "Chile"),
    "JP": (36.2048, 138.2529, "Japón"),
    "BR": (-14.2350, -51.9253, "Brasil"),
    "CH": (46.8182, 8.2275, "Suiza"),
    "BE": (50.5039, 4.4699, "Bélgica"),
    "AT": (47.5162, 14.5501, "Austria"),
    "SE": (60.1282, 18.6435, "Suecia"),
    "NO": (60.4720, 8.4689, "Noruega")
}

def extract_client_ip(headers: Dict[str, str], client_host: Optional[str]) -> str:
    """
    Extracts the true client IP from reverse proxy headers (Nginx, Cloudflare, AWS ALB)
    or falls back to the direct socket client host.
    """
    # X-Forwarded-For can contain multiple IPs: "client, proxy1, proxy2"
    xff = headers.get("x-forwarded-for") or headers.get("X-Forwarded-For")
    if xff:
        parts = [p.strip() for p in xff.split(",")]
        for p in parts:
            if p and not is_private_ip(p):
                return p
        if parts:
            return parts[0]

    for h in ["x-real-ip", "X-Real-IP", "cf-connecting-ip", "CF-Connecting-IP"]:
        val = headers.get(h)
        if val and val.strip():
            return val.strip()

    return client_host or "127.0.0.1"


def is_private_ip(ip: str) -> bool:
    """Checks if IP is a loopback or private local network address."""
    if not ip or ip in ("127.0.0.1", "localhost", "::1", "0.0.0.0"):
        return True
    if ip.startswith("192.168.") or ip.startswith("10."):
        return True
    if ip.startswith("172."):
        try:
            second_octet = int(ip.split(".")[1])
            if 16 <= second_octet <= 31:
                return True
        except Exception:
            pass
    return False


def detect_device_type(user_agent: str) -> str:
    """Parses user-agent to determine device category."""
    if not user_agent:
        return "Desktop"
    ua = user_agent.lower()
    if any(bot in ua for bot in ["bot", "spider", "crawler", "googlebot", "bingbot", "curl", "wget", "python-requests"]):
        return "Bot / Crawler"
    if any(m in ua for m in ["ipad", "tablet"]):
        return "Tablet"
    if any(m in ua for m in ["mobile", "android", "iphone", "ipod", "windows phone"]):
        return "Mobile"
    return "Desktop"


def resolve_geoip(ip: str) -> Dict[str, Any]:
    """
    Resolves geographic location (country, city, lat, lon) for an IP address.
    Uses memory cache, public IP-API lookup, or graceful local fallbacks.
    """
    clean_ip = ip.strip() if ip else "127.0.0.1"

    if clean_ip in IP_GEO_CACHE:
        return IP_GEO_CACHE[clean_ip]

    if is_private_ip(clean_ip):
        res = {
            "ip": clean_ip,
            "country": LOCAL_FALLBACK["country"],
            "country_code": LOCAL_FALLBACK["country_code"],
            "region": LOCAL_FALLBACK["region"],
            "city": LOCAL_FALLBACK["city"],
            "latitude": LOCAL_FALLBACK["latitude"],
            "longitude": LOCAL_FALLBACK["longitude"],
            "is_local": True
        }
        IP_GEO_CACHE[clean_ip] = res
        return res

    # Public IP lookup via ip-api.com
    try:
        url = f"http://ip-api.com/json/{clean_ip}?fields=status,country,countryCode,regionName,city,lat,lon,query"
        req = urllib.request.Request(url, headers={"User-Agent": "LookingForHome/1.0"})
        with urllib.request.urlopen(req, timeout=1.8) as response:
            data = json.loads(response.read().decode("utf-8"))
            if data.get("status") == "success":
                res = {
                    "ip": clean_ip,
                    "country": data.get("country") or "Desconocido",
                    "country_code": data.get("countryCode") or "UN",
                    "region": data.get("regionName") or "",
                    "city": data.get("city") or "Desconocido",
                    "latitude": float(data.get("lat") or 40.4168),
                    "longitude": float(data.get("lon") or -3.7038),
                    "is_local": False
                }
                IP_GEO_CACHE[clean_ip] = res
                return res
    except Exception:
        pass

    # Fallback default
    res = {
        "ip": clean_ip,
        "country": "España",
        "country_code": "ES",
        "region": "Madrid",
        "city": "Madrid (Resolución Automática)",
        "latitude": 40.4168,
        "longitude": -3.7038,
        "is_local": False
    }
    IP_GEO_CACHE[clean_ip] = res
    return res

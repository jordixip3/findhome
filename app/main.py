import os
import sys
import asyncio

if sys.platform == "darwin":
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.models.database import init_db
from app.routers import api

init_db()

app = FastAPI(
    title="LookingForHome — European Shared Housing & Rent-Dividing Platform",
    description="Plataforma europea de vivienda digna y asequible mediante minicomunidades (3-5 personas) y reparto de arriendo.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def visitor_tracking_middleware(request, call_next):
    response = await call_next(request)

    path = request.url.path
    # Ignore static files to avoid cluttering logs
    if not any(path.endswith(ext) for ext in [".css", ".js", ".jpg", ".png", ".jpeg", ".ico", ".svg", ".woff", ".woff2", ".map"]) and not path.startswith("/static"):
        try:
            from app.services.geoip_service import extract_client_ip, resolve_geoip, detect_device_type
            from app.models.database import record_access_log
            
            headers = dict(request.headers)
            client_host = request.client.host if request.client else "127.0.0.1"
            ip = extract_client_ip(headers, client_host)
            ua = headers.get("user-agent", "")
            dev = detect_device_type(ua)
            geo = resolve_geoip(ip)

            record_access_log(
                ip=ip,
                country=geo.get("country", "Desconocido"),
                country_code=geo.get("country_code", "UN"),
                region=geo.get("region", ""),
                city=geo.get("city", "Desconocido"),
                latitude=geo.get("latitude", 0.0),
                longitude=geo.get("longitude", 0.0),
                path=path,
                method=request.method,
                status_code=response.status_code,
                user_agent=ua,
                device_type=dev,
                referrer=headers.get("referer", "")
            )
        except Exception:
            pass

    return response


app.include_router(api.router)

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", include_in_schema=False)
@app.get("/lookingforhome", include_in_schema=False)
@app.get("/lookingforhome/", include_in_schema=False)
@app.get("/findhome", include_in_schema=False)
@app.get("/findhome/", include_in_schema=False)
async def serve_home():
    idx = os.path.join(static_dir, "index.html")
    if os.path.exists(idx):
        return FileResponse(
            idx,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return {"message": "LookingForHome API operational. Visit /docs for OpenAPI specs."}


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

app.include_router(api.router)

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", include_in_schema=False)
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

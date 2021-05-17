import os
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import templates, newsletter
from grapesjs import editor

import config
import data

from constants import API_TAGS_METADATA

config.parse_args()
app = FastAPI(
    title="Grapesjs API",
    description="Simple API for grapesjs and grapesjs-template-manager",
    version="1.0.0",
    openapi_tags=API_TAGS_METADATA,
)

try:
    origins = os.getenv("FRONTEND_URLS").split(",")
except:
    origins = ["http://localhost:3000", "http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="api/static"), name="static")

app.include_router(templates.router)
app.include_router(newsletter.router)
app.include_router(editor.router)


@app.get("/", include_in_schema=False)
async def root():
    return {
        "docs": "api documentation at /docs or /redoc",
        "editor": "newsletter editor at /editor",
    }


if __name__ == "__main__":
    data.setup()
    uvicorn.run("main:app", host=config.CONFIG.host, port=int(config.CONFIG.port))

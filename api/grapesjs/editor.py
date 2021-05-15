from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import config

router = APIRouter(prefix="/editor", include_in_schema=False)


templates = Jinja2Templates(directory="api/templates")


@router.get("", response_class=HTMLResponse)
async def get_editor(request: Request):
    return templates.TemplateResponse(
        "editor.html", {"request": request, "pfx": config.CONFIG.prefix}
    )

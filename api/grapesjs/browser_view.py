import data.emails as data

from uuid import UUID
from fastapi import APIRouter, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/viewer", include_in_schema=False)


templates = Jinja2Templates(directory="api/templates")


@router.get("/{uuid}", response_class=HTMLResponse)
async def get_viewer(
    request: Request, uuid: UUID = Path(..., description="Campaign ID")
):
    campaign = data.get_campaign(uuid)
    return templates.TemplateResponse(
        "browser_view.html",
        {"request": request, "subject": campaign["subject"], "body": campaign["body"]},
    )

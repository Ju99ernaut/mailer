import data.emails as data

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/archive", include_in_schema=False)


templates = Jinja2Templates(directory="api/templates")


@router.get("", response_class=HTMLResponse)
async def get_archive(request: Request):
    campaigns = [campaign for campaign in data.get_all_campaigns_unpaginated()]
    return templates.TemplateResponse(
        "archive.html", {"request": request, "campaigns": campaigns}
    )

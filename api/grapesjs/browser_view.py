import data

from fastapi import APIRouter, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/viewer", include_in_schema=False)


templates = Jinja2Templates(directory="api/templates")


@router.get("/{id}", response_class=HTMLResponse)
async def get_viewer(request: Request, id: int = Path(..., description="Campaign ID")):
    campaign = data.get_campaign(id)
    return templates.TemplateResponse(
        "browser_view.html", {"request": request, "campaign": campaign}
    )

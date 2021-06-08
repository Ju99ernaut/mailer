from enum import Enum
from fastapi import APIRouter, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/edit", include_in_schema=False)


class Action(str, Enum):
    subscribe = "subscribe"
    unsubscribe = "unsubscribe"


templates = Jinja2Templates(directory="api/templates")


@router.get("/{action}", response_class=HTMLResponse)
async def get_editor(
    request: Request, action: Action = Path(..., description="Action Type")
):
    return templates.TemplateResponse(
        "edit.html", {"request": request, "action": action}
    )

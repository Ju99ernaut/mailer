import data

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/dashboard", include_in_schema=False)


templates = Jinja2Templates(directory="api/templates")


@router.get("", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    campaign_config = data.get_campaign_config_default()
    campaigns = data.get_all_campaigns_unpaginated()
    subscribers = data.get_all_emails_unpaginated()
    uppy_config = data.get_uppy_config()
    total_campaigns = data.get_campaign_count()
    default_template = data.get_default_template()
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": {"username": "username"},
            "campaign_config": campaign_config,
            "campaigns": [campaign for campaign in campaigns],
            "subscribers": [subscriber for subscriber in subscribers],
            "uppy_config": uppy_config,
            "total_campaigns": total_campaigns,
            "default_template": default_template,
        },
    )

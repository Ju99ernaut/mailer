"""
 Constants useful for data module
"""

TEMPLATES_TABLE = "templates"
ASSETS_TABLE = "assets"
EMAILS_TABLE = "emails"
UPPY_TABLE = "uppy"
CAMPAIGNS_TABLE = "campaigns"
CONFIG_TABLE = "config"

ASSETS_KEY = "assets"
IDX_KEY = "idx"
UUID_KEY = "uuid"
TEMPLATE_KEY = "template"
THUMBNAIL_KEY = "thumbnail"
HTML_KEY = "html"
CSS_KEY = "css"
COMPONENTS_KEY = "components"
STYLES_KEY = "styles"
URL_KEY = "url"
EMAIL_KEY = "email"
UPDATED_KEY = "updated_at"
SUBSCRIBED_KEY = "subscribed_at"

API_TAGS_METADATA = [
    {"name": "templates", "description": "Grapesjs templates"},
    {"name": "assets", "description": "Store/Load references to assets"},
    {"name": "newsletter", "description": "Subscribe and unsubscribe to newsletter"},
    {"name": "subscribers", "description": "View and edit mailing list"},
    {"name": "campaigns", "description": "View previously sent newsletters"},
]

GJS_PREFIX = "gjs-"

import os


"""
 Constants useful for data module
"""

USERS_TABLE = "users"
TEMPLATES_TABLE = "templates"
ASSETS_TABLE = "assets"
EMAILS_TABLE = "emails"
UPPY_TABLE = "uppy"
CAMPAIGNS_TABLE = "campaigns"
CONFIG_TABLE = "config"

USERNAME_KEY = "username"
EMAIL_KEY = "email"
PASSWORD_KEY = "password"
DISABLED_KEY = "disabled"
JOINED_KEY = "joined"
ACTIVE_KEY = "active"
ROLE_KEY = "role"

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

"""
 Constants useful for API docs module
"""
API_TAGS_METADATA = [
    {"name": "users", "description": "User data"},
    {"name": "templates", "description": "Grapesjs templates"},
    {"name": "assets", "description": "Store/Load references to assets"},
    {"name": "newsletter", "description": "Subscribe and unsubscribe to newsletter"},
    {"name": "subscribers", "description": "View and edit mailing list"},
    {"name": "campaigns", "description": "View previously sent newsletters"},
]

GJS_PREFIX = "gjs-"

"""
 Constants useful for users module
"""
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = (
    os.getenv("SECRET_KEY")
    or "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

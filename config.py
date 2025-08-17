import os
from os import environ

# Bot Configuration
API_ID = int(environ.get("API_ID", "your_api_id"))
API_HASH = environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = environ.get("BOT_TOKEN", "your_bot_token")

# Force Subscribe Channels
AUTH_CHANNEL = [int(ch) if ch.lstrip('-').isdigit() else ch for ch in environ.get('AUTH_CHANNEL', '').split()]

# Web App URL
WEB_APP_URL = environ.get("WEB_APP_URL", "https://your-app.onrender.com")

# Database (optional)
DATABASE_URI = environ.get("DATABASE_URI", "")

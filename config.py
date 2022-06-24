import os
import logging
from os import getenv
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
LOGGER = logging.getLogger(__name__)

if not os.environ.get("ENV"):
    load_dotenv('.env', override=True)

class Config(object):
    try:
        TG_BOT_TOKEN = getenv("TG_BOT_TOKEN")
        APP_ID = int(getenv("APP_ID", 123))
        API_HASH = getenv("API_HASH")
        USER_SESSION = getenv("USER_SESSION")
    except:
        LOGGER.warning("Essential TG Configs are missing")
        exit(1)

    try:
        AUTH_CHAT = set(int(x) for x in getenv("AUTH_CHAT").split())
    except:
        AUTH_CHAT = None

    WORK_DIR = getenv("WORK_DIR", "./bot/")
    DOWNLOADS_FOLDER = getenv("DOWNLOADS_FOLDER", "DOWNLOADS")
    DOWNLOAD_BASE_DIR = WORK_DIR + DOWNLOADS_FOLDER
    
    BOT_USERNAME = getenv("BOT_USERNAME", "")
    if not BOT_USERNAME:
        LOGGER.warning("NO BOT USERNAME FOUND")
        exit(1)

    if BOT_USERNAME.startswith("@"):
        BOT_USERNAME = BOT_USERNAME[1:]        

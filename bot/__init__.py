import logging
from config import Config
from pyrogram import Client

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
LOGGER = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot = Config.BOT_USERNAME

class CMD(object):
    START = ["start", f"start@{bot}"]
    HELP = ["help", f"help@{bot}"]
    UPLOAD = ["upload", f"upload@{bot}"]

"""USER = Client(
    name="PremiumUjer",
    session_string=Config.USER_SESSION,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH
)"""
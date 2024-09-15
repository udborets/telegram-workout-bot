from dotenv import load_dotenv
import os
from logger import logger


load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if BOT_TOKEN is None:
    logger.exception("No BOT_TOKEN provided")
    os._exit(1)
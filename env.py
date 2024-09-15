from dotenv import load_dotenv
import os

from logger import logger


logger.info("Loading environment variables")
dotenv_loaded = load_dotenv()

if not dotenv_loaded:
    logger.exception("No environment variables specified in .env file")
    os._exit(1)
else:
    logger.info(".env loaded")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if BOT_TOKEN is None:
    logger.exception("No BOT_TOKEN environment variable provided")
    os._exit(1)

logger.info("All environment variables loaded successfully")

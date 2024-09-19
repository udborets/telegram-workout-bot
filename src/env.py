from dotenv import load_dotenv
import os

from logger import logger


def get_env_variable(key: str) -> str:
    value = os.environ.get(key)
    if value is None:
        logger.exception("No %s environment variable provided, exiting", key)
        os._exit(1)
    return value


logger.info("Loading environment variables")
dotenv_loaded = load_dotenv()
print(dotenv_loaded)
if not dotenv_loaded:
    logger.exception("No environment variables specified in .env file")
    os._exit(1)
else:
    logger.info(".env loaded")

BOT_TOKEN = get_env_variable("BOT_TOKEN")
POSTGRES_PASSWORD = get_env_variable("POSTGRES_PASSWORD")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

logger.info("All environment variables loaded successfully")

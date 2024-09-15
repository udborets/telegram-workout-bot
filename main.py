import asyncio
from bot import bot

from logger import logger


async def main():
    logger.info("Starting bot polling")
    await bot.polling()


if __name__ == "__main__":
    asyncio.run(main())

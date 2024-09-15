import asyncio
import http
import aiohttp
from bot import bot


async def main():
    await bot.polling()


if __name__ == "__main__":
    asyncio.run(main())
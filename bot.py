from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from env import BOT_TOKEN
from logger import logger


bot = AsyncTeleBot(token=BOT_TOKEN)

commands = {
    "list": {
        
        "description": "",
    },
}

@bot.message_handler(commands=["start"])
async def start(message: Message):
    await bot.send_message(message.chat.id, "Hello World!")
    await bot.send_message(message.chat.id, f"{message.from_user.id}")


##### start of TODO
# send a list of available commands
@bot.message_handler(commands=["help"])
async def commands(message: Message):
    pass


##### end of TODO

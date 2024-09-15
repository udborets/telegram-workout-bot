from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from env import BOT_TOKEN

from logger import logger


bot = AsyncTeleBot(token=BOT_TOKEN)


@bot.message_handler(commands=["start"])
async def start(message: Message):
    await bot.send_message(message.chat.id, "Hello World!")
    

##### start of TODO
# @bot.message_handler(commands=["help"])
# async def help(message: Message):
    # send a list of available commands
    
    
##### end of TODO
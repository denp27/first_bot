import logging
from aiogram import Bot, Dispatcher, executor, types
import config as cfg
import markups as nav

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
      await bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=nav.mainMenu)

dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if message.text == "Профиль":
            await bot.send_message(message.from_user.id, f"ID:{message.from_user.id}\nhttps://t.me/{cfg.BOT_NICKNAME}?start={message.from_user.id}\nКол-во рефералов: 0")






@dp.message_handler()
async def bot_message(message: types.Message):
    if  message.chat.type == 'private':
        pass 

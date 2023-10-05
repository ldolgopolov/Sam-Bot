from aiogram import Bot
from aiogram.types import Message
from config import Config


async def on_startup(bot: Bot):
    await bot.send_message(Config.admin_id, '✅Бот активирован✅')
    print('Bot has been activated')

async def on_shutdown(bot: Bot):
    await bot.send_message(Config.admin_id, '⛔️Бот приостановлен⛔️')
    print('Bot stopped')
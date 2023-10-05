from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from config import Config
from aiogram.filters import Command, CommandStart, Filter
from aiogram.enums import ContentType
from aiogram import F
import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from user.callbacks.user_lang import user_lang_call
from user.clicker_menu.clicker_options import clicker_balance, clicker_click, clicker_top_users, cmd_clicker
from user.handlers.cmd_start import welcome
from user.handlers.main_menu.main_menu_options import to_main_menu
from utils.db import Database
from admin.handlers.admin_notify import on_shutdown, on_startup


async def main():
    logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=Config.token)
    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    db = Database()
    db.create_database()

    #---------------------------------------- CALLBACKS ----------------------------------------
    dp.callback_query.register(user_lang_call, F.data.startswith('lang_'))

    #---------------------------------------- ENG ----------------------------------------
    dp.message.register(cmd_clicker, F.text == 'Clicker💸')
    dp.message.register(clicker_click, F.text == 'Click🎋')
    dp.message.register(clicker_balance, F.text == 'Balance💸')
    dp.message.register(clicker_top_users, F.text == 'Top players🏆')
    dp.message.register(to_main_menu, F.text == 'To the main menu➡️')

    #---------------------------------------- RUS ----------------------------------------
    dp.message.register(cmd_clicker, F.text == 'Кликер💸')
    dp.message.register(clicker_click, F.text == 'Клик🎋')
    dp.message.register(clicker_balance, F.text == 'Баланс💸')
    dp.message.register(clicker_top_users, F.text == 'Топ игроков🏆')
    dp.message.register(to_main_menu, F.text == 'В главное меню➡️')

    #---------------------------------------- STATES ----------------------------------------

    #---------------------------------------- COMMANDS ----------------------------------------
    dp.message.register(cmd_clicker, Command(commands=['clicker']))
    dp.message.register(welcome, CommandStart())


    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
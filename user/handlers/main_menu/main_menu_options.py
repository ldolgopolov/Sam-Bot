from aiogram import Bot
import asyncio
from aiogram.types import Message, FSInputFile
from localization.message_texts import MessageText
from localization.translating import check_lang
from user.keyboards.reply_markups.reply_main_menu import get_main_menu
from utils.db import Database

db = Database()

async def to_main_menu(message: Message):
    user_id = message.from_user.id
    lang = db.get_lang(user_id)
    
    await message.answer(check_lang(MessageText.welcome_text3, lang), reply_markup=get_main_menu(lang),
                              parse_mode='HTML')
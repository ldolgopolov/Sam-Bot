from aiogram import Bot
from aiogram.types import Message, FSInputFile, CallbackQuery
from user.keyboards.reply_markups.reply_main_menu import get_main_menu
from utils.db import Database
from localization.translating import check_lang
from localization.message_texts import MessageText

db = Database()

async def user_lang_call(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    if call.data == 'lang_ru':
        lang = 'ru'
        db.change_user_lang(user_id, lang)
    elif call.data == 'lang_eng':
        lang = 'eng'
        db.change_user_lang(user_id, lang)
    
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    lang = db.get_lang(user_id)
    await call.message.answer(check_lang(MessageText.welcome_text3, lang), reply_markup=get_main_menu(lang),
                              parse_mode='HTML')

    await call.answer()
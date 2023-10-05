from aiogram import Bot
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from user.keyboards.inline_markups.inline_lang_menu import get_lang_kb
from utils.db import Database
from localization.message_texts import MessageText, ButtonText
from localization.translating import check_lang
from stickers import Stickers
from utils.typing_action import send_typing_action_1sek, send_typing_action_2sek

db = Database()

async def welcome(message: Message, bot: Bot):
    if message.chat.type == 'private':
        db = Database()
        db.add_user(message, bot)
        user_id = message.from_user.id

        await bot.send_sticker(message.chat.id, sticker=Stickers.gift_opening)
        await send_typing_action_1sek(message, bot)
        lang = db.get_lang(user_id)
        await message.answer(f'<b>{check_lang(MessageText.welcome_text1, lang)}{message.from_user.first_name}{check_lang(MessageText.welcome_text2, lang)}</b>',
                             parse_mode='HTML')
        await send_typing_action_1sek(message, bot)
        await message.answer('Select a language/Выбери язык:', reply_markup=get_lang_kb(), parse_mode='HTML')
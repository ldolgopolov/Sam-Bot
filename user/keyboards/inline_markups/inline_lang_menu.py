from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from localization.translating import check_lang
from localization.message_texts import ButtonText


#---------- Get Language Keyboard ----------
def get_lang_kb():
    buttons = [
        [InlineKeyboardButton(text='🇷🇺Русский',
                              callback_data='lang_ru'),
         InlineKeyboardButton(text='🇬🇧English',
                              callback_data='lang_eng')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
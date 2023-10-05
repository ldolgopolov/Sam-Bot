import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from localization.message_texts import MessageText, ButtonText
from localization.translating import check_lang


#---------- Main menu ----------
def get_main_menu(lang):
    n = random.randint(0, 8)
    text = ['/menu', '/bamboo', '/shop', '/pawnshop', '/casino', '/profile', '/sender', '/smoke', '/help']
    menu_kb = ReplyKeyboardBuilder()

    menu_kb.button(text=check_lang(ButtonText.clicker_button, lang))
    menu_kb.button(text=check_lang(ButtonText.games_button, lang))
    menu_kb.button(text=check_lang(ButtonText.settings_button, lang))
    menu_kb.button(text=check_lang(ButtonText.feed_button, lang))
    menu_kb.adjust(2, 2)

    return menu_kb.as_markup(resize_keyboard=True,
                              one_time_keyboard=True,
                             input_field_placeholder=f'{text[n]}')
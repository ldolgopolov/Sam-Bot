from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from localization.message_texts import ButtonText
from localization.translating import check_lang


#---------- Clicker Menu ----------
def get_clicker_menu(lang):
    clicker_kb = ReplyKeyboardBuilder()

    clicker_kb.button(text=check_lang(ButtonText.click_button, lang))
    clicker_kb.button(text=check_lang(ButtonText.balance_button, lang))
    clicker_kb.button(text=check_lang(ButtonText.top_players_button, lang))
    clicker_kb.button(text=check_lang(ButtonText.back_button, lang))
    clicker_kb.adjust(2, 2)

    return clicker_kb.as_markup(resize_keyboard=True,
                              one_time_keyboard=False)
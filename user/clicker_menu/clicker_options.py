import time
from aiogram import Bot
import asyncio
from aiogram.types import Message, FSInputFile
from localization.translating import check_lang
from user.keyboards.reply_markups.reply_clicker_menu import get_clicker_menu
from utils.typing_action import send_typing_action_1sek
from stickers import Stickers
from localization.message_texts import MessageText
from utils.db import Database

db = Database()

times = {}

async def cmd_clicker(message: Message, bot: Bot):
    user_id = message.from_user.id
    lang = db.get_lang(user_id)
    await send_typing_action_1sek(message, bot)
    await bot.send_sticker(message.chat.id,
                           sticker=Stickers.throw_like)
    
    await send_typing_action_1sek(message, bot)
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"<em>{check_lang(MessageText.tavern_link_text1, lang)}<b>{check_lang(MessageText.tavern_link_text2, lang)}</b></em>",
        parse_mode='HTML')
    await send_typing_action_1sek(message, bot)
    await bot.send_message(message.chat.id, f'{check_lang(MessageText.clicker_text1, lang)}', reply_markup=get_clicker_menu(lang))


async def clicker_click(message: Message, bot: Bot):
    user_id = message.from_user.id
    lang = db.get_lang(user_id)
    current_time = times.get(user_id, 0)

    if current_time and (time.time() - current_time) < 5:
        cooldown: int = 5 - (time.time() - current_time)
        timer_mes = await bot.send_message(chat_id=message.chat.id, text=f"<em>{round(cooldown)} {check_lang(MessageText.timer_text, lang)}</em>🕐",
                               parse_mode='HTML')
        await asyncio.sleep(1)
        await bot.delete_message(chat_id=message.from_user.id, message_id=timer_mes.message_id - 1)
        await bot.delete_message(chat_id=message.from_user.id, message_id=timer_mes.message_id)
        return
    times[user_id] = time.time()

    await db.user_click(message, bot, user_id, lang)


async def clicker_balance(message: Message, bot: Bot):
    user_id = message.from_user.id
    lang = db.get_lang(user_id)
    balance = db.get_user_balance(user_id)

    await message.answer(f'<em><b>{check_lang(MessageText.clicker_balance_text, lang)}:</b></em>\n'
                                f'-----------------------------\n'
                                f'{round(balance[0], 1)} 🎋  {round(balance[1], 1)} 💎\n'
                                f'-----------------------------',
                                parse_mode='HTML')
    

async def clicker_top_users(message: Message, bot: Bot):
    user_id = message.from_user.id
    lang = db.get_lang(user_id)

    current_time = times.get(user_id, 0)

    if current_time and (time.time() - current_time) < 5:
        cooldown: int = 5 - (time.time() - current_time)
        timer_mes = await bot.send_message(chat_id=message.chat.id, text=f"<em>{round(cooldown)} {check_lang(MessageText.timer_text, lang)}</em>🕐",
                               parse_mode='HTML')
        await asyncio.sleep(1)
        await bot.delete_message(chat_id=message.from_user.id, message_id=timer_mes.message_id - 1)
        await bot.delete_message(chat_id=message.from_user.id, message_id=timer_mes.message_id)
        return
    times[user_id] = time.time()

    top_bamboo_users = db.get_top_bamboo_users(10)
    top_diamond_users = db.get_top_diamond_users(10)

    await message.answer(f'----- 💰<em>{check_lang(MessageText.top_users_text1, lang)}</em>💰 -----\n\n', parse_mode='HTML')
    for i, user in enumerate(top_bamboo_users, start=1):
        user_nickname = db.get_user_name(user.user_id)
        user_inst = db.get_user_inst(user.user_id)
        await message.answer(f'---------------------------------------\n'
                            f'<b>{await number_to_symbol(i)}</b> - <b>{user_nickname[0]} {user_nickname[1]}</b> : {round(user.bamboo_balance, 1)}🎋\n'
                            f'        <b>Inst:</b> <em>{user_inst}</em>\n'
                            f'---------------------------------------', parse_mode='HTML')
    
    await message.answer(f'----- 💎<em>{check_lang(MessageText.top_users_text2, lang)}</em>💎 -----\n\n', parse_mode='HTML')
    for i, user in enumerate(top_diamond_users, start=1):
        user_nickname = db.get_user_name(user.user_id)
        user_inst = db.get_user_inst(user.user_id)
        await message.answer(f'---------------------------------------\n'
                            f'<b>{await number_to_symbol(i)}</b> - <b>{user_nickname[0]} {user_nickname[1]}</b> : {user.diamond_balance} 💎\n'
                            f'        <b>Inst:</b> <em>{user_inst}</em>\n'
                            f'---------------------------------------', parse_mode='HTML')
        

async def number_to_symbol(i):
    places = {
        1: '🥇',
        2: '🥈',
        3: '🥉'
    }

    if i in range(1, 4):
        return places[i]
    else:
        return i
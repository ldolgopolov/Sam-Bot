from dataclasses import dataclass

@dataclass
class ButtonText:
    #Main Menu KB
    games_button = 'Игры🎮'
    feed_button = 'Покормить🍎'
    settings_button = 'Настройки⚙️'
    clicker_button = 'Кликер💸'

    click_button = 'Клик🎋'
    balance_button = 'Баланс💸'
    top_players_button = 'Топ игроков🏆'
    back_button = 'В главное меню➡️'

@dataclass
class MessageText:
    welcome_text1 = 'Привет, '
    welcome_text2 = '!\nЯ весёлая, интерактивная красная панда Сэм!\nРад знакомству😊'
    welcome_text3 = 'Давай веселиться!🎉'
    timer_text = 'секунд осталось до повторного клика'
    collected_text = 'собрано'
    clicker_balance_text = 'Баланс'
    tavern_link_text1 = 'Чтобы собирать больше бамбука🎋 за один клик, тебе нужно зайти\nв '
    tavern_link_text2 = 'Таверну Улучшений💸'
    clicker_text1 = 'Давай собирать бамбук🎋'
    top_users_text1 = 'Мажоры в чате'
    top_users_text2 = 'Главные ювелиры'
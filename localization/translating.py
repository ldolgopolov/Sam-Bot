from localization.message_texts import MessageText, ButtonText

translation = {
    'eng': {
        MessageText.welcome_text1: 'Hello, ',
        MessageText.welcome_text2: "!\nI'm a fun, interactive red panda Sam!\nNice to meet you😊",
        MessageText.welcome_text3: "Let's have fun!🎉",
        MessageText.tavern_link_text1: 'To collect more bamboo🎋 in one click, you need to go to the ',
        MessageText.tavern_link_text2: 'Improvement Tavern💸',
        MessageText.clicker_text1: "Let's gather bamboo🎋",
        MessageText.timer_text: 'seconds left to click again',
        MessageText.collected_text: 'collected',
        MessageText.clicker_balance_text: 'Balance',
        MessageText.top_users_text1: 'Majors in chat',
        MessageText.top_users_text2: 'Chief jewelers',

        ButtonText.games_button: 'Games🎮',
        ButtonText.feed_button: 'Feed🍎',
        ButtonText.settings_button: 'Settings⚙️',
        ButtonText.clicker_button: 'Clicker💸',

        ButtonText.click_button: 'Click🎋',
        ButtonText.balance_button: 'Balance💸',
        ButtonText.top_players_button: 'Top players🏆',
        ButtonText.back_button: 'To the main menu➡️'
    }
}

def check_lang(text, lang):
    if lang == 'ru':
        return text
    elif lang == 'eng':
        try:
            return translation[lang][text]
        except:
            return text
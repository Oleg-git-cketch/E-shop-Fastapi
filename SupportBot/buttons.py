from telebot import types


def number_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Отправить номер📞', request_contact=True)
    kb.add(but1)

    return kb

def questions():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Проблемы с регистрацией')
    but2 = types.KeyboardButton('Поддержка пользователей и настройки аккаунта')
    but3 = types.KeyboardButton('Проблемы с сетью или интернет-соединением')
    but4 = types.KeyboardButton('Запросы на возврат или обмен товаров')
    but5 = types.KeyboardButton('Безопасность и конфиденциальность')
    but6 = types.KeyboardButton('Связаться с администратором')
    kb.add(but1)
    kb.add(but2)
    kb.add(but3)
    kb.add(but4)
    kb.add(but5)
    kb.add(but6)
    return kb

def back_to_home():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_but = types.KeyboardButton('/start')
    kb.add(back_but)
    return kb
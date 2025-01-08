import telebot

import db
import buttons as bt
from SupportBot.buttons import questions

bot = telebot.TeleBot('7108456694:AAHeO3i1lX3VxekGSZh0HdT0yUfNLXiy81s') # @PySiteSupportBot
admin_id = 7040733741
admins = {}
users = {}


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    menu = questions()
    if db.check_user(user_id):
        bot.send_message(user_id, f'Здравствуйте, @{message.from_user.username}!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Выберите пункт меню:', reply_markup=menu)
    else:
        bot.send_message(user_id, 'Привет! Давайте начнем регистрацию!\n'
                                  'Введите ваше Имя!', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично! Теперь отправьте свой номер через кнопку!',
                     reply_markup=bt.number_button())
    bot.register_next_step_handler(message, get_number, user_name)

def get_number(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_number = message.contact.phone_number
        db.register(user_id, user_name, user_number)
        bot.send_message(user_id, 'Вы успешно зарегистрированы!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        menu = questions()
        bot.send_message(user_id, 'Выберите пункт меню:',
                         reply_markup=menu)
    else:
        bot.send_message(user_id, 'Отправьте номер через кнопку ниже!')
        bot.register_next_step_handler(message, get_number, user_name)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    if message.text == "Проблемы с регистрацией":
        bot.send_message(user_id, "Здравствуйте!\nЕсли у вас возникли трудности при создании аккаунта, пожалуйста, убедитесь, что вы правильно вводите все данные (например, email и пароль).\nТакже проверьте, не использовали ли вы уже этот email для регистрации.\n\nЕсли ошибка продолжает возникать, попробуйте выполнить следующие шаги:\n\n1. Перезагрузите страницу или перезапустите приложение.\n\n2. Попробуйте использовать другой email.\n\n3. Если ошибка не устраняется, сообщите нам (@Oleg_Fozen) точную ошибку, и мы постараемся вам помочь.", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, "Вернуться на главное меню:", reply_markup=bt.back_to_home())
    elif message.text == "Поддержка пользователей и настройки аккаунта":
        bot.send_message(user_id, "Если у вас возникли вопросы по поводу настроек вашего аккаунта, изменению данных или восстановлению доступа, пожалуйста, выполните следующие шаги:\n\nИзменение данных: Чтобы изменить ваше имя или контактные данные, обратитесь в поддержку (@Oleg_Fozen).\nВосстановление пароля: Если вы забыли свой пароль, воспользуйтесь функцией восстановления через ссылку на странице входа.\nПроблемы с аккаунтом: Если у вас возникли технические проблемы с аккаунтом, напишите нам (@Oleg_Fozen), и мы постараемся решить вашу проблему как можно скорее.", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, "Вернуться на главное меню:", reply_markup=bt.back_to_home())
    elif message.text == "Проблемы с сетью или интернет-соединением":
        bot.send_message(user_id, "Если у вас возникли проблемы с подключением к сети или интернет-соединению, пожалуйста, выполните следующие шаги:\n\nПроверьте подключение: Убедитесь, что ваше устройство подключено к сети Wi-Fi или мобильному интернету.\nПопробуйте перезагрузить ваше устройство или роутер (если используете Wi-Fi).\nПроверьте скорость интернета:\n\nИспользуйте онлайн-сервисы для проверки скорости интернета (например, speedtest.net) и убедитесь, что скорость соответствует вашим ожиданиям.\nОтключите и снова подключитесь к сети:\nЕсли вы используете Wi-Fi, попробуйте отключиться и снова подключиться к сети.\nДля мобильного интернета попробуйте отключить и снова включить мобильные данные. Проблемы с сервером или приложением: Иногда проблемы могут быть на стороне сервера.\n\nЕсли ни одно из решений не помогает, cвяжитесь с нашей поддержкой (@Oleg_Fozen) для дальнейшей помощи. Мы постараемся помочь вам решить проблему в кратчайшие сроки.")
        bot.send_message(user_id, "Вернуться на главное меню:", reply_markup=bt.back_to_home())
    elif message.text == "Запросы на возврат или обмен товаров":
        bot.send_message(user_id, "Если вам нужно вернуть или обменять товар, выполните следующие шаги:\n\nознакомьтесь с условиями возврата на нашем сайте (обычно в течение 14 дней, товар в оригинальной упаковке), отправьте номер заказа и причину возврата для начала процесса, после чего мы предоставим инструкции для возврата товара.\n\nЕсли нужно обменять товар, уточните, что хотите получить взамен, и мы поможем организовать обмен.\n\nВозврат средств производится в течение 5-7 рабочих дней тем же способом, которым была оплачена покупка")
        bot.send_message(user_id, "Вернуться на главное меню:", reply_markup=bt.back_to_home())
    elif message.text == "Безопасность и конфиденциальность":
        bot.send_message(user_id, "Мы придаем большое значение защите ваших данных, используя современные методы шифрования и SSL-сертификаты для безопасной передачи информации.\nМы соблюдаем политику конфиденциальности, и ваши данные используются только для обслуживания и не передаются третьим лицам без вашего согласия.\nРекомендуем использовать надежные пароли для вашего аккаунта, а также обновлять их регулярно.\nВы можете запросить доступ к своим данным или их удаление, а также связаться с поддержкой (@Oleg_Fozen) при подозрении на компрометацию аккаунта. Мы регулярно обновляем наши системы безопасности, чтобы защитить ваши данные от угроз.\nЕсли у вас есть вопросы, не стесняйтесь обращаться!")
        bot.send_message(user_id, "Вернуться на главное меню:", reply_markup=bt.back_to_home())
    elif message.text == "Связаться с администратором":
        bot.send_message(user_id, "Наш администратор @Oleg_Fozen всегда поможет вам! Пишите не стесняйтесь!")
        bot.send_message(user_id, "Вернуться на главное меню:", reply_markup=bt.back_to_home())

bot.polling()

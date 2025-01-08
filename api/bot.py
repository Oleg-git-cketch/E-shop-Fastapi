import telebot

API_TOKEN = '7774947483:AAHCNR3YnpyWauWQANV2P1RBhBzQU3MufxM'
CHAT_ID = '7040733741'

bot = telebot.TeleBot(API_TOKEN)


def send_order_to_telegram(cart_items, username, total_price, discount):
    message = f"Новый заказ от пользователя {username}:\n\n"

    total_price_calculated = 0
    for item in cart_items:
        message += f"Продукт: {item['product_name']}\n" \
                   f"Количество: {item['quantity']}\n" \
                   f"Цена за штуку: {item['price']}\n" \
                   f"Конечная цена: {item['total_price']}\n\n"
        total_price_calculated += item['total_price']

    message += f"Промокод: -{discount} UZS\n\n"
    message += f"Общая сумма заказа: {total_price} UZS\n\n"
    message += "Заказ успешно оформлен!"

    try:
        bot.send_message(CHAT_ID, message)
        print("Сообщение успешно отправлено в Telegram!")
    except Exception as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")

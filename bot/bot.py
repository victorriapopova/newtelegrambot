import telebot
from secret import TOKEN
import random

bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я бот для генерации случайных чисел. Напиши /help для списка команд.")


# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Я могу сгенерировать случайное число в заданном диапазоне. Напиши /generate для начала.")


# Обработчик команды /generate
@bot.message_handler(commands=['generate'])
def handle_generate(message):
    msg = bot.send_message(message.chat.id, "Введите диапазон чисел (начало и конец через пробел):")
    bot.register_next_step_handler(msg, process_range_step)


def process_range_step(message):
    try:
        start, end = map(int, message.text.split())
        if start >= end:
            bot.send_message(message.chat.id, "Некорректный диапазон чисел. Начало должно быть меньше конца.")
            return
        # Генерируем случайное число в заданном диапазоне
        random_number = random.randint(start, end)
        bot.send_message(message.chat.id, f"Случайное число в диапазоне от {start} до {end}: {random_number}")
    except ValueError:
        bot.send_message(message.chat.id, "Некорректный формат ввода. Введите два целых числа через пробел.")


if __name__ == "__main__":
    bot.polling()

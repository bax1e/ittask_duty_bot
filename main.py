import telebot

TOKEN = "7911875136:AAF943QOo0y1ZYufvifFK10-m6xq1hWo-kU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я рабочий бот компании it-task 👋")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Привет!")

bot.infinity_polling()



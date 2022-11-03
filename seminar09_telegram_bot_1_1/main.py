# from imaplib import Commands
import telebot
# import token_1

# решение преподавателя
def deleting(text):
    while text.find('абв') != -1:
        text = text.replace('абв', '')
    return text

# https://pypi.org/project/pyTelegramBotAPI/
bot = telebot.TeleBot("5647569592:AAFjT40cJOjnDzpoCNBZdcHNTLEKRKeevUo")  # t.me/seminar_9_abv_bot

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, deleting(message.text))

bot.infinity_polling()
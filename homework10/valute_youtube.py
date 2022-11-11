import telebot
from pytube import YouTube
import requests

bot = telebot.TeleBot("*********************************", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.send_message(message.chat.id, "Здравствуйте!")
  bot.send_message(message.chat.id, "Если хотите увидеть клип, напишите 'клип'")
  bot.send_message(message.chat.id, "Если хотите узнать курс USD, напишите 'курс'")
  
  
@bot.message_handler(func=lambda message: True)
def yt_do(message):
  if message.text == 'клип':
    url = 'https://www.youtube.com/watch?v=msipKortNIA'
    yt = YouTube(url)
    yt.streams.filter(res="360p").first().download(filename=f'slade.mp4')
    video=open(f'slade.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True)
    # return yt.title
  elif message.text == 'курс':
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    bot.send_message(message.chat.id, data['Valute']['USD']['Value'])
  else:
    bot.send_message(message.chat.id, "Напишите правильную команду")


bot.infinity_polling()
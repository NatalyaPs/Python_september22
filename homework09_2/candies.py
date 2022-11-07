# БОТ ДЛЯ ИГРЫ С КОНФЕТАМИ. Правила: На столе лежит 2021 (117 для проверки, т.к. %28 =5, как и 2021) конфета. Игрет человек против бота. 
# Первый ход за человеком. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 

import telebot
import random


bot = telebot.TeleBot("////////////////////////////////////////", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  # bot.clear_step_handler(message)  # ====================== попытка перезапуска )
  bot.send_message(message.chat.id, "Играем?\nВаш ход")
  

a = 117


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  global a

  if int(message.text) > a:
    bot.reply_to(message, 'Проверьте остаток конфет')  
  elif int(message.text) <=0 or int(message.text) > 28:
    bot.reply_to(message, 'Возьмите от 1 до 28 конфет')
  else:
    a -= int(message.text)
    bot.reply_to(message, f'Осталось: {a}')
    p = 0
  if a == 0 and p == 0:
    bot.send_message(message.chat.id, 'Вы победили! Чтобы начать снова, перезапустите программу.')
    bot.send_message(message.chat.id, '٩(｡•́‿•̀｡)۶!')
    # send_welcome(message)  # ===================
        
  elif a <= 28:
    cb = a
    a -= cb
    bot.send_message(message.chat.id, f'Бот взял {cb}\nосталось : {a}')
    bot.send_message(message.chat.id, 'Бот победил! Чтобы начать снова, перезапустите программу.')
    bot.send_message(message.chat.id, 'w(°ｏ°)w')
    # send_welcome(message)  # =================
  else:
    cb = random.randint(1,29)
    a -= cb
    bot.send_message(message.chat.id, f'Бот взял {cb}\nосталось : {a}')
    p = 1

   
bot.infinity_polling()

# основа игры ====================================================
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):

#   global a
#   a -= int(message.text)
#   bot.reply_to(message, f'Осталось: {a}')
#   cb = random.randint(1,10)
#   a -= cb
#   bot.send_message(message.chat.id, f'Бот взял {cb}, осталось : {a}')

# bot.infinity_polling()

# ================================================================
# перезапуск?
# flag = 1
# @bot.message_handler(commands=['stop', 'end'])
# def stop(message):
#     global flag
#     flag = 0
#     bot.send_message(message.chat.id, "Игра окончена.")

# @bot.message_handler(commands=['stop'])
# def stop(message):
#   bot.reply_to(message, "Игра завершена\nДля начала нажмите /start")
#   bot.stop_polling()
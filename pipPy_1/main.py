# from turtle import update
from lib2to3.pgen2 import token
from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from bot_commands import *


# # из лекции

updater = Updater('5563371047:AAFovHYAvy3GT2yiMDFqDXw-DB_vX0pkzpA')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')
updater.start_polling()
updater.idle()






# # https://python-telegram-bot.org/
# def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:                            
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')


# app = ApplicationBuilder().token("5563371047:AAFovHYAvy3GT2yiMDFqDXw-DB_vX0pkzpA").build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()

# # print('server start')








#  ------------------------------------------------------------------------


# # для графиков и т.п:  - очень объёмная библиотека, изучение может занять месяцы - pip install matplotlib - перейти на-> homepage -> examples
# import matplotlib.pyplot as plt
# import numpy as np

# # пример кода Камянецкого из лекции:
# list = [1, 2, 3, 2, 7]
# plt.plot(list)
# plt.show()




#              *******

# # пример с  сайта python:
# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()






# ------------------------------------------------------

# import emoji

# print(emoji.emojize('Python is :thumbs_up:')) # Python is 👍



# -----------------------------------------


# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=10)  # max=20
# for i in range(10):
#     time.sleep(1)
#     # Do some work
#     bar.next()
# bar.finish()
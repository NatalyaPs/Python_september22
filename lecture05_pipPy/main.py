# from lib2to3.pgen2 import token
from  telegram import Update
from  telegram.ext import Updater, ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext   # , update_queue - где должен быть этот позиционный аргумент?
from bot_commands import *



# # из лекции
updater = Updater("5563371047:AAFovHYAvy3GT2yiMDFqDXw-DB_vX0pkzpA")  # показывает ошибку


updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')
updater.start_polling()
updater.idle()
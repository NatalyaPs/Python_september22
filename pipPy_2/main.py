from lib2to3.pgen2 import token
from  telegram import Update
from  telegram.ext import Updater, ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from bot_commands import *
from token_1 import *


# # из лекции
updater = Updater(token_1)   #.bot()

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')
updater.start_polling()
updater.idle()

# from lib2to3.pgen2 import token
from  telegram import Update
from  telegram.ext import Updater, ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext   # , update_queue - где должен быть этот позиционный аргумент?
from bot_commands import *



# # из лекции
updater = Updater("")  # показывает ошибку в этой строке /// токен в файле 


updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')
updater.start_polling()
updater.idle()
# выдает ошибку, но в лекции ее не было (???)
# TypeError: Updater.__init__() missing 1 required positional argument: 'update_queue'
# Ошибка типа: Средство обновления.__init__() отсутствует 1 обязательный позиционный аргумент: 'update_queue'
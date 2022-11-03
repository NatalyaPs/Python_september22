from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import datetime

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/help')


def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')
    

def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum  123 5421  => на выходе получим команду и 2 числа через пробел, которые надо сложить
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')

import telegram
from telegram.ext import *
from decouple import config
from AquaSenseCommands import Commands


TOKEN = config('TOKEN')
bot = telegram.Bot(token=TOKEN)

updater = Updater(bot.token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(
    Filters.status_update.new_chat_members, Commands.start_command))
updater.start_polling()
updater.idle()

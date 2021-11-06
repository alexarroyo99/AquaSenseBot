import telegram
from telegram.ext import *


class Commands:

    def start_command(update, context):
        bot = context.bot
        name = update.effective_user["first_name"]
        bot.sendMessage(
            chat_id="-761945628",
            text=f"""\U0001F389Bienvenido {name}\U0001F389
Le estaremos notificando cuando tenga flujo de agua
Para mas detalles visite nuestro sitio web:
\U0001F30Fwww.aquasense.com.co"""
        )

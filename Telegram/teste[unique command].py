from telegram.ext import Updater
updater = Updater(token='466963914:AAGJpIKVBG4Nc-tZagqDNeZ6g5U_lvAu50w')

dispatcher = updater.dispatcher


""" Setting up a logging sys """
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

""" Starter message """
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

""" Command Handler """
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

""" Waiting a message"""
updater.start_polling()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent




logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("Liberar Porta", callback_data='1'),
                 InlineKeyboardButton("Ver quem é", callback_data='2')],

                [InlineKeyboardButton("Polícia ?", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Alguém está à porta, que fazer ?', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query

    chat_id = query.message.chat_id
    print("{}".format(chat_id))
    if query.data == '1':
        bot.edit_message_text(text="Opção 1...",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    if query.data == '2':
        bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me!")
        bot.send_photo(chat_id=chat_id, photo=open('/home/henrique/T/a/henrique/henrique.png', 'rb'))

        #bot.edit_message_text(text="Opção 1...",
                              #chat_id=query.message.chat_id,
                              #message_id=query.message.message_id)


def help(bot, update):
    update.message.reply_text("Use /start para testar esse bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


#def main():
    # Create the Updater and pass it your bot's token.
updater = Updater("466963914:AAGJpIKVBG4Nc-tZagqDNeZ6g5U_lvAu50w")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)

bot = updater.bot
dp = updater.dispatcher

# Start the Bot
#updater.start_polling(clean=True)


# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
#updater.idle()


#if __name__ == '__main__':
    #main()

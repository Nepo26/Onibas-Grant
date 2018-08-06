#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from Sample2 import  watch



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    Keyboard =[[KeyboardButton("Op_1"),KeyboardButton("Op_2")],
               [KeyboardButton("Op_3"),KeyboardButton("Op_4")]]
    keyboard=ReplyKeyboardMarkup(Keyboard)
    update.message.reply_text('Hello...', reply_markup=keyboard)

    """keyboard = [[InlineKeyboardButton("Op_1", callback_data='1'),InlineKeyboardButton("Op_2", callback_data='2')],
                [InlineKeyboardButton("Op_3", callback_data='3'),InlineKeyboardButton("Op_4", callback_data='4')]]
answerCallbackQuery
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Choose:', reply_markup=reply_markup)"""


def button(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id

    print("{}".format(chat_id))
    if query.data == '1':
        bot.edit_message_text(text="Opção 1...",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    if query.data == '2':
        bot.edit_message_text(text="I'm a bot, please talk to me!",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
        bot.send_photo(chat_id=chat_id, photo=open('/home/henrique/T/a/henrique/henrique.png', 'rb'))

    if query.data == '3':
        keys = [[InlineKeyboardButton(text = "حساب المطور", url ="t.me/x_p_0")],
                [InlineKeyboardButton(text = "حسابك", url = "t.me/")]]
        key1=InlineKeyboardMarkup(keys)
        bot.send_message(chat_id=chat_id ,text="*Welcome In The Group:*", reply_markup=key1 , parse_mode="markdown")

    if query.data == '4':
        keys = [[KeyboardButton(text = "1")],
                [KeyboardButton(text = "2")]]
        key1=ReplyKeyboardMarkup(keys)
        bot.send_message(chat_id=chat_id ,text="*Welcome In The Group:*", reply_markup=key1 , parse_mode="markdown")




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
print("Ok")
updater.start_polling(clean=True)
print("ok")
#while True:
#    watch()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()


#if __name__ == '__main__':
    #main()

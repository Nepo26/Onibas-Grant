from alecrim import bot,dp,updater, CommandHandler #,Updater

def hello(bot, update):
    update.message.reply_text("Use /start para testar esse bot.")



dp.add_handler(CommandHandler('hello',hello))

updater.start_polling(clean=True)
bot.send_message(chat_id="571008755", text="Testing")

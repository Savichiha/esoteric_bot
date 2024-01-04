from glob import glob
import logging
from random import choice
from telegram.ext import Updater, CommandHandler
import setting

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    my_keyboard = ReplyKeyboardMarkup([['/taro']])
    update.message.reply_text(f"Привет💫" , reply_markup=my_keyboard)

def send_taro_picture(update, context):
    taro_photo_list = glob('images/taro*.jp*g')
    taro_photo_filename = choice(taro_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(taro_photo_filename, 'rb'))


def main():
    mybot = Updater(setting.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("taro", send_taro_picture))


    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

from main import wildbowify
from config import TOKEN, CHAT_ID
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def generate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='One moment, please...')
    wildbowify()
    with open("result.txt", 'r') as f:
        text = f.read().split('\n\n')
        for i in text:
            if i != '':
                context.bot.send_message(chat_id=update.effective_chat.id, text=i)
        f.close()


bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

generate_handler = CommandHandler('generate', generate)
dispatcher.add_handler(generate_handler)



updater.start_polling()

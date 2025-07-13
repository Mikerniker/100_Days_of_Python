import telegram
import logging
from telegram import Update
from telegram.ext import  filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
from main import get_btc_details


TOKEN ="my_token"
MY_ID = "my_id"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi, I'm a BTC alert bot! To get started type /btc_price to get the current BTC price"

    )
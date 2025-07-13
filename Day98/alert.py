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

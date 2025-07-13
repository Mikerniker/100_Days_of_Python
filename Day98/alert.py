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

async def btc_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_btc_details()
    price = data['current_price']

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"BTC price is ${price:,.2f}"
    )



if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    price_handler = CommandHandler('btc_price', btc_price)

    application.add_handler(start_handler)
    application.add_handler(price_handler)
  

    application.run_polling()

import telegram
import logging
from telegram import Update,  ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    ApplicationBuilder,
    filters,
)
from main import get_btc_details

TOKEN ="my_token"
MY_ID = "my_id"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)




async def btc_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_btc_details()
    price = data['current_price']

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"BTC price is ${price:,.2f}"
    )


upper_threshold_alert = 115000
lower_threshold_alert = 100000

async def btc_alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_btc_details()
    price = data['current_price']
    if price > upper_threshold_alert:
        text_alert = f"🚨 BTC has crossed ${upper_threshold_alert:,.2f}!"
    elif price < lower_threshold_alert:
        text_alert = f"📉 BTC dropped below ${lower_threshold_alert:,.2f}!"
    else:
        text_alert = f"✅ BTC price is currently ${price:,.2f}"

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=text_alert
    )

# TO REVIEW


UPPER, LOWER = range(2)

async def test_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Asks the user about user's upper threshold."""

    await update.message.reply_text(
        "Hi! What is your upper threshold. "
        "Send /cancel to stop talking to me.\n\n",
    )

    return UPPER

async def upper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    text = update.message.text

    if not text.isdigit():
        await update.message.reply_text("Please enter a valid number for your upper threshold.")
        return UPPER  # Stay in current state until valid input

    context.user_data["upper"] = int(text)  # Save it
    logger.info("Upper threshold for %s is %s", user.first_name, text)

    await update.message.reply_text("Got it! What about your lower threshold?")
    return LOWER



# async def get_lower(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     pass


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    price_handler = CommandHandler('btc_price', btc_price)

    
    application.add_handler(price_handler)
  

    application.run_polling()

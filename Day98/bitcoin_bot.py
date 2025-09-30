import asyncio
import logging
import requests
import time
import threading
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)

# Bot Configuration
BOT_TOKEN = "*******"
DEFAULT_CHAT_ID = "********"

# Conversation states
CHOOSING_TYPE, ENTERING_PRICE = range(2)

# User data storage
user_alerts = {}

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_bitcoin_price():
    """Get current Bitcoin price from CoinGecko"""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        price = data['bitcoin']['usd']
        return price, None
        
    except Exception as e:
        logger.error(f"Error fetching Bitcoin price: {e}")
        return None, str(e)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler"""
    user = update.effective_user
    logger.info(f"User {user.first_name} ({user.id}) started the bot")
    
    welcome_message = f"""
🤖 <b>Welcome to Bitcoin Alert Bot!</b>

Hi {user.first_name}! I'll help you monitor Bitcoin prices.

<b>Commands:</b>
/price - Get current Bitcoin price
/alert - Set a price alert
/my_alerts - View your alerts
/help - Show help

<b>Quick Start:</b>
1. Use /alert to set a price threshold
2. I'll monitor Bitcoin every 30 seconds
3. You'll get notified when price reaches your target!

Let's get started! 🚀
    """
    
    await update.message.reply_text(welcome_message, parse_mode='HTML')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    help_text = """
<b>🤖 Bitcoin Alert Bot Help</b>

<b>Commands:</b>
/price - Get current Bitcoin price
/alert - Set a new price alert
/my_alerts - View your alerts
/help - Show this help

<b>Setting Alerts:</b>
1. Use /alert command
2. Choose "Above" or "Below"
3. Enter your target price
4. Get notified when price hits!

<b>Example:</b>
/alert → Above → 50000
This alerts you when Bitcoin goes above $50,000
    """
    
    await update.message.reply_text(help_text, parse_mode='HTML')

async def get_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get current Bitcoin price"""
    try:
        price, error = get_bitcoin_price()
        
        if error:
            await update.message.reply_text(f"❌ Error getting price: {error}")
            return
        
        # Format price with emoji
        if price > 50000:
            emoji = "🚀"
        elif price > 40000:
            emoji = "📈"
        else:
            emoji = "📊"
        
        message = f"""
{emoji} <b>Current Bitcoin Price</b>

💰 <b>Price:</b> ${price:,.2f}
🕐 <b>Time:</b> {datetime.now().strftime('%H:%M:%S')}

<i>Use /alert to set price notifications!</i>
        """
        
        await update.message.reply_text(message, parse_mode='HTML')
        
    except Exception as e:
        logger.error(f"Error in get_price: {e}")
        await update.message.reply_text("❌ Sorry, something went wrong.")

async def start_alert_setup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start alert setup"""
    user_id = update.effective_user.id
    
    if user_id in user_alerts and user_alerts[user_id]:
        existing_alerts = user_alerts[user_id]
        alert_text = "\n".join([f"• {alert['type']} ${alert['price']:,.2f}" for alert in existing_alerts])
        message = f"""
<b>You have alerts set:</b>
{alert_text}

<b>Add another alert?</b>
Choose your alert type:
        """
    else:
        message = """
<b>🔔 Set up your Bitcoin alert!</b>

Choose when you want to be notified:
        """
    
    keyboard = [
        ["🢁 Above a certain price"],
        ["🡻 Below a certain price"],
        ["❌ Cancel"]
    ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        message,
        parse_mode='HTML',
        reply_markup=reply_markup
    )
    
    return CHOOSING_TYPE

async def handle_alert_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle alert type choice"""
    text = update.message.text
    user_id = update.effective_user.id
    
    logger.info(f"User {user_id} chose: {text}")
    
    if "Above" in text:
        context.user_data['alert_type'] = 'above'
        await update.message.reply_text(
            "🢁 <b>Above Alert</b>\n\n"
            "Enter the price (e.g., 50000):\n"
            "<i>I'll alert you when Bitcoin goes above this price</i>",
            parse_mode='HTML',
            reply_markup=ReplyKeyboardRemove()
        )
        return ENTERING_PRICE
    elif "Below" in text:
        context.user_data['alert_type'] = 'below'
        await update.message.reply_text(
            "🡻 <b>Below Alert</b>\n\n"
            "Enter the price (e.g., 40000):\n"
            "<i>I'll alert you when Bitcoin goes below this price</i>",
            parse_mode='HTML',
            reply_markup=ReplyKeyboardRemove()
        )
        return ENTERING_PRICE
    elif "Cancel" in text:
        await update.message.reply_text("❌ Alert setup cancelled.")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Please choose from the options above.")
        return CHOOSING_TYPE



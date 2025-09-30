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
BOT_TOKEN = "my_token"
DEFAULT_CHAT_ID = "my_id"

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

async def handle_price_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle price input"""
    try:
        price_text = update.message.text
        logger.info(f"User entered price: {price_text}")
        
        price = float(price_text)
        alert_type = context.user_data.get('alert_type')
        user_id = update.effective_user.id
        
        if price <= 0:
            await update.message.reply_text("❌ Please enter a valid price (greater than 0).")
            return ENTERING_PRICE
        
        # Store the alert
        if user_id not in user_alerts:
            user_alerts[user_id] = []
        
        alert = {
            'type': alert_type,
            'price': price,
            'created_at': datetime.now()
        }
        user_alerts[user_id].append(alert)
        
        # Send confirmation
        emoji = "🢁" if alert_type == 'above' else "🡻"
        message = f"""
✅ <b>Alert Set Successfully!</b>

{emoji} <b>Type:</b> {alert_type.title()}
💰 <b>Price:</b> ${price:,.2f}
🕐 <b>Set at:</b> {datetime.now().strftime('%H:%M:%S')}

I'll monitor Bitcoin and notify you when it reaches your target!

Use /my_alerts to view all your alerts.
        """
        
        await update.message.reply_text(message, parse_mode='HTML')
        context.user_data.clear()
        return ConversationHandler.END
        
    except ValueError:
        await update.message.reply_text("❌ Please enter a valid number (e.g., 50000).")
        return ENTERING_PRICE
    except Exception as e:
        logger.error(f"Error in handle_price_input: {e}")
        await update.message.reply_text("❌ Something went wrong. Please try again.")
        return ConversationHandler.END

async def show_user_alerts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user's current alerts"""
    user_id = update.effective_user.id
    
    if user_id not in user_alerts or not user_alerts[user_id]:
        await update.message.reply_text(
            "📭 <b>No alerts set</b>\n\n"
            "Use /alert to set your first Bitcoin price alert!",
            parse_mode='HTML'
        )
        return
    
    alerts = user_alerts[user_id]
    alert_text = ""
    
    for i, alert in enumerate(alerts, 1):
        emoji = "🢁" if alert['type'] == 'above' else "🡻"
        alert_text += f"{i}. {emoji} {alert['type'].title()} ${alert['price']:,.2f}\n"
    
    message = f"""
📋 <b>Your Bitcoin Alerts</b>

{alert_text}

<b>Total alerts:</b> {len(alerts)}

Use /alert to add more alerts!
    """
    
    await update.message.reply_text(message, parse_mode='HTML')

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancel conversation"""
    await update.message.reply_text("❌ Operation cancelled.")
    context.user_data.clear()
    return ConversationHandler.END

def send_alert_sync(chat_id, current_price, alert_type, threshold_price):
    """Send price alert to user (synchronous version)"""
    try:
        if alert_type == 'above':
            emoji = "🚀"
            message = f"""
{emoji} <b>BITCOIN PRICE ALERT!</b>

💰 <b>Current Price:</b> ${current_price:,.2f}
🎯 <b>Your Alert:</b> Above ${threshold_price:,.2f}

✅ <b>Target reached!</b> Bitcoin has gone above your alert price!

<i>Alert triggered at {datetime.now().strftime('%H:%M:%S')}</i>
            """
        else:  # below
            emoji = "📉"
            message = f"""
{emoji} <b>BITCOIN PRICE ALERT!</b>

💰 <b>Current Price:</b> ${current_price:,.2f}
🎯 <b>Your Alert:</b> Below ${threshold_price:,.2f}

✅ <b>Target reached!</b> Bitcoin has dropped below your alert price!

<i>Alert triggered at {datetime.now().strftime('%H:%M:%S')}</i>
            """
        
        # Send message using requests
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            logger.info(f"🚨 Alert sent to {chat_id} for {alert_type} ${threshold_price:,.2f}")
        else:
            logger.error(f"Failed to send alert to {chat_id}: {response.text}")
        
    except Exception as e:
        logger.error(f"Failed to send alert to {chat_id}: {e}")

def monitor_prices():
    """Monitor Bitcoin prices and send alerts"""
    logger.info("📊 Starting price monitoring (checking every 30 seconds)")
    
    while True:
        try:
            # Get current Bitcoin price
            current_price, error = get_bitcoin_price()
            
            if error:
                logger.error(f"Monitor failed to get BTC price: {error}")
                time.sleep(30)
                continue
            
            logger.info(f"📈 Current BTC price: ${current_price:,.2f}")
            
            # Check all user alerts
            for user_id, alerts in user_alerts.items():
                for alert in alerts[:]:  # Use slice to avoid modification during iteration
                    try:
                        alert_type = alert['type']
                        threshold_price = alert['price']
                        
                        should_trigger = False
                        
                        if alert_type == 'above' and current_price >= threshold_price:
                            should_trigger = True
                        elif alert_type == 'below' and current_price <= threshold_price:
                            should_trigger = True
                        
                        if should_trigger:
                            logger.info(f"🚨 Alert triggered for user {user_id}: {alert_type} ${threshold_price:,.2f}")
                            
                            # Send alert
                            send_alert_sync(user_id, current_price, alert_type, threshold_price)
                            
                            # Remove the alert after triggering
                            alerts.remove(alert)
                            logger.info(f"✅ Alert removed for user {user_id}")
                            
                    except Exception as e:
                        logger.error(f"Error checking alert for user {user_id}: {e}")
            
            # Wait 30 seconds before next check
            time.sleep(30)
            
        except Exception as e:
            logger.error(f"Error in price monitoring: {e}")
            time.sleep(60)  # Wait 1 minute before retrying

def main():
    """Main function to run the bot"""
    logger.info("🤖 Starting Bitcoin Alert Bot...")
    logger.info(f"Using bot token: {BOT_TOKEN}")
    logger.info(f"Default chat ID: {DEFAULT_CHAT_ID}")
    
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Conversation handler for alerts
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("alert", start_alert_setup)],
        states={
            CHOOSING_TYPE: [
                MessageHandler(filters.Regex("Above"), handle_alert_choice),
                MessageHandler(filters.Regex("Below"), handle_alert_choice),
            ],
            ENTERING_PRICE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_price_input),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    # Add all handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("price", get_price))
    application.add_handler(CommandHandler("my_alerts", show_user_alerts))
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("cancel", cancel))
    
    # Start monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor_prices, daemon=True)
    monitor_thread.start()
    
    logger.info("✅ Bot and monitor starting...")
    logger.info("📱 Bot is ready to receive messages")
    logger.info("📊 Price monitoring is active (checking every 30 seconds)")
    logger.info("🚨 You'll get notifications when Bitcoin reaches your alert prices!")
    logger.info("Press Ctrl+C to stop")
    
    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()

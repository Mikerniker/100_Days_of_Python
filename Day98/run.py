import sys
import os


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the bot
from bitcoin_bot import main

if __name__ == "__main__":
    print("🚀 Starting Bitcoin Alert Bot...")
    print("📱 Bot will be ready to receive messages")
    print("📊 Price monitoring will start automatically")
    print("🚨 You'll get notifications when Bitcoin reaches your alert prices!")
    print("Press Ctrl+C to stop")
    print("-" * 50)
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
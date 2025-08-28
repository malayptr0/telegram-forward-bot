from telethon import TelegramClient, events
import os

# Load from Railway environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")  
SOURCE_BOT = os.getenv("SOURCE_BOT")  # keep as string (username or ID)
TARGET_GROUP = int(os.getenv("TARGET_GROUP"))

# Create Telegram client session with bot token
client = TelegramClient("forwarder", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Handler for new messages from the source bot
@client.on(events.NewMessage(from_users=SOURCE_BOT))
async def handler(event):
    try:
        if event.media:
            await event.forward_to(TARGET_GROUP)
            print(f"📦 Forwarded media message {event.id}")
        else:
            print(f"⏩ Skipped text-only message {event.id}")
    except Exception as e:
        print("❌ Error:", e)

print("🚀 Forwarder running...")
client.run_until_disconnected()

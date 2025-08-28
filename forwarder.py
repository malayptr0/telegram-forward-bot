from telethon import TelegramClient, events
import os

# Load from Railway environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")  # if you need it later
SOURCE_BOT = int(os.getenv("SOURCE_BOT"))  # 👈 add in Railway Variables
TARGET_GROUP = int(os.getenv("TARGET_GROUP"))  # 👈 add in Railway Variables

# Create Telegram client session
client = TelegramClient("forwarder", API_ID, API_HASH)

# Handler for new messages from the source bot
@client.on(events.NewMessage(from_users=SOURCE_BOT))
async def handler(event):
    try:
        if event.media:  # ✅ Only forward if the message contains media
            await event.forward_to(TARGET_GROUP)
            print(f"📦 Forwarded media message {event.id}")
        else:
            print(f"⏩ Skipped text-only message {event.id}")
    except Exception as e:
        print("❌ Error:", e)

print("🚀 Forwarder running...")
client.start()
client.run_until_disconnected()

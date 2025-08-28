from telethon import TelegramClient, events
import config

# Create Telegram client session
client = TelegramClient("forwarder", config.api_id, config.api_hash)

# Handler for new messages from the source bot
@client.on(events.NewMessage(from_users=config.SOURCE_BOT))
async def handler(event):
    try:
        if event.media:  # ✅ Only forward if the message contains media
            await event.forward_to(config.TARGET_GROUP)
            print(f"📦 Forwarded media message {event.id}")
        else:
            print(f"⏩ Skipped text-only message {event.id}")
    except Exception as e:
        print("❌ Error:", e)

print("🚀 Forwarder running...")
client.start()
client.run_until_disconnected()

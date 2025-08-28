from telethon import TelegramClient
import config

client = TelegramClient("forwarder", config.api_id, config.api_hash)

async def main():
    async for dialog in client.iter_dialogs():
        print(f"{dialog.name} -> {dialog.id}")

with client:
    client.loop.run_until_complete(main())

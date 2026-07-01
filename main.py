import os
import asyncio
from telethon import TelegramClient

api_id = int(os.getenv('TELEGRAM_API_ID'))
api_hash = os.getenv('TELEGRAM_API_HASH')
bot_name = os.getenv('TELEGRAM_API_HASH')

bot_name = os.getenv("TELEGRAM_TO")
bot_message = os.getenv("TELEGRAM_MESSAGE")

client = TelegramClient("session", api_id, api_hash)

async def main():
    await client.start()

    # 打开 bot 对话
    await client.send_message(bot_name, bot_message)

with client:
    client.loop.run_until_complete(main())

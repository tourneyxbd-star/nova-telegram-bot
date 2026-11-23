import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


async def main():
    if not BOT_TOKEN or not CHAT_ID:
        raise ValueError("TELEGRAM_BOT_TOKEN এবং TELEGRAM_CHAT_ID সেট করা নেই।")

    bot = Bot(token=BOT_TOKEN)
    message = (
        "✨ *Nova Daily Update*\n"
        "আজকের নির্ধারিত কাজ শুরু করার সময় হয়েছে!"
    )
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")


if __name__ == "__main__":
    asyncio.run(main())

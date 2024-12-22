import asyncio
from random import choice
from aiogram import types
from aiogram.types import ContentType
from loader import bot, dp
from data.config import ADMINS
CHANNELS = ['Amirjon_Karimov_Blog', 'Amirjon_Karimov_Life']

# Reaktsiyalar ro'yxati
reactions = ["👍", "❤", "🔥", "🥰", "👏", "🎉", "🤩", "👌", "😍", "❤‍🔥", "💯", "🤣", "⚡", "🏆", "🍓", "🍾", "💋", "🎃", "😇", "🤝", "😘"]

# Channel postlarga reaktsiya qo'shish
@dp.channel_post_handler(content_types=ContentType.ANY)
async def reaction(message: types.Message):
    # Kanal username'ini tekshirish
    if message.chat.username not in CHANNELS:
        return

    try:
        reaction = f'{{"type": "emoji", "emoji": "{choice(reactions)}"}}'

        # Xabarni tasodifiy reaktsiya qo'shish
        await bot.request(
            method="setMessageReaction",
            data={
                "chat_id": message.chat.id,
                "message_id": message.message_id,
                "reaction": f"[{reaction}]"
            }
        )
    except Exception as e:
        print(f"Error: {e}")
        await bot.send_message(chat_id=ADMINS[0], text=f"Error: {e}")

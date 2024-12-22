import asyncio
from random import choice
from aiogram import types
from aiogram.types import ContentType
from loader import bot, dp
from data.config import ADMINS


import json
CHANNELS = ['Amirjon_Karimov_Blog', 'Amirjon_Karimov_Life']

# Reaktsiyalar ro'yxati
reactions = ["👍", "❤", "🔥", "🥰", "👏", "🎉", "🤩", "👌", "😍", "❤‍🔥", "💯", "🤣", "⚡", "🏆", "🍓", "🍾", "💋", "🎃", "😇", "🤝", "😘"]

# Channel postlarga reaktsiya qo'shish
@dp.channel_post_handler(content_types=ContentType.ANY)
async def reaction(message: types.Message):
    # Kanal username'ini tekshirish
    if message.chat.username not in CHANNELS:
        return
    else:
        with open('channels_info.json','r') as file:
            data = json.load(file)
        data[f"@{message.chat.username}"] = {
            'message_id': message.message_id
        }
        with open('channels_info.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        
    
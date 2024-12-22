from aiogram import executor

from data.config import ADMINS
from loader import dp,db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import asyncio
from random import choice
from datetime import datetime
import json

# CHANNELS = {'@Amirjon_Karimov_Blog':523, '@Amirjon_Karimov_Life':113}
# tugirlandi
reactions = ["👍", "❤", "🔥", "🥰", "👏", "🎉", "🤩", "⚡", "👌", "😍", "❤‍🔥", "💯", "🤣", "🏆", "🍓", "🍾", "💋", "🎃", "😇", "🤝", "😘"]

async def periodic_reaction(dp):
    while True:
        with open('channels_info.json','r') as f:
            data = json.load(f)
        channels = list(data.keys())
        if channels:
            for channel in channels:
                try:
                    reaction = f'{{"type": "emoji", "emoji": "{choice(reactions)}"}}'
                    await dp.bot.request(
                        method="setMessageReaction",
                        data={
                            "chat_id": channel,
                            "message_id": data[channel]['message_id'],
                            "reaction": f"[{reaction}]"
                        }
                    )
                except Exception as e:
                    await dp.bot.send_message(chat_id=ADMINS[0], text=f"Error: {e}")
                    del data[channel]
                    with open('channels_info.json', 'w') as file:
                        json.dump(data, file, indent=4)
                await asyncio.sleep(3)
            
            await asyncio.sleep(23)
        else:
            try:
                reaction = f'{{"type": "emoji", "emoji": "{choice(reactions)}"}}'
                await dp.bot.request(
                    method="setMessageReaction",
                    data={
                        "chat_id": "@Amirjon_Karimov_Blog",
                        "message_id": 500,
                        "reaction": f"[{reaction}]"
                    }
                )
                print(f"bosildi:kanel{channel}:{reaction}")
            except Exception as e:
                await dp.bot.send_message(chat_id=ADMINS[0], text=f"Error: {e}")
            await asyncio.sleep(20)

async def on_startup(dispatcher):
    # Birlamchi komandaPlar (/star va /help)
    await db.create()
    try:
        await db.create_table_channel()
        await db.create_table_admins()
        await db.create_table_files()
    except Exception as err:
          print(err)
    # Get the user ID from the incoming update
    await set_default_commands(dispatcher)
    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    asyncio.create_task(periodic_reaction(dp))

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
    dp.middleware.setup()
    

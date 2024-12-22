from aiogram import executor

from data.config import ADMINS
from loader import dp,db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import asyncio
from random import choice
from datetime import datetime
CHANNELS = {'@Amirjon_Karimov_Blog':523, '@Amirjon_Karimov_Life':113}

# Reaktsiyalar ro'yxati
reactions = ["👍", "❤", "🔥", "🥰", "👏", "🎉", "🤩", "👌", "😍", "❤‍🔥", "💯", "🤣", "⚡", "🏆", "🍓", "🍾", "💋", "🎃", "😇", "🤝", "😘"]

async def periodic_reaction(dp):
    while True:
        for channel,message_id in CHANNELS.items():
            try:
                reaction = f'{{"type": "emoji", "emoji": "{choice(reactions)}"}}'
                reaksiya = await dp.bot.request(
                    method="setMessageReaction",
                    data={
                        "chat_id": channel,
                        "message_id": message_id,
                        "reaction": f"[{reaction}]"
                    }
                )
                print(reaksiya)
                print(f"bosildi:kanel{channel}:{reaction}")
            except Exception as e:
                print(f"Error: {e}:{reaction}")
                await dp.bot.send_message(chat_id=ADMINS[0], text=f"Error: {e}")
            await asyncio.sleep(3)
            
        await asyncio.sleep(23)

        # Har 20 soniyada qayta ishga tushadi

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
    

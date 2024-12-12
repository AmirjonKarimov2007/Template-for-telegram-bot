from aiogram import types

from aiogram.dispatcher.filters import BoundFilter
from loader import db


class IsUser(BoundFilter):
    async def check(self, message: types.Message):
        user_id =message.from_user.id
        user = await db.is_user(user_id=user_id)
        if user:
            return True
        else:
            return False

class IsBlocked(BoundFilter):
    async def check(self, message: types.Message):
        user_id =message.from_user.id
        user = await db.is_user(user_id=user_id)
        if user and (user[0]['is_blocked']==True):
            return True
        else:
            return False
        
class IsGuest(BoundFilter):
    async def check(self, message: types.Message):
        user_id = message.from_user.id
        user = await db.is_user(user_id=user_id)
        if user:
            return False
        else:
            return True

class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )

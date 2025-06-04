from typing import Any
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram import Bot
from aiogram import types
from aiogram.enums import ChatMemberStatus


class SibscriptionMiddleware(BaseMiddleware):
    def __init__(self, bot: Bot, channel_id: str | int) -> None:
        super().__init__()
        self.bot = bot
        self.channel_id = channel_id

    async def __call__(self, handler, event: types.Message, data: dict) -> Any | None:
        message: types.Message = event

        if message.sender_chat is not None:
            return await handler(event, data)

        user_id = message.from_user.id

        if user_id is None:
            return await handler(event, data)

        member = await self.bot.get_chat_member(self.channel_id, user_id=user_id)
        if member.status in (ChatMemberStatus.LEFT, ChatMemberStatus.KICKED):
            await message.delete()
            return
            
        return await handler(event, data) 
from typing import Any
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram import Bot
from aiogram import types
from aiogram.enums import ChatMemberStatus


class SibscriptionMiddleware(BaseMiddleware):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot

    async def __call__(self, handler, event: types.Message, data: dict) -> Any | None:
        message: types.Message = event

        if message.sender_chat is not None:
            return await handler(event, data)

        user_id = message.from_user.id
        
        chat_obj = await message.bot.get_chat(message.chat.id)
        linked_chat_id = chat_obj.linked_chat_id

        member = await self.bot.get_chat_member(linked_chat_id, user_id=user_id)

        if member.status in (ChatMemberStatus.LEFT, ChatMemberStatus.KICKED):
            await message.delete()
            return
            
        return await handler(event, data) 
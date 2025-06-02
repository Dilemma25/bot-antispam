from aiogram import BaseMiddleware
from aiogram import types
from censure.base import Censor
from aiogram import Bot


class ProfanityFilterMIddleware(BaseMiddleware):

    def __init__(self, bot: Bot, channel_id: int | str, censor: Censor):
        super().__init__()
        self.bot = bot
        self.channel_id = channel_id
        self.censor = censor

    async def __call__(self, handler, event: types.Message, data: dict):
        message: types.Message = event
        text = message.text
        print(self.censor.clean_line(text))

            
        return await handler(event, data) 
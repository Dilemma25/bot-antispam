from aiogram import BaseMiddleware
from aiogram import types
from censure.base import Censor
from aiogram import Bot


class ProfanityFilterMIddleware(BaseMiddleware):

    def __init__(self, bot: Bot, censor: Censor):
        super().__init__()
        self.bot = bot
        self.censor = censor

    async def __call__(self, handler, event: types.Message, data: dict):
        message: types.Message = event
        
        if message.text is None:
            return

        if message.sender_chat is not None:
            return await handler(event, data) 

        filter_result = self.censor.clean_line(message.text)#[
                                                            # 0 - line, 
                                                            # 1 - bad_words_count, 
                                                            # 2 - bad_phrases_count, 
                                                            # 3 - detected_bad_words, 
                                                            # 4 - detected_bad_phrases, 
                                                            # 5 - detected_pats
                                                            #]

        profanity_words_count = filter_result[1]
        profanity_phrases_count = filter_result[2]
        
        if profanity_words_count > 0 or profanity_phrases_count > 0:
            await message.delete()
            return
            
        return await handler(event, data) 
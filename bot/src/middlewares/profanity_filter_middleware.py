from aiogram import BaseMiddleware
from aiogram import types
from censure.base import Censor
from aiogram import Bot
import string

class ProfanityFilterMIddleware(BaseMiddleware):

    def __init__(self, bot: Bot, censor: Censor, local_bad_phrases: list[str]):
        super().__init__()
        self.bot = bot
        self.censor = censor
        self.local_bad_phrases = local_bad_phrases

    def check_exist_bad_phrases(self, message_text: str) -> bool:
        table = str.maketrans('', '', string.punctuation)
        message_text = message_text.translate(table).lower()
        
        if message_text.strip() in self.local_bad_phrases:
            return True

        for phrase in self.local_bad_phrases:
            message_words = message_text.split()
            message_words_set = set(message_words)

            phrase_words = phrase.split()
            phrase_words_set = set(phrase_words)
        
            common_words = message_words_set.intersection(phrase_words_set)

            common_count = len(common_words)

            phrase_ratio = common_count / len(phrase_words) if phrase_words else 0
            message_ratio = common_count / len(message_words) if message_words else 0

            if phrase_ratio >= 0.6 and message_ratio >= 0.6:
                return True

        return False

    async def __call__(self, handler, event: types.Message, data: dict):
        message: types.Message = event

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

        print(filter_result)

        profanity_words_count = filter_result[1]
        profanity_phrases_count = filter_result[2]
        
        if profanity_words_count > 0 or profanity_phrases_count > 0 or self.check_exist_bad_phrases(message.text):
            await message.delete()
            return

        return await handler(event, data) 
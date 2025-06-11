from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.debug_print_handler import debug_router
import settings
from censure.base import Censor
from middlewares.sibscription_middleware import SibscriptionMiddleware
from middlewares.profanity_filter_middleware import ProfanityFilterMIddleware 
import os


def load_bad_phrases():
    list = []
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "local_bad_phrases.txt")

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            list.append(line)
            
    return list

dp = Dispatcher()

bot = Bot(
          token=settings.TOKEN, 
          default=DefaultBotProperties(parse_mode=ParseMode.HTML)
          )


dp.message.middleware(SibscriptionMiddleware(
                                             bot=bot, 
                                            ))

local_bad_phrases = load_bad_phrases()

censor_ru = Censor.get(lang='ru')
dp.message.middleware(ProfanityFilterMIddleware(
                                                bot=bot, 
                                                censor=censor_ru,
                                                local_bad_phrases=local_bad_phrases
                                                ))

dp.include_router(debug_router)
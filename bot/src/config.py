from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from middlewares.sibscription_middleware import SibscriptionMiddleware
from handlers.debug_print_handler import debug_router
import redis.asyncio as redis
import settings
from censure.base import Censor
from middlewares.profanity_filter_middleware import ProfanityFilterMIddleware 
from middlewares.anti_flood_middleware import AntiFloodMiddleware
from constats import MAX_MESSAGES
from constats import INTERVAL

redis_client = redis.Redis(
                           host=settings.REDIS_HOST, 
                           port=settings.REDIS_PORT, 
                           db=settings.REDIS_DB
                           )

dp = Dispatcher()
bot = Bot(
          token=settings.TOKEN, 
          default=DefaultBotProperties(parse_mode=ParseMode.HTML)
          )


dp.message.middleware(SibscriptionMiddleware(
                                             bot=bot, 
                                            ))

censor_ru = Censor.get(lang='ru')
dp.message.middleware(ProfanityFilterMIddleware(
                                                bot=bot, 
                                                censor=censor_ru
                                                ))

dp.message.middleware(AntiFloodMiddleware(
                                          redis=redis_client, 
                                          bot=bot, 
                                          max_messages=MAX_MESSAGES, 
                                          interval=INTERVAL
                                          ))

dp.include_router(debug_router)
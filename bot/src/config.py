from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from middlewares.sibscription_middleware import SibscriptionMiddleware
from handlers.find_location_dev import debug_router
import redis.asyncio as redis
import settings
from censure.base import Censor
from middlewares.profanity_filter_middleware import ProfanityFilterMIddleware 

redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

dp = Dispatcher()
bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


dp.message.middleware(SibscriptionMiddleware(bot=bot, channel_id=settings.CHANNEL_ID))

censor_ru = Censor.get(lang='ru')
dp.message.middleware(ProfanityFilterMIddleware(bot=bot, channel_id=settings.CHANNEL_ID, censor=censor_ru))

dp.include_router(debug_router)
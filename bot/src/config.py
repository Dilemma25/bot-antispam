from os import getenv
from dotenv import load_dotenv
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from middlewares.sibscription_middleware import SibscriptionMiddleware
from handlers.find_location_dev import debug_router

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

CHANNEL_ID = getenv('CHANNEL_ID')
dp.message.middleware(SibscriptionMiddleware(bot=bot, channel_id=CHANNEL_ID))


dp.include_router(debug_router)
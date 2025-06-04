from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv('BOT_TOKEN')


REDIS_HOST = getenv('REDIS_HOST')
REDIS_PORT = getenv('REDIS_PORT')
REDIS_DB = getenv('REDIS_DB')
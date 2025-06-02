import asyncio
import logging
import sys
from config import dp
from config import bot
from config import redis_client


async def main() -> None:
    # await redis_client.rpush("my-item", "value1")
    # await redis_client.rpush("my-item", "value2")
    # value = await redis_client.lrange("my-item", 0, -1)
    # print(value)
    await dp.start_polling(bot)

    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
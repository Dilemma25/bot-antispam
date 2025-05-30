import asyncio
import logging
import sys
from config import dp
from config import bot
from config import redis_client


async def main() -> None:
    await redis_client.set("my-key", "value")
    value = await redis_client.get("my-key")
    print(value)
    await dp.start_polling(bot)

    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
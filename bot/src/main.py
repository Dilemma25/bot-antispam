import asyncio
import logging
import sys
from config import dp
from config import bot

#сделать подсчет сообщений для каждого пользователя в мидлвеерах на пропверку подписки и матов
#сделать бан при спаме
#сделать номральынй docker-c0mpose
async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
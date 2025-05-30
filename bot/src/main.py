import asyncio
import logging
import sys
from aiogram.filters import CommandStart
from aiogram import types

from config import dp
from config import bot

# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receives messages with `/start` command
#     """
#     await message.answer(f"Hello, {message.from_user.full_name}!")

# @dp.message()
# async def debug_all_messages(message: types.Message):
#     logging.info(f"Получено сообщение: type={message.content_type}, from={message.from_user.full_name}, text={message.text}")

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
from aiogram.filters import Command
from aiogram import types
import logging
from aiogram import Router


debug_router = Router()

@debug_router.message()
async def debug_all_messages(message: types.Message):
    logging.info(
                 f"Получено сообщение: type={message.content_type}, \
                 from={message.from_user.full_name, message.from_user.id}, \
                 text={message.text}"
                )
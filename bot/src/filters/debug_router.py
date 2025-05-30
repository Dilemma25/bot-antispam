from constats import BLOCKED_CONTENT
from aiogram import types
from aiogram import Router 
from aiogram.enums import ChatType
from aiogram import F
import logging

sibscriber_router = Router()

# @sibscriber_router.message()
# async def media_filter(message: types.Message):
#     try:
#         await message.delete()
#         logging.info(
#             f"Удалено сообщение типа {message.content_type} от юзера @{message.from_user.username} \
#             (ID: {message.from_user.id})"
#         )
#     except Exception as e:
#         logging.error(f"Ошибка при удалении: {e}")

from aiogram import BaseMiddleware
from redis.asyncio import Redis
from aiogram import types
from aiogram import Bot
import time


class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, redis: Redis, bot: Bot, channel_id: int | str, max_messages: int = 5, interval: int = 10) -> None:
        super().__init__()
        self.redis = redis
        self.bot = bot
        self.channel_id = channel_id
        self.max_messages = max_messages
        self.interval = interval
    
    async def __delete_message_per_user(self, msg_times: dict[str, int]):
        for mid in msg_times:
            try:
                chat_id, message_id = mid.split(":")
                await self.bot.delete_message(chat_id, message_id)
            except Exception as error:
                print(error)
            return  

    async def __call__(self, handler, event, data):
        if not isinstance(event, types.Message) or event.from_user is None:
            return handler(event, data)
        
        message: types.Message = event
        user_id = message.from_user.id

        now = int(time.time())

        key = f"antiflood:{user_id}"
        msg_ids_key = f"{key}:msgs"

        field = f"{message.chat.id}:{message.message_id}"

        pipe = self.redis.pipeline()

        # 1. Сохраняем message_id в хэш с временной меткой
        await pipe.hset(msg_ids_key, field, now)

        # 2. Очищаем старые message_id
        # Получим весь хэш
        await pipe.hgetall(msg_ids_key)

        # 3. Работаем с количеством сообщений
        await pipe.zadd(key, {field: now})
        await pipe.zremrangebyscore(key, 0, now - self.interval)
        await pipe.zcard(key)
        await pipe.expire(key, self.interval + 5)
        await pipe.expire(msg_ids_key, self.interval + 5)

        # Выполняем и извлекаем данные
        _, all_msgs, _, _, message_count, _, _ = await pipe.execute()

        # Преобразуем all_msgs в словарь: {message_id: timestamp}
        msg_times: dict[str, int] = {
            mid.decode(): int(ts.decode())
            for mid, ts in all_msgs.items()
        }
        # Удалим старые message_id
        for mid, ts in msg_times.items():
            if ts < now - self.interval:
                await self.redis.hdel(msg_ids_key, mid)

        if message_count > self.max_messages:
            print(msg_times)
            # Удаляем все сообщения этого юзера за период
            for mid in msg_times:
                try:
                    chat_id, message_id = mid.split(":")
                    await self.bot.delete_message(chat_id, message_id)
                except Exception as error:
                    print(error)
            return  # Не передаём дальше
        
        return await handler(event, data)

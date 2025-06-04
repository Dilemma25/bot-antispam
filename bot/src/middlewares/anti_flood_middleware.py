from aiogram import BaseMiddleware
from redis.asyncio import Redis


class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, redis: Redis, max_messages: int = 5, interval: int = 10) -> None:
        super().__init__()
        self.redis = redis
        self.max_messages = max_messages
        self.interval = interval

    async def __call__(self, handler, event, data):
        
        
        
        return await handler(event, data)

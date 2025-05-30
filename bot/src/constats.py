from aiogram.enums import ContentType

BLOCKED_CONTENT = {
    ContentType.PHOTO,
    ContentType.VIDEO,
    ContentType.ANIMATION,  # GIF
    ContentType.STICKER,
    ContentType.DOCUMENT,
    ContentType.VOICE,
    ContentType.AUDIO
}
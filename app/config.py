import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    BOT_TOKEN: str
    POLL_TIMEOUT: int = 30


def get_settings() -> Settings:
    bot_token = os.getenv("TG_BOT_TOKEN")

    if not bot_token:
        raise ValueError(
            "Переменная окружения TG_BOT_TOKEN не найдена. "
            "Добавь её в .env файл."
        )

    return Settings(BOT_TOKEN=bot_token)


settings = get_settings()


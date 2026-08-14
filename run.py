import time

from app.config import settings
from app.handlers import handle_update
from app.telegram_api import get_updates


def main():
    print("Бот запущен...")
    offset = None

    while True:
        try:
            updates = get_updates(
                token=settings.BOT_TOKEN,
                offset=offset,
                timeout=settings.POLL_TIMEOUT,
            )

            for update in updates:
                offset = update["update_id"] + 1
                handle_update(update, settings.BOT_TOKEN)

        except Exception as error:
            print(f"Ошибка: {error}")
            time.sleep(5)


if __name__ == "__main__":
    main()

    
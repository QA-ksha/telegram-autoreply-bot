import random

from app.telegram_api import send_message


AUTO_REPLIES = [
    "Привет! Я сейчас занят, отвечу позже.",
    "Спасибо за сообщение. Увидел 👌 передам!",
    "Получил сообщение. Напишу чуть позже.",
    "Я в режиме автоответчика 🙂",
]

START_TEXT = (
    "Привет! Я бот-автоответчик.\n"
    "Напиши мне любое текстовое сообщение, и я отвечу одной из заготовленных фраз."
)


def handle_update(update: dict, token: str):
    message = update.get("message")

    if not message:
        return

    handle_message(message, token)


def handle_message(message: dict, token: str):
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    text = message.get("text", "").strip()

    if not chat_id:
        return

    if text == "/start":
        send_message(token, chat_id, START_TEXT)
        return

    if not text:
        send_message(token, chat_id, "Я пока умею отвечать только на текстовые сообщения.")
        return

    reply_text = random.choice(AUTO_REPLIES)
    send_message(token, chat_id, reply_text)

    
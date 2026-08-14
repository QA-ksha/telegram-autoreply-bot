import requests


BASE_URL = "https://api.telegram.org/bot{token}/{method}"


def build_url(token: str, method: str) -> str:
    return BASE_URL.format(token=token, method=method)


def get_updates(token: str, offset=None, timeout: int = 30):
    params = {"timeout": timeout}

    if offset is not None:
        params["offset"] = offset

    response = requests.get(
        build_url(token, "getUpdates"),
        params=params,
        timeout=timeout + 5,
    )
    response.raise_for_status()

    data = response.json()
    return data.get("result", [])


def send_message(token: str, chat_id: int, text: str):
    response = requests.post(
        build_url(token, "sendMessage"),
        data={
            "chat_id": chat_id,
            "text": text,
        },
        timeout=15,
    )
    response.raise_for_status()
    return response.json()


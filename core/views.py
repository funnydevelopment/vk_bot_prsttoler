import os

import httpx

from core import text_messages as texts


def create_post() -> None:
    access_token = os.getenv("ACCESS_TOKEN")
    owner_id = os.getenv("OWNER_ID")
    message = texts.MESSAGE_TEXT
    params = {
        "access_token": access_token,
        "owner_id": owner_id,
        "message": message,
        "v": "5.131",
    }
    url = "https://api.vk.com/method/wall.post"
    code = os.getenv("CODE")
    response = httpx.post(url, params=params)
    result = response.json()
    print(result)

import os

import httpx

from core import text_messages as texts


def create_post() -> None:
    access_token = os.getenv("ACCESS_TOKEN")
    owner_id = int(os.getenv("OWNER_ID"))
    from_group = 0
    message = texts.MESSAGE_TEXT
    version = "5.131"
    params = {
        "access_token": access_token,
        "owner_id": owner_id,
        "from_group": from_group,
        "message": message,
        "v": version,
    }
    url = "https://api.vk.com/method/wall.post"
    code = os.getenv("CODE")
    response = httpx.post(url, params=params)
    result = response.json()
    print(result)

import os
import time

import httpx

import texts


def create_post(vk_group_id: int) -> None:
    try:
        access_token = os.getenv("ACCESS_TOKEN")
        owner_id = vk_group_id
        from_group = 0
        message = texts.MESSAGE_TEXT
        attachment = ""
        version = "5.131"
        params = {
            "access_token": access_token,
            "owner_id": owner_id,
            "from_group": from_group,
            "message": message,
            "attachments": attachment,
            "v": version,
        }
        url = "https://api.vk.com/method/wall.post"
        response = httpx.post(url, params=params)
        result = response.json()
        print(result)
    except Exception as error:
        print(f"Произошла ошибка {error}")
    time.sleep(60)

import httpx

from core import text_messages as text

# todo: посмотреть vk api как отправлять письма в группы
# todo: бот должен работать непрерывно С 6 утра до 12 и с 14 до 00:00
# todo: бот должен отправлять сообщения в группы с интервалом 2-3 минут, каждый час
# todo: посмотреть какие группы бывают в VK и отличаются ли они при отправке поста


# https://api.vk.com/method/wall.post?access_token=ВАШ_ТОКЕН&owner_id=-ГРУППА_ID&message=Ваш текст для записи


access_token = "vk1.a.PKu9_6O1uHxXqetwo6foONDovSijpvYhwPt7vKNeljhdJjZi4nkkUt2M7ywEZj3l0MfxQLvxq36DbtgYc5VURQVu-bN8gsaD3N9wllNvjOqgnrRCTO6P86DCQA1c4YuVN4yek9Pyn33gWtq302qzCXq0vWqioXpWOzluHorf34dVLpTT-NhxPn9iR2fVM9M4gjeh62bAc3GDLQtNg3mLrw"

owner_id = "-222553253"

message = text.MESSAGE_TEXT

params = {
    "access_token": access_token,
    "owner_id": owner_id,
    "message": message,
    "v": "5.131"
}

url = "https://api.vk.com/method/wall.post"

code = "700bb9d2216f20642d"

response = httpx.post(url, params=params)

result = response.json()

print(result)

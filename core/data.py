import os


def upload_photos():
    photo_1, photo_2, photo_3 = (
        int(os.getenv("MEDIA_ID_1")),
        int(os.getenv("MEDIA_ID_2")),
        int(os.getenv("MEDIA_ID_3")),
    )
    pass


def get_group_id() -> list:
    id_list = []
    for i in range(1, 14):
        group_id = os.getenv(f"VK_GROUP_ID_{i}")
        id_list.append(int(group_id))
    return id_list

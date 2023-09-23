from dotenv import load_dotenv

from core.views import create_post
from core.data import get_group_id


def run_app():
    load_dotenv(".env")
    vk_groups_id = get_group_id()
    for vk_group_id in vk_groups_id:
        create_post(vk_group_id)


if __name__ == "__main__":
    run_app()

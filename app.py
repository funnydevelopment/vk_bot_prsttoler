import time
from datetime import datetime, timedelta

import pytz
import schedule
from dotenv import load_dotenv

from core.views import create_post
from core.data import get_group_id


timezone_7 = pytz.timezone("Europe/Istanbul")


def run_app():
    load_dotenv(".env")
    vk_groups_id = get_group_id()
    for vk_group_id in vk_groups_id:
        create_post(vk_group_id)


def job():
    now = datetime.now(timezone_7)
    print(now)
    if (9 <= now.hour <= 12) or (20 <= now.hour <= 24):
        run_app()


schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

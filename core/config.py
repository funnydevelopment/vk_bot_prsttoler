from dotenv import load_dotenv


def get_dotenv() -> None:
    load_dotenv("../.env")

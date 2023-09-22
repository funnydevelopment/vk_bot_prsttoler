from dotenv import load_dotenv

from core.views import create_post


def run_app():
    load_dotenv(".env")
    create_post()


if __name__ == "__main__":
    run_app()

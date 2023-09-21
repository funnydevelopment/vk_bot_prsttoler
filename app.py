from core.config import get_dotenv
from core.views import create_post


def run_app():
    get_dotenv()
    create_post()


if __name__ == "__main__":
    run_app()

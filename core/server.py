import os

from flask import Flask, request
import httpx

import text_messages as texts


app = Flask(__name__)


@app.route("/")
def get_code() -> str:
    code = request.args.get("code")
    result = get_access_token(code)
    print(result)
    return f"Значение параметра: {code}"


def get_access_token(code: str) -> str:
    client_id = os.getenv("CLIENT_ID")
    redirect_url = os.getenv("REDIRECT_URL")
    client_secret_key = os.getenv("CLIENT_SECRET_KEY")
    get_token_url = texts.GET_TOKEN_URL.format(
        client_id=client_id,
        client_secret_key=client_secret_key,
        redirect_url=redirect_url,
        code=code,
    )
    response = httpx.get(get_token_url)
    result = response.json()
    print(response.status_code)
    print(result)
    return result["access_token"]

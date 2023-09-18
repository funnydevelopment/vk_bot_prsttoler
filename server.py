from flask import Flask, request
import httpx


app = Flask(__name__)


@app.route("/")
def get_code():
    code = request.args.get('code')
    result = get_access_token(code)
    print(result)
    return f'Значение параметра: {code}'


def get_access_token(code: str) -> str:
    client_id = 51752056
    redirect_url = "https://chayan.ecorp.fun"
    client_secret = "C39V00XC0UyQ2NQUmteI"
    get_token_url = f"https://oauth.vk.com/access_token?client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_url}&code={code}"
    response = httpx.get(get_token_url)
    result = response.json()
    print(response.status_code)
    print(result)
    return result["access_token"]


import random
import string
import json
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic_core import Url

app = FastAPI()
data = dict()

try:
    with open("links.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("No existing links found. Starting fresh!")
    data = {}


def randstring():
    a = ''
    for i in range(random.randint(5, 7)):
        a += random.choice(string.ascii_letters + string.digits)
    return a


@app.post("/shorten")
async def shorten(url: Url):
    a = randstring()
    data[a] = str(url)

    # Saving data
    with open("links.json", "w") as g:
        json.dump(data, g)

    return {"url": a}

@app.get("/{short_id}")
async def redirect(short_id: str):
    url = data.get(short_id)
    if not url:
        return {"error": "Link not found"}
    else:
        return RedirectResponse(url)




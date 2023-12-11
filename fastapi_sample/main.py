from typing import Union

from fastapi import FastAPI

import a2wsgi

app = FastAPI()


@app.get("/")
def read_root():
    #return {"Hello": "World"}
    return "hoge"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

wsgi_app = a2wsgi.ASGIMiddleware(app)


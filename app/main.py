from fastapi import FastAPI
from db import init_db, add_feed, get_feeds, get_articles
from aggregator import fetch_articles

app = FastAPI()
init_db()

@app.get("/")
def home():
    return {"feeds": get_feeds()}

@app.get("/add")
def add(input: str):
    add_feed(input)
    return {"msg": "added"}

@app.get("/rss/{biz}")
def rss(biz: str):
    articles = get_articles(biz)
    from rss import generate_rss
    return generate_rss(articles, biz)

@app.get("/update")
def update():
    for biz in get_feeds():
        fetch_articles(biz)
    return {"msg": "updated"}
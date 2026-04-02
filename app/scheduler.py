from apscheduler.schedulers.background import BackgroundScheduler
from aggregator import fetch_articles
from db import get_feeds

def start():
    s = BackgroundScheduler()
    s.add_job(lambda: [fetch_articles(b) for b in get_feeds()], "interval", minutes=20)
    s.start()
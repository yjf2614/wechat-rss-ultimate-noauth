import requests
from parser import parse_rss, parse_sogou
from utils import safe_get
from db import save_article
from content import fetch_full


def fetch_from_rsshub(biz):
    url = f"https://rsshub.app/wechat/mp/{biz}"
    resp = safe_get(url)

    if not resp:
        return []

    return parse_rss(resp.text)


def fetch_from_sogou(keyword):
    url = f"https://weixin.sogou.com/weixin?type=2&query={keyword}"
    resp = safe_get(url)

    if not resp:
        return []

    return parse_sogou(resp.text)


def fetch_articles(biz):
    articles = []

    # 🥇 RSSHub 优先
    rss_articles = fetch_from_rsshub(biz)
    if rss_articles:
        articles = rss_articles

    # 🥈 fallback：Sogou
    if not articles:
        articles = fetch_from_sogou(biz)

    # 👉 保存 + 抓全文
    for a in articles:
        try:
            content = fetch_full(a["link"])

            save_article(biz, {
                "title": a["title"],
                "link": a["link"],
                "content": content,
                "pub_date": ""
            })
        except:
            continue

    return articles
import sqlite3

conn = sqlite3.connect("data/rss.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feeds (biz TEXT PRIMARY KEY)
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        biz TEXT,
        title TEXT,
        link TEXT UNIQUE,
        content TEXT,
        pub_date TEXT
    )
    """)
    conn.commit()

def add_feed(biz):
    cursor.execute("INSERT OR IGNORE INTO feeds VALUES (?)", (biz,))
    conn.commit()

def get_feeds():
    return [x[0] for x in cursor.execute("SELECT biz FROM feeds")]

def save_article(biz, a):
    try:
        cursor.execute(
            "INSERT INTO articles (biz,title,link,content,pub_date) VALUES (?,?,?,?,?)",
            (biz, a["title"], a["link"], a["content"], a["pub_date"])
        )
        conn.commit()
    except:
        pass

def get_articles(biz):
    return cursor.execute(
        "SELECT title,link,content,pub_date FROM articles WHERE biz=? ORDER BY id DESC LIMIT 20",
        (biz,)
    ).fetchall()
import random
import time
import requests

UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/119",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/118",
]

def get_headers():
    return {
        "User-Agent": random.choice(UA_LIST)
    }


def random_delay(a=2, b=5):
    time.sleep(random.uniform(a, b))


def safe_get(url, timeout=10):
    for _ in range(3):
        try:
            random_delay()
            return requests.get(url, headers=get_headers(), timeout=timeout)
        except:
            time.sleep(2)
    return None

import redis
import json
from flask import current_app

r = None

def init_redis():
    global r
    try:
        r = redis.Redis.from_url(current_app.config['REDIS_URL'])
        r.ping()
    except:
        r = None

def get_books_cache():
    try:
        data = r.get("books") if r else None
        return json.loads(data) if data else None
    except:
        return None

def set_books_cache(data):
    try:
        if r:
            r.set("books", json.dumps(data))
    except:
        pass

from app.cache import get_books_cache, set_books_cache
import fakeredis

def test_cache_miss_and_hit_behavior(monkeypatch):
    fake_r = fakeredis.FakeRedis()
    monkeypatch.setattr("app.cache.r", fake_r)

    assert get_books_cache() is None  # cache miss

    books_data = [{"id": 1, "title": "Some Book"}]
    set_books_cache(books_data)

    cached = get_books_cache()
    assert cached == books_data  # cache hit

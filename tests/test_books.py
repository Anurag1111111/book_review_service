
import requests

BASE_URL = "http://localhost:5000"

def test_create_book():
    res = requests.post(f"{BASE_URL}/books", json={"title": "Flask Book"})
    assert res.status_code == 200
    assert res.json()["title"] == "Flask Book"

def test_list_books():
    res = requests.get(f"{BASE_URL}/books")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_post_review():
    # Create a book
    book_res = requests.post(f"{BASE_URL}/books", json={"title": "Test Review Book"})
    assert book_res.status_code == 200
    book_id = book_res.json()["id"]

    # Post a review to that book
    review_res = requests.post(f"{BASE_URL}/book/{book_id}/reviews", json={"content": "Great book!"})
    assert review_res.status_code == 200
    assert review_res.json()["content"] == "Great book!"

def test_get_reviews():
    # Create a book and post a review
    book_res = requests.post(f"{BASE_URL}/books", json={"title": "Another Review Book"})
    assert book_res.status_code == 200
    book_id = book_res.json()["id"]

    review_res = requests.post(f"{BASE_URL}/book/{book_id}/reviews", json={"content": "Awesome read!"})
    assert review_res.status_code == 200

    # Fetch the reviews
    get_res = requests.get(f"{BASE_URL}/book/{book_id}/reviews")
    assert get_res.status_code == 200
    data = get_res.json()
    assert isinstance(data, list)
    assert any(r["content"] == "Awesome read!" for r in data)

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_create_post():
    payload = {
        "title": "Test Post",
        "content": "This is a test post",
        "published": True
    }
    response = client.post("/posts", json=payload)
    assert response.status_code == 201
    res_json = response.json()
    assert "data" in res_json
    created_post = res_json["data"]
    assert created_post["title"] == payload["title"]
    assert created_post["content"] == payload["content"]
    assert created_post["published"] == payload["published"]
    assert "id" in created_post
    assert isinstance(created_post["id"], int)


def test_get_post_by_id():
    response = client.get("/posts/2")
    assert response.status_code == 200
    assert response.json() == {
        "post_detail": {
            "title": "title of post 2",
            "content": "content of post 2",
            "id": 2
        }
    }


def test_delete_post_success():
    payload = {
        "title": "Post to delete",
        "content": "This post will be deleted",
        "published": True
    }
    create_response = client.post("/posts", json=payload)
    assert create_response.status_code == 201
    post_id = create_response.json()["data"]["id"]
    delete_response = client.delete(f"/posts/{post_id}")
    assert delete_response.status_code == 204
    assert delete_response.content == b""


def test_update_post():
    payload = {
        "title": "Updated Title",
        "content": "Updated content",
        "published": True
    }
    response = client.put("/posts/1", json=payload)
    assert response.status_code == 200
    res_json = response.json()
    assert "data" in res_json
    updated_post = res_json["data"]
    assert updated_post["id"] == 1
    assert updated_post["title"] == payload["title"]
    assert updated_post["content"] == payload["content"]
    assert updated_post["published"] == payload["published"]

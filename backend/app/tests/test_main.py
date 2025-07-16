# from fastapi.testclient import TestClient
# from backend.app.main import app

# client = TestClient(app)


# # Test Home Page GET Method "/"
# def test_root():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Welcome to my API"}


# # Test GET Method for Retrieving "id": 2
# def test_posts():
#     response = client.get("/posts/2")
#     assert response.status_code == 200
#     assert response.json() == {
#         "post_detail": {
#             "title": "title of post 2",
#             "content": "content of post 2",
#             "id": 2
#         }
#     }

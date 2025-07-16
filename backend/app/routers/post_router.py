from fastapi import APIRouter, status, HTTPException, Response
from random import randrange
from backend.app.schemas.post_schema import Post
from backend.app.helpers import find_post, find_index_post
from backend.app.data import my_posts

post_router = APIRouter()


@post_router.get("/posts")
def get_posts():
    return {"data": my_posts}


# .model_dump replaces .dict (converts to dictionary)
@post_router.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@post_router.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
            )
    return {"post_detail": post}


@post_router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
            )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@post_router.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
            )
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'data': 'post_dict'}

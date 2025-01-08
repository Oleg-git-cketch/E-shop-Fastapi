from db.productservice import *
from api import result_message
from fastapi import APIRouter


like_router = APIRouter(prefix='/like', tags=["Лайки"])

"""
Comment likes
"""

@like_router.post('/add_like_to_comment')
async def add_like_comment(user_id, comment_id):
    result = add_like_to_comment_db(user_id=user_id, comment_id=comment_id)
    return result_message(result)

@like_router.get('/get_likes_comment')
async def get_like_comment(comment_id):
    result = get_likes_by_comment_db(comment_id=comment_id)
    return result_message(result)

@like_router.delete('/delete_like_comment')
async def delete_like_comment(user_id, comment_id):
    result = delete_like_by_comment_db(user_id=user_id, comment_id=comment_id)
    return result_message(result)


"""
Product likes
"""

@like_router.post('/add_like_to_product')
async def add_like_product(user_id, pr_id):
    result = add_like_to_product_db(user_id=user_id, pr_id=pr_id)
    return result_message(result)

@like_router.get('/get_likes_product')
async def get_like_product(pr_id):
    result = get_likes_by_product_db(pr_id=pr_id)
    return result_message(result)

@like_router.delete('/delete_like_product')
async def delete_like_product(user_id, pr_id):
    result = delete_like_by_product_db(user_id=user_id, pr_id=pr_id)
    return result_message(result)

from db.productservice import *
from api import result_message
from fastapi import APIRouter

comments_router = APIRouter(prefix='/comment', tags=["Комменты"])


@comments_router.post('/add_comment')
async def add_comment(user_id, product_id, text):
    result = add_comment_db(user_id, product_id, text)
    return result_message(result)

@comments_router.get('/get_comment')
async def get_comment(comment_id):
    result = get_comment_db(comment_id)
    return result_message(result)

@comments_router.post('/update_comment')
async def update_comment(comment_id, new_info):
    result = update_comment_db(comment_id, new_info)
    return result_message(result)

@comments_router.delete('/delete_comment')
async def delete_comment(comment_id):
    result = delete_comment_db(comment_id)
    return result_message(result)
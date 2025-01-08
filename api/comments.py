from db.productservice import *
from api import result_message
from fastapi import APIRouter

comments_router = APIRouter(prefix='/comment', tags=["Комменты"])


@comments_router.post('/add_comment')
async def add_comment(user_id, product_id, text):
    result = add_comment_db(user_id, product_id, text)
    return result_message(result)

@comments_router.get('/get_all_comments')
async def get_all_comments(comment_id):
    result = get_all_comments_db(comment_id)
    return result_message(result)

@comments_router.get('get_exact_comment_by_post')
async def get_exact_comment_by_post(post_id):
    result = get_exact_comment_by_post(post_id)
    return result_message(result)

@comments_router.get('/get_exact_comment')
async def get_exact_comment(comment_id):
    result = get_exact_comment_db(comment_id)
    result_message(result)

@comments_router.post('/update_comment')
async def update_comment(comment_id, new_info):
    result = update_comment_db(comment_id, new_info)
    return result_message(result)

@comments_router.delete('/delete_comment')
async def delete_comment(comment_id):
    result = delete_comment_db(comment_id)
    return result_message(result)
from api import result_message
from db.productservice import *
from fastapi import APIRouter

category_router = APIRouter(prefix='/category', tags=["Категории"])


@category_router.post('/add_category')
async def add_category(name, description):
    result = create_category_db(name, description)
    return result_message(result)

@category_router.get('/get_category')
async def get_category(category_id):
    result = get_categories_db(category_id)
    return result_message(result)

@category_router.post('/update_category')
async def update_category(category_id, change_info, new_info):
    result = update_category_db(category_id, change_info, new_info)
    return result_message(result)

@category_router.delete('/delete_category')
async def delete_category(category_id):
    result = delete_category_db(category_id)
    return result_message(result)
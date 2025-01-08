from db.productservice import *
from pydantic import BaseModel
from api import result_message
from fastapi import APIRouter

product_router = APIRouter(prefix='/product', tags=["Продукты"])

class ProductModel(BaseModel):
    user_id: int
    pr_name: str
    pr_description: str
    pr_price: float
    pr_quantity: int
    category_id: int

@product_router.post('/add_product')
async def add_product(pr_data: ProductModel):
    pr_dict = dict(pr_data)
    result = add_product_db(**pr_dict)
    return result_message(result)

@product_router.get('/get_all_products')
async def get_all_products(pr_id):
    result = get_all_product_db(pr_id)
    return result_message(result)

@product_router.get('/get_exact_product')
async def get_exact_product(pr_id):
    result = get_exact_product_db(pr_id)
    return result_message(result)

@product_router.post('/update_product')
async def update_product(pr_id, change_info, new_info):
    result = update_product_db(pr_id, change_info, new_info)
    return result_message(result)

@product_router.delete('/delete_product')
async def delete_product(pr_id):
    result = delete_product_db(pr_id)
    return result_message(result)

# @product_router.post('/add_like_to_product')
# async def add_like_comment(user_id, comment_id):
#     result = add_like_to_comment_db(user_id=user_id, comment_id=comment_id)
#     return result_message(result)
#
# @product_router.get('/get_likes_product')
# async def get_like_comment(comment_id):
#     result = get_likes_by_comment_db(comment_id=comment_id)
#     return result_message(result)
#
# @product_router.delete('/delete_like_product')
# async def delete_like_comment(user_id, comment_id):
#     result = delete_like_by_comment_db(user_id=user_id, comment_id=comment_id)
#     return result_message(result)

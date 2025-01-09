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
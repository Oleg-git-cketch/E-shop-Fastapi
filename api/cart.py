from db.productservice import *
from api import result_message
from fastapi import APIRouter


cart_router = APIRouter(prefix='/cart', tags=["Корзина"])

@cart_router.post('/add_to_cart')
async def add_to_cart(user_id, pr_id, quantity: int):
    result = add_to_cart_db(user_id=user_id, pr_id=pr_id, quantity=quantity)
    return result_message(result)

@cart_router.get('/get_pr_in_cart')
async def get_cart(user_id: int):
    result = get_cart_by_user_db(user_id=user_id)
    return result_message(result)

@cart_router.delete('/delete_user_cart')
async def delete_user_cart(user_id):
    result = clear_cart_db(user_id)
    return result_message(result)

@cart_router.delete('/delete_exact_pr_in_cart')
async def delete_exact_cart(cart_item_id):
    result = delete_from_cart_db(cart_item_id=cart_item_id)
    return result_message(result)


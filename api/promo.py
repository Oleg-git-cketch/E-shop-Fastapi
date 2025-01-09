from . import result_message
from db.productservice import *
from fastapi import APIRouter


promo_router = APIRouter(prefix='/promo', tags=["Промокоды"])


@promo_router.post('/add_promo')
async def add_promo(code, amount, min_order_value):
    result = create_promo_code_db(code, amount, min_order_value)
    return result_message(result)

@promo_router.get('/get_promo')
async def get_promo(code):
    result = get_promo_code_db(code)
    return result_message(result)

@promo_router.post('/update_promo')
async def update_promo(code, change_info, new_info):
    result = update_promo_code_db(code, change_info, new_info)
    return result_message(result)

@promo_router.delete('/delete_promo')
async def delete_promo(code):
    result = delete_promo_code(code)
    return result_message(result)
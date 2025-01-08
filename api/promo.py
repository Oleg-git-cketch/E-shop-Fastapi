from . import result_message
from .bot import send_order_to_telegram
from db.productservice import *
from fastapi import APIRouter


promo_router = APIRouter(prefix='/promo', tags=["Промокод"])


@promo_router.post('/add_promo')
async def add_promo(code, amount, min_order_value):
    result = create_promo_code_db(code, amount, min_order_value)
    return result_message(result)
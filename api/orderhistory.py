from api import result_message
from db.productservice import *
from fastapi import APIRouter

history_router = APIRouter(prefix='/history', tags=["История Покупок"])


@history_router.get('/purchase_history')
async def get_purchase_history(user_id):
    result = get_purchase_history_db(user_id)
    return result_message(result)

@history_router.delete('/delete_order')
async def delete_order(order_id):
    result = delete_history_db(order_id=order_id)
    return result_message(result)

@history_router.delete('/delete_all_history')
async def delete_all_history(user_id):
    result = clear_purchase_history_db(user_id)
    return result_message(result)
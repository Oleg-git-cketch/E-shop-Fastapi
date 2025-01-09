from .bot import send_order_to_telegram
from db.productservice import *
from fastapi import APIRouter


buy_router = APIRouter(prefix='/buy', tags=["Покупка"])


@buy_router.post('/buy_products')
async def order(user_id: int, promo_code: str = None):
    cart_items = get_cart_by_user_db(user_id)

    if not cart_items:
        return {"error": "Cart is empty"}

    cart_total = sum(item["price"] * item["quantity"] for item in cart_items)

    order_data = create_order_db(user_id, cart_items, cart_total, promo_code)

    clear_cart_db(user_id)

    send_order_to_telegram(cart_items, user_id, order_data['total_price'], order_data['discount'])

    return {
        "success": "Order placed successfully",
        "order_id": order_data['order_id'],
        "total": order_data['total_price'],
        "discount": order_data['discount']
    }

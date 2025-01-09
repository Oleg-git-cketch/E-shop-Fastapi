from fastapi import FastAPI

from api.address import address_router
from api.cart import cart_router
from api.categories import category_router
from api.comments import comments_router
from api.likes import like_router
from api.orderhistory import history_router
from api.products import product_router
from api.promo import promo_router
from api.support import support_router
from db import Base, engine
from api.users import user_router
from api.buy import buy_router


Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')
app.include_router(user_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(cart_router)
app.include_router(buy_router)
app.include_router(address_router)
app.include_router(history_router)
app.include_router(promo_router)
app.include_router(like_router)
app.include_router(comments_router)
app.include_router(support_router)

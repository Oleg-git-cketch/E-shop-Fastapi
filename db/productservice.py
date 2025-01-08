from db.models import Product, Comment, Order, OrderItem, Category, Address, Cart, User, PromoCode
from db import get_db



"""
Product
"""

def add_product_db(user_id: int, pr_name: str, pr_description: str, pr_price: float, pr_quantity: int, category_id: int):
    db = next(get_db())

    category = db.query(Category).filter_by(id=category_id).first()
    if not category:
        return {"error": "Category not found"}

    new_product = Product(
        user_id=user_id,
        pr_name=pr_name,
        pr_description=pr_description,
        pr_price=pr_price,
        pr_quantity=pr_quantity,
        category_id=category_id
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "ID:": new_product.id,
        "Название товара:": new_product.pr_name,
        "Описание товара:": new_product.pr_description,
        "Цена:": new_product.pr_price,
        "Количество:": new_product.pr_quantity,
        "Категория:": category.name
    }

def get_exact_product_db(pr_id: int):
    db = next(get_db())
    exact_product = db.query(Product).filter_by(id=pr_id).first()
    return exact_product

def get_all_product_db(pr_id: int):
    db = next(get_db())
    if pr_id:
        all_products = db.query(Product).filter_by(id=pr_id).first()
        return all_products
    return False

def update_product_db(pr_id: int, change_info: str, new_info: str):
    db = next(get_db())
    update_product = db.query(Product).filter_by(id=pr_id).first()

    if update_product:
        if change_info == 'pr_name':
            update_product.pr_name = new_info
        elif change_info == 'pr_description':
            update_product.pr_description = new_info
        elif change_info == 'pr_price':
            update_product.pr_price = new_info
        elif change_info == 'pr_quantity':
            update_product.pr_quantity = new_info
        else:
            return False

        db.commit()
        return True
    return False

def delete_product_db(pr_id: int):
    db = next(get_db())
    delete_product = db.query(Product).filter_by(id=pr_id).first()
    if delete_product:
        db.delete(delete_product)
        db.commit()
        return True
    return False


"""
Comment
"""

def add_comment_db(user_id: int, product_id: int, text: str):
    db = next(get_db())
    product = db.query(Product).filter_by(id=product_id).first()
    user = db.query(User).filter_by(id=user_id).first()

    if product and user:
        new_comment = Comment(user_id=user_id, product_id=product_id, text=text)
        db.add(new_comment)
        db.commit()
        return new_comment
    return False

def get_all_comments_db(comment_id: int):
    db = next(get_db())
    if comment_id:
        all_comments = db.query(Comment).filter_by(id=comment_id).first()
        return all_comments
    return False

def get_exact_comment_db(comment_id: int):
    db = next(get_db())
    exact_user = db.query(Comment).filter_by(id=comment_id).first()
    return exact_user

def get_comments_by_product_db(pr_id: int):
    db = next(get_db())
    exact_user = db.query(Product).filter_by(id=pr_id).first()
    return exact_user

def get_comments_by_user_db(user_id: int):
    db = next(get_db())
    exact_user = db.query(Product).filter_by(id=user_id).first()
    return exact_user

def update_comment_db(comment_id: int, new_info: str):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()

    if comment:
        comment.text = new_info
        db.commit()
        return comment
    return False

def delete_comment_db(comment_id: int):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
        return True
    return False



"""
Likes
"""

def add_like_to_comment_db(user_id: int, comment_id: int):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()
    user = db.query(User).filter_by(id=user_id).first()

    if comment and user:
        comment.likes = (comment.likes or 0) + 1
        db.commit()
        return True
    return False


def delete_like_by_comment_db(user_id: int, comment_id: int):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()
    user = db.query(User).filter_by(id=user_id).first()

    if comment and user:
        comment.likes = (comment.likes or 0) - 1
        db.commit()
        return True
    return False

def get_likes_by_comment_db(comment_id: int):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()
    if comment:
        return f'лайки: {comment.likes}'
    return False


def add_like_to_product_db(user_id: int, pr_id: int):
    db = next(get_db())
    product = db.query(Product).filter_by(id=pr_id).first()
    user = db.query(User).filter_by(id=user_id).first()

    if product and user:
        product.pr_likes = (product.pr_likes or 0) + 1
        db.commit()
        return True
    return False


def delete_like_by_product_db(user_id: int, pr_id: int):
    db = next(get_db())
    product = db.query(Product).filter_by(id=pr_id).first()
    user = db.query(User).filter_by(id=user_id).first()

    if product and user:
        product.pr_likes = (product.pr_likes or 0) - 1
        db.commit()
        return True
    return False

def get_likes_by_product_db(pr_id: int):
    db = next(get_db())
    product = db.query(Product).filter_by(id=pr_id).first()
    if product:
        return f'лайки: {product.pr_likes}'
    return False



"""
Cart
"""

def add_to_cart_db(user_id: int, pr_id: int, quantity: int):
    db = next(get_db())

    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        return {"error": "User not found"}

    product = db.query(Product).filter_by(id=pr_id).first()
    if not product:
        return {"error": "Product not found"}

    if product.pr_quantity < quantity:
        return {"error": "Not enough product in stock"}

    cart_item = db.query(Cart).filter_by(user_id=user_id, pr_id=pr_id).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id=user_id, pr_id=pr_id, quantity=quantity)
        db.add(cart_item)

    product.pr_quantity -= quantity

    db.commit()
    return {"success": "Product added to cart"}

def get_cart_by_user_db(user_id: int):
    db = next(get_db())
    cart_items = db.query(Cart).filter_by(user_id=user_id).all()
    cart = []

    for item in cart_items:
        product = db.query(Product).filter_by(id=item.pr_id).first()
        cart.append({
            "ID": product.id,
            "product_name": product.pr_name,
            "quantity": item.quantity,
            "price": product.pr_price,
            "total_price": product.pr_price * item.quantity
        })
    return cart





def delete_from_cart_db(cart_item_id: int):
    db = next(get_db())
    cart_item = db.query(Cart).filter_by(id=cart_item_id).first()
    if not cart_item:
        return {"error": "Cart item not found"}

    product = db.query(Product).filter_by(id=cart_item.pr_id).first()
    if product:
        product.pr_quantity += cart_item.quantity

    db.delete(cart_item)
    db.commit()
    return {"success": "Cart item removed"}

def clear_cart_db(user_id: int):
    db = next(get_db())
    cart_items = db.query(Cart).filter_by(user_id=user_id).all()

    for item in cart_items:
        product = db.query(Product).filter_by(id=item.pr_id).first()
        if product:
            product.pr_quantity += item.quantity
        db.delete(item)

    db.commit()
    return {"success": "Cart cleared"}

def buy_db(user_id: int):
    db = next(get_db())
    cart_items = db.query(Cart).filter_by(user_id=user_id).all()
    return cart_items



"""
Order
"""

def create_order_db(user_id: int, cart_items: list, cart_total: float, promo_code: str = None):
    db = next(get_db())

    if promo_code:
        cart_total, discount = apply_promo_code_db(promo_code, cart_total)
    else:
        discount = 0

    new_order = Order(
        user_id=user_id,
        total_price=cart_total,
        status="Pending"
    )
    db.add(new_order)
    db.commit()

    for item in cart_items:
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item['ID'],
            quantity=item['quantity'],
            price=item['price']
        )
        db.add(order_item)

    db.commit()

    return {
        "order_id": new_order.id,
        "total_price": cart_total,
        "discount": discount,
        "status": new_order.status
    }

def get_order_db(order_id):
    db = next(get_db())
    order = db.query(Order).filter_by(id=order_id).first()
    return order



"""
History
"""

def get_purchase_history_db(user_id: int):
    db = next(get_db())

    orders = db.query(Order).filter_by(user_id=user_id).all()

    if not orders:
        return []

    history = []
    for order in orders:
        order_items = db.query(OrderItem).filter_by(order_id=order.id).all()
        items = [
            {
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price_per_item": item.price,
                "total_price": item.quantity * item.price
            }
            for item in order_items
        ]

        history.append({
            "order_id": order.id,
            "total_price": order.total_price,
            "status": order.status,
            "created_at": order.created_at,
            "items": items
        })

    return history

def delete_history_db(order_id: int):
    db = next(get_db())

    order = db.query(Order).filter_by(id=order_id).first()

    if not order:
        raise Exception("Order not found")

    order_items = db.query(OrderItem).filter_by(order_id=order.id).all()
    for item in order_items:
        db.delete(item)

    db.delete(order)

    db.commit()
    return {"success": "Order and its items deleted successfully"}

def clear_purchase_history_db(user_id: int):
    db = next(get_db())

    orders = db.query(Order).filter_by(user_id=user_id).all()

    if not orders:
        raise Exception("No orders found for this user")

    for order in orders:
        order_items = db.query(OrderItem).filter_by(order_id=order.id).all()
        for item in order_items:
            db.delete(item)

        db.delete(order)

    db.commit()
    return {"success": "All purchase history deleted successfully"}



"""
Categories
"""

def create_category_db(name: str, description: str):
    db = next(get_db())

    existing_category = db.query(Category).filter_by(name=name).first()

    new_category = Category(name=name, description=description)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return {
        "ID:": new_category.id,
        "Название категории:": new_category.name,
        "Описание категории:": new_category.description
    }

def get_categories_db(category_id):
    db = next(get_db())
    category = db.query(Category).filter_by(id=category_id).first()
    return category

def update_category_db(category_id, change_info, new_info):
    db = next(get_db())
    category = db.query(Category).filter_by(id=category_id).first()
    if category:
        if change_info == 'name':
            category.name = new_info
        if change_info == 'description':
            category.description = new_info
        db.commit()
        return True
    return False

def delete_category_db(category_id):
    db = next(get_db())
    category = db.query(Category).filter_by(id=category_id).first()

    if category:
        db.delete(category)
        db.commit()
        return True
    return False

"""
Address
"""

def add_address_db(user_id: int, street: str, house_number: str, entrance_number: str = None, apartment_number: str = None, city: str = None, country: str = None):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()

    if not user:
        return {"error": "User not found"}

    if not city or not country:
        return {"error": "City and Country are required fields"}

    new_address = Address(
        user_id=user_id,
        street=street,
        house_number=house_number,
        entrance_number=entrance_number,
        apartment_number=apartment_number,
        city=city,
        country=country
    )

    db.add(new_address)
    db.commit()
    db.refresh(new_address)

    return {
        "ID:": new_address.id,
        "Улица:": new_address.street,
        "Номер дома:": new_address.house_number,
        "Номер подъезда:": new_address.entrance_number,
        "Номер квартиры:": new_address.apartment_number,
        "Город:": new_address.city,
        "Страна:": new_address.country
    }

def get_user_addresses_db(user_id: int):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()

    if not user:
        return {"error": "User not found"}

    addresses = db.query(Address).filter_by(user_id=user_id).all()
    address_list = []

    for address in addresses:
        address_list.append({
            "ID:": address.id,
            "Улица:": address.street,
            "Номер дома:": address.house_number,
            "Номер подъезда:": address.entrance_number,
            "Номер квартиры:": address.apartment_number,
            "Город:": address.city,
            "Страна:": address.country
        })

    return address_list

def update_address_db(user_id: int, change_info: str, new_info: str):
    db = next(get_db())

    addresses = db.query(Address).filter_by(user_id=user_id).all()
    updated_addresses = []

    for address in addresses:
        if change_info == "street":
            address.street = new_info
        elif change_info == "house_number":
            address.house_number = new_info
        elif change_info == "entrance_number":
            address.entrance_number = new_info
        elif change_info == "apartment_number":
            address.apartment_number = new_info
        elif change_info == "city":
            address.city = new_info
        elif change_info == "country":
            address.country = new_info
        else:
            return {"error": "Invalid field to update"}

        db.commit()

        updated_addresses.append({
            "ID:": address.id,
            "Улица:": address.street,
            "Номер дома:": address.house_number,
            "Номер подъезда:": address.entrance_number,
            "Номер квартиры:": address.apartment_number,
            "Город:": address.city,
            "Страна:": address.country
        })

    return updated_addresses
def delete_address_db(user_id: int):
    db = next(get_db())

    addresses = db.query(Address).filter_by(user_id=user_id).all()

    if not addresses:
        return {"error": "User does not have any addresses"}

    for address in addresses:
        db.delete(address)

    db.commit()
    return {"success": "All addresses deleted successfully"}



def create_promo_code_db(code: str, amount: float, min_order_value: float):
    db = next(get_db())

    db_promo = PromoCode(code=code, amount=amount, min_order_value=min_order_value)
    db.add(db_promo)
    db.commit()
    db.refresh(db_promo)
    return db_promo

def apply_promo_code_db(code: str, order_total: float):
    db = next(get_db())

    promo = db.query(PromoCode).filter_by(code=code).first()

    if promo and order_total >= promo.min_order_value:
        discounted_total = order_total - promo.amount
        return discounted_total, promo.amount

    return order_total, 0
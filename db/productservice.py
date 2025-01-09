from db.models import Product, Comment, Order, OrderItem, Category, Address, Cart, User, PromoCode
from db import get_db



"""
Product
"""

def add_product_db(user_id: int, pr_name: str, pr_description: str, pr_price: float, pr_quantity: int, category_id: int):
    db = next(get_db())

    category = db.query(Category).filter_by(id=category_id).first()
    if not category:
        return 'Категория не найдена!'

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
    return 'Продукт успешно добавлен!'

def get_exact_product_db(pr_id: int):
    db = next(get_db())
    exact_product = db.query(Product).filter_by(id=pr_id).first()
    if exact_product:
        return [{
            "ID:": exact_product.id,
            "Название товара:": exact_product.pr_name,
            "Описание товара:": exact_product.pr_description,
            "Цена:": exact_product.pr_price,
            "Количество:": exact_product.pr_quantity,
            "Категория:": exact_product.category
        }]
    return 'Продукт не найден!'

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
            return 'Изменяемая информация не найдена!'

        db.commit()
        return 'Продукт успешно изменен!'
    return 'Продукт не найден!'

def delete_product_db(pr_id: int):
    db = next(get_db())
    delete_product = db.query(Product).filter_by(id=pr_id).first()
    if delete_product:
        db.delete(delete_product)
        db.commit()
        return 'Продукт успешно удален!'
    return 'Продукт не найден!'


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
        return 'Коммент успешно добавлен!'
    return 'Продукт или пользователь не найдены!'

def get_comment_db(comment_id: int):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()
    if comment:
        return [{
            'ID': comment.id,
            'Пользователь': comment.user_id,
            'Продукт': comment.product_id,
            'Текст': comment.text,
            'Лайки': comment.likes,
            'Дата создания': comment.reg_date
        }]
    return 'Коммент не найден!'

def update_comment_db(comment_id: int, new_info: str):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()

    if comment:
        comment.text = new_info
        db.commit()
        return 'Коммент успешно обновлен!'
    return 'Коммент не найден!'

def delete_comment_db(comment_id: int):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
        return 'Коммент успешно удален!'
    return 'Коммент не найден!'



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
        return 'Лайк успешно поставлен!'
    return 'Коммент или Пользователь не найдены!'


def delete_like_by_comment_db(user_id: int, comment_id: int):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()
    user = db.query(User).filter_by(id=user_id).first()

    if comment and user:
        comment.likes = (comment.likes or 0) - 1
        db.commit()
        return 'Лайк успешно убран!'
    return 'Коммент или Пользователь не найдены!'

def get_likes_by_comment_db(comment_id: int):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()
    if comment:
        return [{
            'ID автора коммента': comment.user_id,
            'Коммент ID': comment.id,
            'Коммент': comment.text,
            'Лайки': comment.likes
        }]
    return 'Коммент не найден!'


def add_like_to_product_db(user_id: int, pr_id: int):
    db = next(get_db())
    product = db.query(Product).filter_by(id=pr_id).first()
    user = db.query(User).filter_by(id=user_id).first()

    if product and user:
        product.pr_likes = (product.pr_likes or 0) + 1
        db.commit()
        return 'Лайк успешно поставлен!'
    return 'Продукт или Пользователь не найдены!'


def delete_like_by_product_db(user_id: int, pr_id: int):
    db = next(get_db())
    product = db.query(Product).filter_by(id=pr_id).first()
    user = db.query(User).filter_by(id=user_id).first()

    if product and user:
        product.pr_likes = (product.pr_likes or 0) - 1
        db.commit()
        return 'Лайк успешно убран!'
    return 'Коммент или Пользователь не найдены!'

def get_likes_by_product_db(pr_id: int):
    db = next(get_db())
    product = db.query(Product).filter_by(id=pr_id).first()
    if product:
        return [{
            'ID автора продукта': product.user_id,
            'ID Продукта': product.id,
            'Название продукта': product.pr_name,
            'Лайки': product.pr_likes
        }]
    return 'Продукт не найден!'



"""
Cart
"""

def add_to_cart_db(user_id: int, pr_id: int, quantity: int):
    db = next(get_db())

    user = db.query(User).filter_by(id=user_id).first()
    product = db.query(Product).filter_by(id=pr_id).first()
    cart_item = db.query(Cart).filter_by(user_id=user_id, pr_id=pr_id).first()

    if not user:
        return 'Пользователь не найден!'

    if not product:
        return 'Продукт не найден!'

    if product.pr_quantity < quantity:
        return 'Столько продуктов нет в наличии!'

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id=user_id, pr_id=pr_id, quantity=quantity)
        db.add(cart_item)

    product.pr_quantity -= quantity

    db.commit()
    return 'Продукт добавлен в корзину!'

def get_cart_by_user_db(user_id: int):
    db = next(get_db())
    cart_items = db.query(Cart).filter_by(user_id=user_id).all()
    items = []

    if cart_items:
        for item in cart_items:
            product = db.query(Product).filter_by(id=item.pr_id).first()
            items.append({
                "ID": product.id,
                "product_name": product.pr_name,
                "quantity": item.quantity,
                "price": product.pr_price,
                "total_price": product.pr_price * item.quantity,
            })
        return items

    return []


def delete_from_cart_db(cart_item_id: int):
    db = next(get_db())
    cart_item = db.query(Cart).filter_by(id=cart_item_id).first()
    if not cart_item:
        return 'Продукты в корзине не найдены!'

    product = db.query(Product).filter_by(id=cart_item.pr_id).first()
    if product:
        product.pr_quantity += cart_item.quantity

    db.delete(cart_item)
    db.commit()
    return 'Продукты в корзине были успешно очищены!'

def clear_cart_db(user_id: int):
    db = next(get_db())
    cart_items = db.query(Cart).filter_by(user_id=user_id).all()

    if cart_items:
        for item in cart_items:
            product = db.query(Product).filter_by(id=item.pr_id).first()
            if product:
                product.pr_quantity += item.quantity
            db.delete(item)
            db.commit()
            return 'Корзина успешно очищена!'
    return 'Продукты в корзине не найдены!'

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




"""
History
"""

def get_purchase_history_db(user_id: int):
    db = next(get_db())

    orders = db.query(Order).filter_by(user_id=user_id).all()

    if not orders:
        return 'Заказы у пользователя не были найдены!'

    history = []
    for order in orders:
        order_items = db.query(OrderItem).filter_by(order_id=order.id).all()
        items = [
            {
                "ID Продукта": item.product_id,
                "Количество": item.quantity,
                "Цена на 1 шт": item.price,
                "Конечная цена": item.quantity * item.price
            }
            for item in order_items
        ]

        history.append({
            "ID заказа": order.id,
            "Конечная цена (с промокодом)": order.total_price,
            "Статус": order.status,
            "Дата создания": order.created_at,
            "Продукты": items
        })

    return history

def delete_history_db(order_id: int):
    db = next(get_db())

    order = db.query(Order).filter_by(id=order_id).first()
    order_items = db.query(OrderItem).filter_by(order_id=order.id).all()

    if order:
        for item in order_items:
            db.delete(item)
            db.delete(order)
            db.commit()
            return 'Заказ успешно удален!'
    return 'Заказ не найден!'

def clear_purchase_history_db(user_id: int):
    db = next(get_db())

    orders = db.query(Order).filter_by(user_id=user_id).all()

    if orders:
        for order in orders:
            order_items = db.query(OrderItem).filter_by(order_id=order.id).all()
            for item in order_items:
                db.delete(item)

            db.delete(order)
        db.commit()
        return 'История была успешно очищена!'
    return 'Заказы у пользователя не были найдены!'




"""
Categories
"""

def create_category_db(name: str, description: str):
    db = next(get_db())

    category = Category(name=name, description=description)
    db.add(category)
    db.commit()
    db.refresh(category)

    return 'Категория успешно создана!'

def get_categories_db(category_id):
    db = next(get_db())
    category = db.query(Category).filter_by(id=category_id).first()

    if category:
        return [{"ID:": category.id,
             "Название категории:": category.name,
             "Описание категории:": category.description}]
    return 'Категория не найдена!'

def update_category_db(category_id, change_info, new_info):
    db = next(get_db())
    category = db.query(Category).filter_by(id=category_id).first()

    if category:
        if change_info == 'name':
            category.name = new_info
        if change_info == 'description':
            category.description = new_info
        db.commit()
        return 'Данные успешно обновлены!'
    return 'Категория не найдена!'

def delete_category_db(category_id):
    db = next(get_db())
    category = db.query(Category).filter_by(id=category_id).first()

    if category:
        db.delete(category)
        db.commit()
        return 'Категория успешно удалена!'
    return 'Категория не найдена!'

"""
Address
"""

def add_address_db(user_id: int, street: str, house_number: str, entrance_number: str = None, apartment_number: str = None, city: str = None, country: str = None):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()

    if not user:
        return 'Пользователь не найден!'


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

    return 'Адрес успешно добавлен!'

def get_user_addresses_db(user_id: int):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    addresses = db.query(Address).filter_by(user_id=user_id).all()
    result = []

    if user and addresses:
        for address in addresses:
            result.append({
                "ID адреса": address.id,
                "Улица": address.street,
                "Номер дома": address.house_number,
                "Номер подьезда": address.entrance_number,
                "Номер квартиры": address.apartment_number,
                "Город": address.city,
                "Страна": address.country
            })
        return result
    return 'Пользователь или адрес не были найдены!'


def update_address_db(user_id: int, change_info: str, new_info: str):
    db = next(get_db())

    addresses = db.query(Address).filter_by(user_id=user_id).all()

    if addresses:
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
                return 'Изменяемая информация не найдена!'

            db.commit()
            return 'Информация успешно обновлена!'
    return 'Адрес не найден!'

def delete_address_db(user_id: int):
    db = next(get_db())

    addresses = db.query(Address).filter_by(user_id=user_id).all()

    if addresses:
        for address in addresses:
            db.delete(address)
            db.commit()
            return 'Адрес был успешно удален!'
    return 'Ошибка! У пользователя нет сохраненных адресов!'



def create_promo_code_db(code: str, amount: float, min_order_value: float):
    db = next(get_db())

    promo = PromoCode(code=code, amount=amount, min_order_value=min_order_value)
    db.add(promo)
    db.commit()
    db.refresh(promo)
    return 'Промокод был успешно добавлен!'

def get_promo_code_db(code):
    db = next(get_db())
    promo = db.query(PromoCode).filter_by(code=code).first()

    if promo:
        return [{
            'ID': promo.id,
            'Промокод': promo.code,
            'Сумма скидки': promo.amount,
            'Минимальная сумма заказа': promo.min_order_value
        }]
    return 'Промокод не найден!'

def update_promo_code_db(code, change_info, new_info):
    db = next(get_db())
    promo = db.query(PromoCode).filter_by(code=code).first()

    if promo:
        if change_info == 'code':
            promo.code = new_info
        elif change_info == 'amount':
            promo.amount = new_info
        elif change_info == 'min_order_value':
            promo.min_order_value = new_info

        db.commit()
        return 'Информация успешно обновлена!'
    return 'Промокод не найден!'

def delete_promo_code(code):
    db = next(get_db())
    promo = db.query(PromoCode).filter_by(code=code).first()

    if promo:
        db.delete(promo)
        db.commit()
        return 'Промокод успешно удален!'
    return 'Промокод не найден!'


def apply_promo_code_db(code: str, order_total: float):
    db = next(get_db())

    promo = db.query(PromoCode).filter_by(code=code).first()

    if promo and order_total >= promo.min_order_value:
        discounted_total = order_total - promo.amount
        return discounted_total, promo.amount

    return order_total, 0
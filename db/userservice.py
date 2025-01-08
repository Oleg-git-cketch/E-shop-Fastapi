from db import get_db
from db.models import User


def register_user_db(name: str, surname: str, phone_number: str, age: str, city: str, username: str, email: str, password: str):
    db = next(get_db())
    new_user = User(name=name, surname=surname, phone_number=phone_number, age=age, city=city, username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    return new_user

def get_exact_user_db(user_id: int):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    return exact_user

def get_all_users_db(user_id: int):
    db = next(get_db())
    if user_id:
        all_users = db.query(User).filter_by(id=user_id).first()
        return all_users

def update_user_db(user_id: int, change_info: str, new_info: str):
    db = next(get_db())
    update_user = db.query(User).filter_by(id=user_id).first()

    if update_user:
        if change_info == 'name':
            update_user.name = new_info
        elif change_info == 'surname':
            update_user.surname = new_info
        elif change_info == 'phone_number':
            update_user.phone_number = new_info
        elif change_info == 'age':
            update_user.age = new_info
        elif change_info == 'city':
            update_user.city = new_info
        elif change_info == 'username':
            update_user.username = new_info
        elif change_info == 'email':
            update_user.email = new_info
        elif change_info == 'password':
            update_user.password = new_info
        else:
            return False

        db.commit()
        return True
    return False

def delete_user_db(user_id: int):
    db = next(get_db())
    delete_user = db.query(User).filter_by(id=user_id).first()

    if delete_user:
        db.delete(delete_user)
        db.commit()
        return True
    return False
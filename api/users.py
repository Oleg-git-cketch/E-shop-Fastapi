from fastapi import APIRouter
from db.userservice import *
from pydantic import BaseModel
from typing import Optional
from api import result_message


user_router = APIRouter(prefix='/user', tags=["Пользователи"])


class UserModel(BaseModel):
    username: str
    phone_number: str
    email: str
    password: str
    name: str
    surname: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None

@user_router.post("/register_user")
async def register_user(user_data: UserModel):
    user_dict = dict(user_data)
    result = register_user_db(**user_dict)
    return result_message(result)

@user_router.get('/get_exact_user')
async def get_exact_user(user_id):
    result = get_exact_user_db(user_id)
    return result_message(result)

@user_router.post('/update_user')
async def update_user(user_id, change_info, new_info):
    result = update_user_db(user_id, change_info, new_info)
    return result_message(result)

@user_router.delete('/delete_user')
async def delete_user(user_id):
    result = delete_user_db(user_id)
    return result_message(result)
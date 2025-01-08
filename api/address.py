from db.productservice import *
from pydantic import BaseModel
from api import result_message
from fastapi import APIRouter

address_router = APIRouter(prefix='/address', tags=["Адреса"])

class AddressModel(BaseModel):
    user_id: int
    street: str
    house_number: str
    entrance_number: str
    apartment_number: str
    city: str
    country: str


@address_router.post('/add_address')
async def add_address(address_data: AddressModel):
    address_dict = dict(address_data)
    result = add_address_db(**address_dict)
    return result_message(result)

@address_router.get('/get_address')
async def get_address(user_id):
    result = get_user_addresses_db(user_id)
    return result_message(result)

@address_router.post('/update_address')
async def update_address(user_id, change_info, new_info):
    result = update_address_db(user_id, change_info, new_info)
    return result_message(result)

@address_router.delete('/delete_address')
async def delete_address(user_id):
    result = delete_address_db(user_id)
    return result_message(result)
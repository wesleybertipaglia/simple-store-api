from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None

    class Config:
        orm_mode = True

class AddressList(BaseModel):
    id: Optional[str] = None
    address: Optional[str] = None
    zip_code: Optional[str] = None

    class Config:
        orm_mode = True

class AddressSingle(BaseModel):
    id: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None

    class Config:
        orm_mode = True
        
class AddressCreate(BaseModel):
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None

    class Config:
        orm_mode = True

class AddressUpdate(BaseModel):
    user_id: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None

    class Config:
        orm_mode = True
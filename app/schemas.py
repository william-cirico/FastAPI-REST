from datetime import datetime

from pydantic import BaseModel, Field


class ClientBase(BaseModel):
    cpf: str
    name: str


class ClientCreate(ClientBase):
    class Config:
        schema_extra = {
            'example': {
                'cpf': '049.143.320-43',
                'name': 'Foo'
            }
        }


class Client(ClientBase):
    id: int

    class Config:

        orm_mode = True


class OrderBase(BaseModel):
    description: str
    price: float = Field(..., gt=0)


class OrderCreate(OrderBase):
    client_id: int

    class Config:
        schema_extra = {
            'example': {
                'description': 'Caneta',
                'price': 2.50,
                'client_id': 1
            }
        }


class Order(OrderBase):
    id: int
    date: datetime
    client: Client

    class Config:

        orm_mode = True

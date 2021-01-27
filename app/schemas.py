from datetime import date, time

from pydantic import BaseModel


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
        schema_extra = {
            'example': {
                'id': 1,
                'cpf': '049.143.320-42',
                'name': 'Foo'
            }
        }

        orm_mode = True


class OrderBase(BaseModel):
    client_id: int
    description: str
    price: float


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    date: date
    time: time

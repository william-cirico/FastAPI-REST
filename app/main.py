from fastapi import FastAPI

from . import models
from .database import engine
from .routers import clients, orders


models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        'name': 'clients',
        'description': 'Operações com clientes'
    },
    {
        'name': 'orders',
        'description': 'Operações com pedidos'
    },
]

app = FastAPI(
    title='FastAPI REST',
    description='Exemplo de REST API com Python utilizando o framework FastAPI',
    version='1.0.0',
    openapi_tags=tags_metadata
)

app.include_router(clients.router)
app.include_router(orders.router)

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud
from ..dependencies import get_db
from .. import schemas

router = APIRouter(
    prefix='/orders',
    tags=['orders']
)


@router.delete('/{order_id}', status_code=204, summary='Deleta um pedido')
def delete_order(order_id: int, db: Session = Depends(get_db)):
    """
    Deleta o pedido cujo ID foi passado como parâmetro na URL.
    """
    if not crud.get_order_by_id(db, order_id):
        raise HTTPException(404, detail='Pedido com o ID informado não existe.')

    crud.delete_order(db, order_id)


@router.get(
    '/',
    response_description='Lista com todos os pedidos cadastrados no banco',
    response_model=List[schemas.Order],
    summary='Lista todos os pedidos cadastrados no banco'
)
def get_orders(db: Session = Depends(get_db)):
    """
    Retorna uma lista com todos os pedidos cadastrados no banco
    """
    return crud.get_orders(db)


@router.get(
    '/{order_id}',
    response_description='O pedido solicitado',
    response_model=schemas.Order,
    summary='Lista as informações de um pedido através do seu ID'
)
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    """
    Retorna o pedido cujo ID foi passado como parâmetro na URL.
    """
    order = crud.get_order_by_id(db, order_id)

    if not order:
        raise HTTPException(404, detail='Pedido com o ID informado não existe.')

    return order


@router.put(
    '/{order_id}',
    response_description='O pedido com os dados atualizados',
    response_model=schemas.Order,
    summary='Atualiza os dados de um pedido'
)
def update_order(order_id: int, update_data: schemas.OrderCreate, db: Session = Depends(get_db)):
    """
    Atualiza um pedido com base no ID.
    """
    if not crud.get_order_by_id(db, order_id):
        raise HTTPException(404, detail='Pedido com o ID informado não existe.')

    if not crud.get_client_by_id(db, update_data.client_id):
        raise HTTPException(404, detail='Cliente com o ID informado não existe.')

    crud.update_order(db, order_id, update_data)

    return crud.get_order_by_id(db, order_id)


@router.post(
    '/',
    response_description='O pedido criado',
    response_model=schemas.Order,
    status_code=201,
    summary='Cria um pedido'
)
def post_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    """
    Cria um pedido com as seguintes informações:

    - **description**: Descrição do produto (obrigatório).
    - **price**: Preço do produto (obrigatório).
    """
    if not crud.get_client_by_id(db, order.client_id):
        raise HTTPException(404, detail='Cliente com o ID informado não existe.')

    return crud.create_order(db, order)

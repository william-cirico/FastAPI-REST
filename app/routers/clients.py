from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud
from ..dependencies import get_db
from .. import schemas
from .. import utils

router = APIRouter(
    prefix='/clients',
    tags=['clients']
)


@router.delete('/{client_id}', status_code=204, summary='Deleta um usuário')
def delete_client(client_id: int, db: Session = Depends(get_db)):
    """
    Deleta o usuário cujo ID foi passado como parâmetro na URL.
    """
    if not crud.get_client_by_id(db, client_id):
        raise HTTPException(404, detail='Usuário com o ID informado não está cadastrado.')

    crud.delete_client(db, client_id)


@router.get(
    '/',
    response_description='Lista com os clientes cadastrados no banco',
    response_model=List[schemas.Client],
    summary='Lista todos os clientes cadastrados no banco'
)
def get_clients(db: Session = Depends(get_db)):
    """
    Retorna uma lista com todos os clientes cadastrados no banco.
    """
    return crud.get_clients(db)


@router.get(
    '/{client_id}',
    response_description='O cliente solicitado',
    response_model=schemas.Client,
    summary='Lista os dados de um usuário através do seu ID'
)
def get_client_by_id(client_id: int, db: Session = Depends(get_db)):
    """
    Retorna o cliente cujo ID foi passado como parâmetro na URL.
    """
    client = crud.get_client_by_id(db, client_id)

    if not client:
        raise HTTPException(404, detail='Usuário com o ID informado não está cadastrado.')

    return client


@router.put(
    '/{client_id}',
    response_description='O cliente com os dados atualizados',
    response_model=schemas.Client,
    summary='Atualiza os dados de um cliente'
)
def update_client(
    client_id: int,
    name: str = Body(..., embed=True),
    db: Session = Depends(get_db)
):
    """
    Atualiza um cliente com base no ID. Como o CPF de uma pessoa não muda, só é
    possível alterar o nome da pessoa.
    """
    if not crud.get_client_by_id(db, client_id):
        raise HTTPException(404, detail='Usuário com o ID informado não está cadastrado.')

    crud.update_client(db, client_id, name)

    return crud.get_client_by_id(db, client_id)


@router.post(
    '/',
    response_description='O cliente criado',
    response_model=schemas.Client,
    status_code=201,
    summary='Cria um cliente'
)
def post_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """
    Cria um cliente com as seguintes informações:

    - **cpf**: CPF do cliente (obrigatório).
    - **name**: Nome do cliente (obrigatório).
    """
    cpf = utils.clear_cpf(client.cpf)

    if crud.get_client_by_cpf(db, cpf):
        raise HTTPException(400, detail='CPF informado já foi cadastrado.')

    if not utils.is_cpf_valid(cpf):
        raise HTTPException(400, detail='CPF informado é inválido.')

    return crud.create_client(db, cpf, client.name)







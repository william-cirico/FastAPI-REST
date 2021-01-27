from typing import List

from sqlalchemy.orm import Session

from . import models
from . import schemas


def create_client(db: Session, cpf: str, name: str) -> models.Client:
    db_client = models.Client(cpf=cpf, name=name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def delete_client(db: Session, client_id: int) -> None:
    db.query(models.Client).filter(models.Client.id == client_id).delete()
    db.commit()


def get_clients(db: Session) -> List[models.Client]:
    return db.query(models.Client).all()


def get_client_by_cpf(db: Session, cpf: str) -> models.Client:
    return db.query(models.Client).filter(models.Client.cpf == cpf).first()


def get_client_by_id(db: Session, client_id: int) -> models.Client:
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def update_client(db: Session, client_id: int, name: str):
    db.query(models.Client)\
        .filter(models.Client.id == client_id)\
        .update({models.Client.name: name})
    db.commit()

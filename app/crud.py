from typing import List
from datetime import datetime

from sqlalchemy.orm import Session

from . import models
from . import schemas


def create_client(db: Session, cpf: str, name: str) -> models.Client:
    db_client = models.Client(cpf=cpf, name=name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def create_order(db: Session, order: schemas.OrderCreate) -> models.Order:
    db_order = models.Order(
        **order.dict(),
        date=datetime.now()
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_client(db: Session, client_id: int) -> None:
    db.query(models.Client).filter(models.Client.id == client_id).delete()
    db.commit()


def delete_order(db: Session, order_id: int) -> None:
    db.query(models.Order).filter(models.Order.id == order_id).delete()
    db.commit()


def get_clients(db: Session) -> List[models.Client]:
    return db.query(models.Client).all()


def get_client_by_cpf(db: Session, cpf: str) -> models.Client:
    return db.query(models.Client).filter(models.Client.cpf == cpf).first()


def get_client_by_id(db: Session, client_id: int) -> models.Client:
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_orders(db: Session) -> List[models.Order]:
    return db.query(models.Order).all()


def get_order_by_id(db: Session, order_id: int) -> models.Order:
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def update_client(db: Session, client_id: int, name: str) -> None:
    db.query(models.Client)\
        .filter(models.Client.id == client_id)\
        .update({models.Client.name: name})
    db.commit()


def update_order(db: Session, order_id: int, update_data: schemas.OrderCreate) -> None:
    db.query(models.Order)\
        .filter(models.Order.id == order_id)\
        .update({**update_data.dict()})
    db.commit()

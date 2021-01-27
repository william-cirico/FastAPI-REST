from sqlalchemy import Column, DateTime, Integer, Float, ForeignKey, String

from .database import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String, unique=True)
    name = Column(String)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    price = Column(Float)
    date = Column(DateTime)
    client_id = (Integer, ForeignKey('clients.id'))

from sqlalchemy import Column, DateTime, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from .database import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String, unique=True)
    name = Column(String)

    orders = relationship('Order', back_populates='client')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    price = Column(Float)
    date = Column(DateTime)
    client_id = Column(Integer, ForeignKey('clients.id', ondelete='cascade'))

    client = relationship('Client', back_populates='orders')

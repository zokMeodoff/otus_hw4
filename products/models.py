from sqlalchemy import Column, Integer, String, Text
from products.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    author = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Text())
    image = Column(String(100), nullable=False)

    def __init__(self, author=None, name=None, price=None, description=None, image=None):
        self.author = author
        self.name = name
        self.price = price
        self.description = description
        self.image = image

    def __repr__(self):
        return self.author + " " + self.name
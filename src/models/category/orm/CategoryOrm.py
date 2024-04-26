from sqlalchemy import Column, String, Integer
from shared.Base.Base import Base


class CategoryOrm(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, nullable=False)
    name: str = Column(String(20), unique=True, nullable=False)

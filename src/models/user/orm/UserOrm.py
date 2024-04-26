from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import Enum

from shared.Enums.TypeAccess import TypeAccess
from shared.Base.Base import Base


class UserOrm(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20))
    login: str = Column(String(20), unique=True, nullable=False)
    password: str = Column(String(64), nullable=False)
    typeAccess = Column(Enum(TypeAccess), nullable=False, default=TypeAccess.User)

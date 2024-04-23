from datetime import datetime

from sqlalchemy import Column, Double, ForeignKey, DateTime, Integer
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship

from models.product.orm.Product import ProductOrm
from models.user.orm.UserOrm import UserOrm
from shared.Base.Base import Base


class ProductHistoryOrm(Base):
    __tablename__ = 'product_history'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    product_bar_cod: Mapped[str] = mapped_column(ForeignKey("product.bar_cod"))
    product_name: Mapped[str] = mapped_column(ForeignKey("product.name"))
    user_login: Mapped[str] = mapped_column(ForeignKey("user.login"))
    date: datetime = Column(DateTime, nullable=False)
    price: float = Column(Double, nullable=False)



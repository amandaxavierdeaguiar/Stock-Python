from sqlalchemy import Column, Double, ForeignKey, String, Integer
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.types import Enum

from shared.Enums.QuantityType import QuantityType
from shared.base.Base import Base


class ProductOrm(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    bar_cod = Column(String(20), unique=True, nullable=False)
    name = Column(String(20), unique=True, nullable=False)
    photo = Column(String(256), nullable=True)
    description = Column(String(256), nullable=False)
    price = Column(Double, nullable=False)
    brand_name: Mapped[str] = mapped_column(ForeignKey("brand.name"))
    category_name: Mapped[str] = mapped_column(ForeignKey("category.name"))
    quantity_type: QuantityType = Column(Enum(QuantityType), nullable=False)

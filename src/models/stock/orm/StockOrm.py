from sqlalchemy import Column, Double, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship
from shared.Base.Base import Base

from models.product.orm.Product import ProductOrm
from models.supplier.orm.SupplierOrm import SupplierOrm


class StockOrm(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True, nullable=False)
    product_name: Mapped[str] = mapped_column(ForeignKey("product.name"))
    product_bar_cod: Mapped[str] = mapped_column(ForeignKey("product.bar_cod"))
    supplier_name: Mapped[str] = mapped_column(ForeignKey("supplier.name"))
    quantity = Column(Double, nullable=False)

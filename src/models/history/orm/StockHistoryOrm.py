from datetime import datetime

from sqlalchemy import Column, Double, ForeignKey, DateTime, Integer
from sqlalchemy.orm import mapped_column, Mapped

from shared.base.Base import Base


class StockHistoryOrm(Base):
    __tablename__ = 'stock_history'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    product_bar_cod: Mapped[str] = mapped_column(ForeignKey("product.bar_cod"))
    product_name: Mapped[str] = mapped_column(ForeignKey("product.name"))
    supplier_name: Mapped[str] = mapped_column(ForeignKey("supplier.name"))
    user_login: Mapped[str] = mapped_column(ForeignKey("user.login"))
    date: datetime = Column(DateTime, nullable=False)
    quantity: float = Column(Double, nullable=False)

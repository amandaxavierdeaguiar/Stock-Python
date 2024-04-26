from sqlalchemy import Column, Double, ForeignKey, String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from shared.Base.Base import Base


class ProductOrm(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    bar_cod = Column(String(20), unique=True, nullable=False)
    name = Column(String(20), unique=True, nullable=False)
    photo = Column(String(256), nullable=True)
    description = Column(String(256), nullable=False)
    price = Column(Double, nullable=False)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

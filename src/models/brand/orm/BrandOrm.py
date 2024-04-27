from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped

from shared.Base.Base import Base


# from Models.supplier import SupplierOrm


class BrandOrm(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), unique=True, nullable=False)
    supplier_name: Mapped[int] = mapped_column(ForeignKey("supplier.name"))
    # supplier: Mapped['SupplierOrm'] = relationship(back_populates="brand")

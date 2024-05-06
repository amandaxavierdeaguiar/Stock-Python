from sqlalchemy import Column, String, Integer

from shared.base.Base import Base


class SupplierOrm(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False, unique=True)
    address = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(20), unique=True)

    # brand: Mapped[List["BrandOrm"]] = relationship(back_populates="supplier")

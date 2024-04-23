from datetime import datetime
from uuid import uuid1
from pydantic import BaseModel, ConfigDict


class ProductHistoryDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_name: str
    product_bar_cod: str
    user_login: str
    date: datetime = datetime.now()
    price: float


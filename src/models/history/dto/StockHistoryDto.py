from datetime import datetime

from pydantic import BaseModel, ConfigDict


class StockHistoryDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_name: str
    product_bar_cod: str
    supplier_name: str
    user_login: str
    date: datetime = datetime.now()
    quantity: float

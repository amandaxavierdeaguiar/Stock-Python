from typing import Optional

from pydantic import BaseModel, ConfigDict


class StockTableDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_name: str
    product_bar_cod: str
    category_name: str
    brand_name: str
    description: str
    photo: Optional[str] = None
    supplier_name: str
    quantity: float
    price: float

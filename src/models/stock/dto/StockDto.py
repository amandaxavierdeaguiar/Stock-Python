from pydantic import BaseModel, ConfigDict


class StockDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_name: str
    product_bar_cod: str
    supplier_name: str
    quantity: float

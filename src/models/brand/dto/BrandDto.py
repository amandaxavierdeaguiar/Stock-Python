from typing import Any

from pydantic import BaseModel, ConfigDict


class BrandDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    supplier_name: str

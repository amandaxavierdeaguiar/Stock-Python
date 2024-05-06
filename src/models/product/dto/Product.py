from typing import Optional

import shortuuid
from pydantic import BaseModel, computed_field, ConfigDict


class ProductDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    photo: Optional[str] = None
    description: str
    price: float
    brand_name: str
    category_name: str
    _bar_cod: str

    @computed_field
    @property
    def bar_cod(self) -> str:
        shortuuid.set_alphabet(alphabet="013456789")
        self._bar_cod = '{}-{}-{}'.format(
            shortuuid.uuid(self.brand_name)[:3],
            shortuuid.uuid(self.category_name)[:3],
            shortuuid.uuid(self.name)[:8])
        return self._bar_cod

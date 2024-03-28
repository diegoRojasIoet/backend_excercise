from decimal import Decimal
from typing import NamedTuple, Optional
from app.src.core import ProductStatuses

class EditProductRequest(NamedTuple):
    product_id: str
    user_id: str
    name: str
    description: Optional[str]
    price: Decimal
    location: str
    status: ProductStatuses
    is_available: bool

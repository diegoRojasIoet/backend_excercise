
from typing import NamedTuple
from app.src.core.enums import ProductStatuses

class FilterByStatusRequest(NamedTuple):
    status: ProductStatuses
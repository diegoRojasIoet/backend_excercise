from typing import List, NamedTuple

from ....core.models._product import Product

class FilterByStatusResponse(NamedTuple):
    products: List[Product]
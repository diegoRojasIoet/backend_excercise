from app.src.repositories import ProductRepository
from app.src.exceptions.repository.product import ProductRepositoryException

from .request import FilterByStatusRequest
from .response import FilterByStatusResponse

class FilterProductsByStatus:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def __call__(self, request: FilterByStatusRequest) -> FilterByStatusResponse:
        try:
            filtered_products = self.product_repository.filter_products_by_status(request.status)
            return FilterByStatusResponse(products=filtered_products)
        except ProductRepositoryException as error:
            raise ProductRepositoryException(str(error))
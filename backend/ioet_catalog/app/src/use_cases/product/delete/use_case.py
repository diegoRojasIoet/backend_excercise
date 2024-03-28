from typing import Optional

from app.src.core import Product
from app.src.repositories import ProductRepository
from app.src.exceptions import ProductNoneException, ProductRepositoryException, ProductBusinessException

from .response import DeleteProductResponse
from .request import DeleteProductRequest


class DeleteProduct:
  def __init__(self, product_repository: ProductRepository) -> None:
    self.product_repository = product_repository

  def __call__(self, request: DeleteProductRequest) -> Optional[DeleteProductResponse]:
    try:
      product_existing = self.product_repository.get_by_id(request.product_id)
      if not product_existing:
        raise ProductNoneException()
      
      response: Product = self.product_repository.delete(product_id=product_existing.product_id)
      return DeleteProductResponse(product_id=response.product_id)

    except ProductRepositoryException as e:
      raise ProductBusinessException(str(e))

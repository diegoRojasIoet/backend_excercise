from typing import Optional

from app.src.core import Product
from app.src.repositories import ProductRepository
from app.src.exceptions import ProductNoneException, ProductRepositoryException, ProductBusinessException

from .response import EditProductResponse
from .request import EditProductRequest


class EditProduct:
  def __init__(self, product_repository: ProductRepository) -> None:
    self.product_repository = product_repository

  def __call__(self, request: EditProductRequest) -> Optional[EditProductResponse]:
    try:
      product_existing = self.product_repository.get_by_id(request.product_id)
      if not product_existing:
        raise ProductNoneException()
      new_product = Product(**request._asdict())
      response: Product = self.product_repository.edit(new_product)
      if not response:
        raise ProductNoneException()
      return EditProductResponse(**response._asdict())

    except ProductRepositoryException as e:
      raise ProductBusinessException(str(e))

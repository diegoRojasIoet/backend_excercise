from decimal import Decimal
from adapters.src.repositories.memory.memory_product_repository import MemoryProductRepository
from app.src.core.enums import ProductStatuses
from app.src.use_cases.product.create.request import CreateProductRequest
from app.src.use_cases.product.create.use_case import CreateProduct
from app.src.core.models import Product
from app.src.use_cases.product.delete.request import DeleteProductRequest
from app.src.use_cases.product.delete.response import DeleteProductResponse
from app.src.use_cases.product.delete.use_case import DeleteProduct
from app.src.use_cases.product.list_all import ListProducts
class TestDeleteProduct:
    def test__delete_product_should_delete_the_specified_product(self):
        memory_repository = MemoryProductRepository()
        #Add products
        all_products = [
            Product(
                product_id="1",
                user_id="1",
                name="Headphones",
                description="Noise cancellation",
                price=Decimal(10.5),
                location="Quito",
                status=ProductStatuses.USED,
                is_available=True,
            ),
            Product(
                product_id="2",
                user_id="2",
                name="Jacket",
                description="Official ioet jacket",
                price=Decimal(20),
                location="Loja",
                status=ProductStatuses.USED,
                is_available=True,
            ),
            Product(
                product_id="3",
                user_id="3",
                name="Mac mini",
                description="With the M1 chip",
                price=Decimal(20),
                location="Guayaquil",
                status=ProductStatuses.NEW,
                is_available=False,
            ),
        ]
        create_use_case = CreateProduct(memory_repository)
        for product in all_products:
            request = CreateProductRequest(
                product_id=product.product_id,
                user_id=product.user_id,
                name=product.name,
                description=product.description,
                price=product.price,
                location=product.location,
                status=product.status,
                is_available=product.is_available
            )
            create_use_case(request=request)
        #
        expected_id = "1"
        expected_length = 2
        
        request = DeleteProductRequest(
            product_id=expected_id,
        )
        use_case = DeleteProduct(memory_repository)
        response = use_case(request=request)

        assert isinstance(response, DeleteProductResponse)
        assert response.product_id == response.product_id

        use_case = ListProducts(memory_repository)
        response = use_case()

        assert expected_length == len(response.products)
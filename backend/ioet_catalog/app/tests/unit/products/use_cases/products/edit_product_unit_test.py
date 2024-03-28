from decimal import Decimal
from adapters.src.repositories.memory.memory_product_repository import MemoryProductRepository
from app.src.use_cases import FilterProductsByStatus
from app.src.core.enums import ProductStatuses
from app.src.use_cases.product.create.request import CreateProductRequest
from app.src.use_cases.product.create.use_case import CreateProduct
from app.src.core.models import Product
from app.src.use_cases.product.edit.request import EditProductRequest
from app.src.use_cases.product.edit.response import EditProductResponse
from app.src.use_cases.product.edit.use_case import EditProduct
class TestEditProducts:
    def test__edit_product_change_price(self):
        memory_repository = MemoryProductRepository()
        #Add products

        product = Product(
                product_id="5",
                user_id="1",
                name="Headphones",
                description="Noise cancellation",
                price=Decimal(10.5),
                location="Quito",
                status=ProductStatuses.NEW,
                is_available=True,
            )

        create_use_case = CreateProduct(memory_repository)
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
        expected_price = 15
        
        request = EditProductRequest(
            product_id=product.product_id,
            user_id=product.user_id,
            name=product.name,
            description=product.description,
            price=15,
            location=product.location,
            status=product.status,
            is_available=product.is_available
        )
        use_case = EditProduct(memory_repository)

        response = use_case(request=request)
        assert isinstance(response, EditProductResponse)
        assert response.price == expected_price
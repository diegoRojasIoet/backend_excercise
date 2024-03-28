from typing import List

from fastapi import APIRouter, Depends

from app.src.use_cases import (
    ListProducts, 
    ListProductResponse, 
    FindProductById, 
    FindProductByIdResponse, 
    FindProductByIdRequest, 
    CreateProduct, 
    CreateProductResponse, 
    CreateProductRequest
)
from app.src.use_cases.product.filter_by_status.request import FilterByStatusRequest
from app.src.use_cases.product.filter_by_status.response import FilterByStatusResponse
from app.src.use_cases.product.filter_by_status.use_case import FilterProductsByStatus
from factories.use_cases.product import filter_product_by_status_use_case
from ..dtos import (
    ProductBase,
    ListProductResponseDto, 
    CreateProductRequestDto,
    CreateProductResponseDto,
    FindProductByIdResponseDto,
)
from factories.use_cases import (
    list_product_use_case, 
    find_product_by_id_use_case,
    create_product_use_case,
)
from app.src.core.models import Product

product_router = APIRouter(prefix="/products")

@product_router.get("/", response_model=ListProductResponseDto)
async def get_products(
    use_case: ListProducts = Depends(list_product_use_case)
) -> ListProductResponse:
    response = use_case()
    response_dto: ListProductResponseDto = ListProductResponseDto(
        products= [ProductBase(**product._asdict()) for product in response.products]
    )
    return response_dto

@product_router.get("/{product_id}", response_model=FindProductByIdResponseDto)
async def get_product_by_id(
    product_id: str,
    use_case: FindProductById = Depends(find_product_by_id_use_case)
) -> FindProductByIdResponse:
    response = use_case(FindProductByIdRequest(product_id=product_id))
    response_dto: FindProductByIdResponseDto = FindProductByIdResponseDto(**response._asdict())
    return response_dto

@product_router.post("/", response_model=CreateProductResponseDto)
async def create_product(
    request: CreateProductRequestDto,
    use_case: CreateProduct = Depends(create_product_use_case)
) -> CreateProductResponse:
    response = use_case(CreateProductRequest(
        product_id=request.product_id, 
        user_id=request.user_id, 
        name=request.name, 
        description=request.description, 
        price=request.price, 
        location=request.location, 
        status=request.status.value,
        is_available=request.is_available
    ))
    response_dto: CreateProductResponseDto = CreateProductResponseDto(**response._asdict())
    return response_dto

@product_router.get("/filter/by_status", response_model=FilterByStatusResponse)
async def filter_products_by_status(
    status: str,
    filter_use_case: FilterProductsByStatus = Depends(filter_product_by_status_use_case),
) -> FilterByStatusResponse:
    request = FilterByStatusRequest(status=status)
    response = filter_use_case(request)
    return response

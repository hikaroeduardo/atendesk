from fastapi import APIRouter, Depends, Body, status

from ..middlewares.verify_token import Middleware
from ..schemas.inputs.customers.create_customer_schema import Customer
from ..controllers.customers.create_customer_controller import CreateCustomerController
from ..responses_docs.customers.create_customer import create_customer_docs

router = APIRouter(tags=["Customers"], prefix="/customer")

@router.post('/', status_code=status.HTTP_201_CREATED, summary="Cadastrar novo cliente", responses={**create_customer_docs})
async def create_customer(data_customer: Customer = Body(examples=[
    {
        "name": "Cliente Teste",
        "phone": "86998000000",
        "email": "cliente@gmail.com"
    }
]), user_id: str = Depends(Middleware.verify_token)):
    return await CreateCustomerController.create(customer=data_customer, user_id=user_id)
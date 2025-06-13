from fastapi import APIRouter, Depends, Body, status, Query

from ..middlewares.verify_token import Middleware
from ..schemas.inputs.customers.create_customer_schema import Customer
from ..controllers.customers.create_customer_controller import CreateCustomerController
from ..controllers.customers.delete_customer_controller import DeleteCustomerController
from ..responses_docs.customers.create_customer import create_customer_docs
from ..responses_docs.customers.delete_customer import delete_customer_docs

router = APIRouter(tags=["Customers"], prefix="/customer")

# Cadastrar cliente
@router.post(
        '/',
        status_code=status.HTTP_201_CREATED,
        summary="Cadastrar novo cliente",
        responses={**create_customer_docs}
        )
async def create_customer(data_customer: Customer = Body(examples=[
    {
        "name": "Cliente Teste",
        "phone": "86998000000",
        "email": "cliente@gmail.com"
    }
]), user_id: str = Depends(Middleware.verify_token)):
    """
    Endpoint para criar um cliente.
    """
    return await CreateCustomerController.create(customer=data_customer, user_id=user_id)


# Deletar Cliente
@router.delete(
        '/',
        dependencies=[Depends(Middleware.verify_token)],
        summary="Deletar um cliente",
        responses={**delete_customer_docs}
        )
async def detele_customer(customer_id: int = Query(alias="id_cliente")):
    """
    Endpoint para deletar um cliente.
    """
    return await DeleteCustomerController.delete(customer_id)
from fastapi import APIRouter, Depends

from ..middlewares.verify_token import Middleware
from ..schemas.inputs.customers.create_customer_schema import Customer
from ..controllers.customers.create_customer_controller import CreateCustomerController

router = APIRouter(tags=["Customers"], prefix="/customer")

@router.post('/')
async def create_customer(data_customer: Customer, user_id: str = Depends(Middleware.verify_token)):

    return await CreateCustomerController.create(customer=data_customer, user_id=user_id)
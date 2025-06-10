from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from ...schemas.inputs.customers.create_customer_schema import Customer
from ...services.customers.create_customer_service import CreateCustomerService
from ...errors.global_error import GlobalError
from ...errors.customers.customer_already_exists_error import CustomerAlreadyExistis

class CreateCustomerController:
    @staticmethod
    async def create(customer: Customer, user_id: str):
        name = customer.name
        phone = customer.phone
        email = customer.email
        user_id = int(user_id)

        try:
            CreateCustomerService.execute(name=name, phone=phone, email=email, user_id=user_id)

            return JSONResponse(
                content={"success": "Cliente cadastrado com sucesso!"},
                status_code=status.HTTP_201_CREATED
            )
        except CustomerAlreadyExistis as error:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error))
        except GlobalError as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
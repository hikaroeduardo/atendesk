from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from ...services.customers.delete_customer_service import DeleteCustomerService
from ...errors.customers.customer_not_found_error import CustomerNotFound
from ...errors.global_error import GlobalError

class DeleteCustomerController:
    @staticmethod
    async def delete(customer_id: int):
        try:
            DeleteCustomerService.execute(customer_id)

            return JSONResponse(
                content={"success": "Cliente deletado com sucesso!"},
                status_code=status.HTTP_200_OK
            )
        except CustomerNotFound as error:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(error)
                )
        except GlobalError as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(error)
            )
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from ...schemas.inputs.tickets.create_ticket_schema import DataCreateTicket
from ...services.ticket.create_ticket_service import CreateTicketService
from ...errors.tickets.ticket_with_different_user_error import TicketWithDifferentUser
from ...errors.customers.customer_not_found_error import CustomerNotFound
from ...errors.global_error import GlobalError

class CreateTicketsController:
    @staticmethod
    async def create(data_ticket: DataCreateTicket, logged_user_id: str):
        data = data_ticket.model_dump()
        logged_user_id_treated = int(logged_user_id)

        try:
            CreateTicketService.execute(
                logged_user_id=logged_user_id_treated,
                user_id=data.get("user_id"),
                customer_id=data.get("customer_id"),
                name=data.get("name"),
                description=data.get("description"),
                )
            
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={
                    "success": "Ticket criado com sucesso."
                }
            )
        except TicketWithDifferentUser as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(error)
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
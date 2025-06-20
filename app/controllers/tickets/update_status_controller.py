from fastapi import HTTPException, status as status_response
from fastapi.responses import JSONResponse
from ...services.ticket.update_status_service import UpdateStatusService
from ...schemas.inputs.tickets.update_ticket_schema import UpdateTicketSchema
from ...errors.tickets.ticket_with_different_user_error import TicketWithDifferentUser
from ...errors.tickets.empty_status_error import EmptyStatus
from ...errors.tickets.ticket_not_found_error import TicketNotFound
from ...errors.global_error import GlobalError

class UpdateStatusController:
    @staticmethod
    async def update(user_id: str, ticket_id: str, status: UpdateTicketSchema):
        user_id_trated = int(user_id)
        ticket_id_trated = int(ticket_id)
        status_ticket = status.model_dump()['status']

        try:
            UpdateStatusService.execute(user_id=user_id_trated, ticket_id=ticket_id_trated, status=status_ticket)

            return JSONResponse(
                content={"success": "Status alterado com sucesso!"},
                status_code=status_response.HTTP_200_OK
            )
        except TicketNotFound as error:
            raise HTTPException(
                status_code=status_response.HTTP_404_NOT_FOUND,
                detail=str(error)
            )
        except TicketWithDifferentUser as error:
            raise HTTPException(
                status_code=status_response.HTTP_401_UNAUTHORIZED,
                detail=str(error)
            )
        except EmptyStatus as error:
            raise HTTPException(
                status_code=status_response.HTTP_400_BAD_REQUEST,
                detail=str(error)
            )
        except GlobalError as error:
            raise HTTPException(
                status_code=status_response.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(error)
            )
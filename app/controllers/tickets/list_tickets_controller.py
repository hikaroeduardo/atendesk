from fastapi import status as status_response, HTTPException
from fastapi.responses import JSONResponse
from ...services.ticket.list_tickets_service import ListTicketsService
from ...errors.global_error import GlobalError

class ListTicketsController:
    @staticmethod
    async def list(status: str, user_id: str):
        user_id_treated = int(user_id)

        try:
            tickets = ListTicketsService.execute(status=status, user_id=user_id_treated)

            return JSONResponse(
                status_code=status_response.HTTP_200_OK,
                content=tickets
            )
        except GlobalError as error:
            raise HTTPException(
                status_code=status_response.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(error)
            )
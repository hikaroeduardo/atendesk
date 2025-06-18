from fastapi import APIRouter, Depends, status
from ..controllers.tickets.create_ticker_controller import CreateTickerController
from ..middlewares.verify_token import Middleware
from ..schemas.inputs.tickets.create_ticket_schema import DataCreateTicket
from ..responses_docs.tickets.create_ticket import create_ticket_docs

router = APIRouter(tags=["Tickets"])

@router.post(
        '/ticket',
        status_code=status.HTTP_201_CREATED,
        summary="Criar um novo chamado",
        responses={**create_ticket_docs}
        )
async def create_tickert(data_ticket: DataCreateTicket, logged_user_id: str = Depends(Middleware.verify_token)):
    '''
    Endpoint para criar um novo ticket.
    '''
    return await CreateTickerController.create(data_ticket=data_ticket, logged_user_id=logged_user_id)

from fastapi import APIRouter, Depends, status
from ..controllers.tickets.create_tickets_controller import CreateTicketsController
from ..controllers.tickets.list_tickets_controller import ListTicketsController
from ..middlewares.verify_token import Middleware
from ..schemas.inputs.tickets.create_ticket_schema import DataCreateTicket
from ..responses_docs.tickets.create_ticket import create_ticket_docs
from ..responses_docs.tickets.list_tickets import list_tickets_docs

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
    return await CreateTicketsController.create(data_ticket=data_ticket, logged_user_id=logged_user_id)

@router.get(
    '/tickets',
    summary="Listar tickets de usuário",
    responses={**list_tickets_docs}
)
async def list_tickets(status: str = "Aberto", user_id: str = Depends(Middleware.verify_token)):
    return await ListTicketsController.list(status=status, user_id=user_id)
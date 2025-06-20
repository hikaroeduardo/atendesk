from ...database import session
from ...repositories.tickets.get_ticket_by_id import GetTicketByIdRepository
from ...repositories.tickets.patch_status_ticket import PatchStatusRepository
from ...errors.tickets.ticket_with_different_user_error import TicketWithDifferentUser
from ...errors.tickets.ticket_not_found_error import TicketNotFound
from ...errors.tickets.empty_status_error import EmptyStatus
from ...errors.global_error import GlobalError

class UpdateStatusService:
    @staticmethod
    def execute(user_id: int, ticket_id: int, status: str):
        try:
            ticket = GetTicketByIdRepository.get(session=session, id=ticket_id)

            if not ticket:
                raise TicketNotFound("Ticket não encontrado.")

            if ticket.user_id != user_id:
                raise TicketWithDifferentUser("Você não pode atualizar este ticket com este usuário.")
            
            if not status:
                raise EmptyStatus("Campo de novo status está vazio.")
            
            PatchStatusRepository.patch(session=session, ticket=ticket, status=status)
        except TicketNotFound:
            raise
        except TicketWithDifferentUser:
            raise
        except EmptyStatus:
            raise
        except:
            raise GlobalError("Não foi possível atualizar o status do ticket. Tente novamente mais tarde!")
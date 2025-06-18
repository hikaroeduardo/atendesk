from ...database import session
from ...repositories.tickets.get_list_tickets import ListTicketsRepository
from ...errors.global_error import GlobalError

class ListTicketsService:
    @staticmethod
    def execute(status: str, user_id: int):
        try:
            tickets = ListTicketsRepository.list(session=session, status=status, user_id=user_id)

            return tickets
        except:
            raise GlobalError("Não foi possível listar os tickets. Tente novamente mais tarde!")
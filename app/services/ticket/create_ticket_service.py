from ...errors.tickets.ticket_with_different_user_error import TicketWithDifferentUser
from ...errors.customers.customer_not_found_error import CustomerNotFound
from ...errors.global_error import GlobalError
from ...repositories.tickets.post_create_ticket import CreateTicketRepository
from ...repositories.customers.get_customer_by_id import GetCustomerByIdRepository
from ...database import session
'''
[] Verificar se custumer id existe
'''

class CreateTicketService:
    @staticmethod
    def execute(
        logged_user_id: int,
        user_id: int,
        customer_id: int,
        name: str,
        description: str
        ):

        if logged_user_id != user_id:
            raise TicketWithDifferentUser("Você não pode criar este ticket com este usuário.")
        
        try:
            customer = GetCustomerByIdRepository.get(session=session, customer_id=customer_id)

            if not customer:
                raise CustomerNotFound("Cliente não encontrado.")

            CreateTicketRepository.create(
                session=session,
                customer_id=customer_id,
                description=description,
                name=name,
                user_id=user_id
                )
        except CustomerNotFound:
            raise
        except:
            raise GlobalError("Erro ao cadastrar novo ticket, tente novamente mais tarde!")
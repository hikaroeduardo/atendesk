from ...repositories.customers.get_customer_by_id import GetCustomerByIdRepository
from ...repositories.customers.delete_customer import DeleteCustomerRepository
from ...errors.customers.customer_not_found_error import CustomerNotFound
from ...errors.global_error import GlobalError
from ...database import session

class DeleteCustomerService:
    @staticmethod
    def execute(customer_id: int):
        try:
            customer = GetCustomerByIdRepository.get(session=session, customer_id=customer_id)

            if not customer:
                raise CustomerNotFound("Cliente não encontrado.")
            
            DeleteCustomerRepository.delete(session=session, customer=customer)
        except CustomerNotFound:
            raise
        except Exception as error:
            raise GlobalError("Erro ao deletar cliente, tente novamente mais tarde!")
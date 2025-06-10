from ...errors.global_error import GlobalError
from ...errors.customers.customer_already_exists_error import CustomerAlreadyExistis
from ...repositories.customers.post_create_customer import CreateCustomerRepository
from ...repositories.customers.get_customer_by_email import GetCustomerByEmailRepository
from ...database import session

class CreateCustomerService:
    @staticmethod
    def execute(name: str, phone: str, email: str, user_id: int):
        try:
            customer = GetCustomerByEmailRepository.get(session=session, email=email)

            if customer:
                raise CustomerAlreadyExistis("Este cliente ja está cadastrado.")

            CreateCustomerRepository.create(session=session, name=name, phone=phone, email=email, user_id=user_id)
        except CustomerAlreadyExistis:
            raise
        except:
            raise GlobalError("Erro ao cadastrar novo cliente, tente novamente mais tarde!")
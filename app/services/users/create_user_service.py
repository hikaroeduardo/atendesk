from bcrypt import hashpw, gensalt

from ...repositories.users.get_user_by_username import GetUerByUsernameRepository
from ...repositories.users.post_create_user import CreateUserRepository
from ...errors.users.email_already_exists_error import UserAlreadyExistis
from ...errors.global_error import GlobalError
from ...database import session

class CreateUserService:
    @staticmethod
    def execute(name: str, email: str, username: str, password: str):
        try:
            user = GetUerByUsernameRepository.get(session=session, username=username)

            if user:
                raise UserAlreadyExistis("Este usuário ja existe em nosso sistema.")

            password_encode = password.encode()
            password_hashed = hashpw(password_encode, gensalt(8))

            CreateUserRepository.create(session=session, email=email, name=name, password=password_hashed, username=username)
        except UserAlreadyExistis:
            raise
        except:
            raise GlobalError("Erro ao cadastrar novo usuário, tente novamente mais tarde!")
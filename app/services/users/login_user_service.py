import os
import jwt
from dotenv import load_dotenv
from bcrypt import checkpw
from datetime import datetime, timedelta
from ...schemas.inputs.users.login_user_schema import DataLoginUser
from ...repositories.users.get_user_by_username import GetUerByUsernameRepository
from ...errors.users.invalid_credentials_error import InvalidCredentials
from ...errors.global_error import GlobalError
from ...database import session

load_dotenv()

class LoginUserService:
    @staticmethod
    def execute(user_data: DataLoginUser):
        try:
            user = GetUerByUsernameRepository.get(session=session, username=user_data.get("username"))

            if not user:
                raise InvalidCredentials("Credenciais incorretas.")
            
            user_password_checked = checkpw(str(user_data.get("password")).encode(), user.password)

            if not user_password_checked:
                raise InvalidCredentials("Credenciais incorretas.")
            
            expire = datetime.now() + timedelta(minutes=int(os.getenv("EXPIRE_TOKEN")))
            
            data_token = {
                "sub": str(user.id),
                "exp": expire
            }

            token = jwt.encode(data_token, os.getenv("SECRET_KEY_JWT"), os.getenv("ALGORITHM_JWT"))

            return token
        except InvalidCredentials:
            raise
        except:
            raise GlobalError("Não foi possível fazer o login, tente novamente mais tarde!")
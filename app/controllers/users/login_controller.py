from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from ...schemas.inputs.users.login_user_schema import DataLoginUser
from ...services.users.login_user_service import LoginUserService
from ...errors.users.invalid_credentials_error import InvalidCredentials
from ...errors.global_error import GlobalError

class LoginController:
    @staticmethod
    async def login(user_data: DataLoginUser):
        data = user_data.model_dump()
        try:
            token = LoginUserService.execute(data)

            return JSONResponse(
                content={
                    "token": token
                },
                status_code=status.HTTP_200_OK
            )
        except InvalidCredentials as error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(error)
            )
        except GlobalError as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(error)
            )
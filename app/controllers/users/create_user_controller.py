from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from ...schemas.inputs.users.create_user_schema import DataCreateUser
from ...services.users.create_user_service import CreateUserService
from ...errors.users.email_already_exists_error import UserAlreadyExistis
from ...errors.global_error import GlobalError

class CreateUserController:
    @staticmethod
    async def create(data_user: DataCreateUser):
        data = data_user.model_dump()
        try:
            CreateUserService.execute(**data)

            return JSONResponse(
                content="Usuário cadastrado com sucesso!",
                status_code=status.HTTP_201_CREATED
            )
        except UserAlreadyExistis as error:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error))
        except GlobalError as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
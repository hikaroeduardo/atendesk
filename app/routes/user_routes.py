from fastapi import APIRouter, status
from ..controllers.users.create_user_controller import CreateUserController
from ..schemas.inputs.users.create_user_schema import DataCreateUser

router = APIRouter(tags=['users'], prefix="/user")

@router.post('/', status_code=status.HTTP_201_CREATED, summary="Criar novo usuário")
async def create_user(data_user: DataCreateUser):
    """
    Endpoint para criação de um novo usuário para o sistema
    """
    return await CreateUserController.create(data_user)
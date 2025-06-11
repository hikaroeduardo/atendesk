from fastapi import Body, APIRouter, status
from ..controllers.users.create_user_controller import CreateUserController
from ..controllers.users.login_controller import LoginController
from ..schemas.inputs.users.create_user_schema import DataCreateUser
from ..schemas.inputs.users.login_user_schema import DataLoginUser
from ..responses_docs.users.create_user import create_user_docs
from ..responses_docs.users.login import login_docs

router = APIRouter(tags=['users'], prefix="/user")

@router.post('/', status_code=status.HTTP_201_CREATED, summary="Criar novo usuário", responses={**create_user_docs})
async def create_user(data_user: DataCreateUser = Body(examples=[
    {
        "name": "Admin Silva",
        "email": "teste@gmail.com",
        "username": "username_teste",
        "password": "admin123"
    }
])):
    """
    Endpoint para criação de um novo usuário para o sistema
    """
    return await CreateUserController.create(data_user)

@router.post('/login', summary="Login", status_code=status.HTTP_200_OK, responses={**login_docs})
async def login(user_data: DataLoginUser = Body(examples=[
    {
        "username": "username_teste",
        "password": "admin123"
    }
])):
    """
    Endpoint para login de usuário
    """
    return await LoginController.login(user_data)
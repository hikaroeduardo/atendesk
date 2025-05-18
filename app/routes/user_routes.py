from fastapi import Body, APIRouter, status
from ..controllers.users.create_user_controller import CreateUserController
from ..schemas.inputs.users.create_user_schema import DataCreateUser

router = APIRouter(tags=['users'], prefix="/user")

@router.post('/', status_code=status.HTTP_201_CREATED, summary="Criar novo usuário", responses={
    "201": {
        "description": "CREATED",
        "content": {
            "application/json": {
                "example": {"success": "Usuário cadastrado com sucesso!"}
            }
        }
    },
    "400": {
        "description": "BAD REQUEST",
        "content": {
            "application/json": {
                "example": {"detail": "Campos obrigatórios faltando. Dados faltantes: ['dado_faltante']"}
            }
        }
    },
    "422": {
        "description": "UNPROCESSABLE_ENTITY",
        "content": {
            "application/json": {
                "example": {"detail": "Este usuário ja existe em nosso sistema."}
            }
        }
    },
    "500": {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Erro ao cadastrar novo usuário, tente novamente mais tarde!"}
            }
        }
    }
})
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
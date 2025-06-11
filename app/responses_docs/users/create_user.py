create_user_docs = {
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
}
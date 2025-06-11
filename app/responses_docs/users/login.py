login_docs = {
    "200": {
        "description": "OK",
        "content": {
            "application/json": {
                "example": {
                    "token": "token"
                }
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
    "401": {
        "description": "UNAUTHORIZED",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Credenciais incorretas."
                }
            }
        }
    },
    "500": {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Não foi possível fazer o login, tente novamente mais tarde!"}
            }
        }
    }
}
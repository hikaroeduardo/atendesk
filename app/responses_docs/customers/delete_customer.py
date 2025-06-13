delete_customer_docs = {
    "200": {
        "description": "OK",
        "content": {
            "application/json": {
                "example": {"success": "Cliente deletado com sucesso!"}
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
    "404": {
        "description": "NOT_FOUND",
        "content": {
            "application/json": {
                "example": {"detail": "Cliente não encontrado."}
            }
        }
    },
     "500": {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Erro ao deletar cliente, tente novamente mais tarde!"}
            }
        }
    }
}
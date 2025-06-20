update_status_ticket_docs = {
    "200": {
        "description": "OK",
        "content": {
            "application/json": {
                "example": {"success": "Status alterado com sucesso!"}
            }
        }
    },
    "400": {
        "description": "BAD REQUEST",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Campo de novo status está vazio."
                }
            }
        }
    },
    "401": {
        "description": "UNAUTHORIZED",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Você não pode atualizar este ticket com este usuário."
                }
            }
        }
    },
    "404": {
        "decription": "NOT FOUND",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Ticket não encontrado."
                }
            }
        }
    },
    "500": {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Erro ao cadastrar novo cliente, tente novamente mais tarde!"}
            }
        }
    }
}
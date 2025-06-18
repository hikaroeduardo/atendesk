create_ticket_docs = {
    "201": {
        "description": "CREATED",
        "content": {
            "application/json": {
                "example": {"success": "Ticket criado com sucesso."}
            }
        }
    },
    "400": {
        "description": "BAD REQUEST",
        "content": {
            "application/json": {
                "examples": {
                    "Missing Fields": {
                        "summary": "Campos obrigatórios faltantdo",
                        "value": {
                            "detail": "Campos obrigatórios faltando. Dados faltantes: ['dado_faltante']"
                            }
                        },
                    "Ticket With Different User": {
                        "summary": "Ticket com usuário diferente do logado",
                        "value": {
                            "detail": "Você não pode criar este ticket com este usuário."
                        }
                    }
                }
            }
        }
    },
    "404": {
        "decription": "NOT FOUND",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Cliente não encontrado."
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
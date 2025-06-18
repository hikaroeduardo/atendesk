list_tickets_docs = {
    "200": {
        "description": "OK",
        "content": {
            "application/json": {
                "example": [
                    {
                        "ticket": {
                            "name": "nome chamado",
                            "status": "Aberto",
                            "description": "descrição chamado"
                        },
                        "customer": {
                            "name": "nome cliente",
                            "email": "cliente@gmail.com",
                            "phone": "86998000000"
                        }
                    }
                ]
            }
        }
    },
    "500": {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Não foi possível listar os tickets. Tente novamente mais tarde!"}
            }
        }
    }
}
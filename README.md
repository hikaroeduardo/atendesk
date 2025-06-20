# API Atendesk

**Atendesk** é uma API desenvolvida em **Python** com **FastAPI** e **SQLModel**, focada no gerenciamento de chamados (tickets).
Oferece recursos como autenticação via JWT, documentação automática e endpoints organizados para uma integração rápida e segura.

## Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI** – Framework web rápido e moderno
- **SQLModel** – ORM baseado em SQLAlchemy e Pydantic
- **JWT (JSON Web Token)** – Autenticação segura via tokens
- **Swagger UI / Redoc** – Documentação para visualizar e testar a API de forma interativa.

---

## Autenticação

A API utiliza **autenticação via JWT**. Após o login, o token JWT deve ser enviado no header `Authorization` no formato:

```
Authorization: Bearer <token_jwt>
```

---

## Documentação Interativa

Após iniciar a aplicação, acesse:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

Todos os endpoints estão documentados, incluindo exemplos de requisições, respostas esperadas e status codes.

---

## Endpoints Disponíveis

### Users

- **Criar novo usuário**
  - `POST /user`
  - Cadastra um novo usuário.

- **Login**
  - `POST /login`
  - Realiza autenticação e retorna um token JWT.

---

### Customers

- **Criar novo cliente**
  - `POST /customer`
  - Adiciona um novo cliente para ser associado aos tickets.

- **Deletar cliente**
  - `DELETE /customers` (Deve passar customer_id via query params)
  - Remove um cliente existente do usuário logado.

---

### Tickets

- **Criar ticket**
  - `POST /ticket`
  - Registra um novo chamado na plataforma.

- **Listar tickets (com filtro de status)**
  - `GET /tickets?status=aberto|fechado|pendente`
  - Lista os tickets, podendo filtrar por status.

- **Atualizar status do ticket**
  - `PATCH /tickets/{ticket_id}` (Deve passar status via body)
  - Atualiza o status do chamado (ex: aberto → fechado).

---

## Executando o Projeto Localmente

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/atendesk.git
cd atendesk
```

2. **Crie e ative um ambiente virtual**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Rode a aplicação**

```bash
fastapi dev app/main.py
```

---

## Segurança

- Autenticação via JWT
- Validação de dados com Pydantic
- Status codes claros para facilitar o consumo da API por front-ends

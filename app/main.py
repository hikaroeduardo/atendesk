import os
from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from .database import create_all_tables
from .routes.user_routes import router as user_routes
from .routes.customer_routes import router as customer_routes
from .routes.ticket_routes import router as ticker_routes

app = FastAPI(title="Atendesk", version="1.0.0")

app.include_router(user_routes)
app.include_router(customer_routes)
app.include_router(ticker_routes)

@app.exception_handler(RequestValidationError)
async def validation_error(request, exc: RequestValidationError):
    errors = exc.errors()
    missing_error = []

    for err in errors:
        if err.get("type") == "missing":
            input_missing = err.get('loc')[1]
            missing_error.append(input_missing)

    return JSONResponse(content={
        "detail": f"Campos obrigatórios faltando. Dados faltantes: {missing_error}"
    }, status_code=status.HTTP_400_BAD_REQUEST)

@app.on_event("startup")
def startup_event():
    path_raiz = os.getcwd()
    path_database = os.path.join(path_raiz, "database.db")

    if not os.path.exists(path_database):
        create_all_tables()
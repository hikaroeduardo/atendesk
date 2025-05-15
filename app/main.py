import os
from fastapi import FastAPI
from .database import create_all_tables

app = FastAPI()

@app.on_event("startup")
def startup_event():
    path_raiz = os.getcwd()
    path_database = os.path.join(path_raiz, "database.db")

    if not os.path.exists(path_database):
        create_all_tables()
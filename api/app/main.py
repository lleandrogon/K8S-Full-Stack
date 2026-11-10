from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/produtos")
def listar_produtos():

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT
            id,
            nome,
            preco
        FROM produtos
        ORDER BY id
    """)

    produtos = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": p[0],
            "nome": p[1],
            "preco": float(p[2])
        }
        for p in produtos
    ]
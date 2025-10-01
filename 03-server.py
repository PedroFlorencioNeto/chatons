import uvicorn
from DeepSeek import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="ChatONS", description="Explore os conjuntos de dados do Portal de Dados Abertos do ONS")

add_routes(app, chain, path="/chat")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
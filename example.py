from fastapi import FastAPI
from orders import router as orders_router

app = FastAPI()

app.include_router(orders_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hola")
def read_root_hola():
    return {"message": "Hola Mundo Querido"}

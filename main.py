from fastapi import FastAPI
from routes.libros_route import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return 1
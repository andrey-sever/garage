from fastapi import FastAPI
from professions.router import router as router_professions


app = FastAPI()

app.include_router(router_professions)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

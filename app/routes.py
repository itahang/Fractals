from fastapi import APIRouter

routes = APIRouter()

@routes.get("/")
def hello():
    return "Hello world"
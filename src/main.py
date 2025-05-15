from fastapi import FastAPI
from fastapi import routing
from .routes import routes

app = FastAPI()
app.add_route(routes)
from fastapi import FastAPI
from fastapi import routing
from .routes import routes
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(routes)
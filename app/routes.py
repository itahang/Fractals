from fastapi import APIRouter
from .mandelbrot import mandelBrotWrapper
from fastapi.responses import HTMLResponse
from .utils import image_to_base64,genImage
routes = APIRouter()

@routes.get("/")
def hello():
    return "Hello world"


@routes.get("/mandel", response_class=HTMLResponse)
async def hmande(
    width: int = 1080,
    height: int = 1080,
    zoom: float = 1000.0,
    center_x: float = -0.5,
    center_y: float = 0.0
):
    image = mandelBrotWrapper(width, height, zoom)
    genImage(image)

    with open("static/index.html", "r") as f:
        html_content = f.read()

    return HTMLResponse(content=html_content)

# @routes.get("/mandel",response_class=HTMLResponse)
# async def hmande():
#     image= mandelBrotWrapper(1080,1080,1000.0)
#     genImage(image)
#     with open("static/index.html", "r") as f:
#         html_content = f.read()

#     return HTMLResponse(content=html_content)

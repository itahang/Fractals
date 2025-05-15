from fastapi import APIRouter
from .mandelbrot import mandelBrotWrapper
from fastapi.responses import HTMLResponse
from .utils import image_to_base64
routes = APIRouter()

@routes.get("/")
def hello():
    return "Hello world"

@routes.get("/mandel",response_class=HTMLResponse)
def hmande():
    image= mandelBrotWrapper(1080,1080,100.0)
    b64_img = image_to_base64(image)
    
    html = f"""
    <html>
    <body>
        <h2>Mandelbrot Image</h2>
        <img src="data:image/png;base64,{b64_img}" />
    </body>
    </html>
    """
    return HTMLResponse(content=html)
    
    
    
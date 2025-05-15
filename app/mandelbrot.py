import os
import ctypes
from pathlib import Path
import numpy as np
import cv2 as cv

if os.name == "nt":
    lib_path = Path(__file__).parent.parent / "libs" / "mandelbrot.dll"
elif os.name == "posix":
    lib_path = Path(__file__).parent.parent / "libs" / "mandelbrot.so"
else:
    print(f"Does not support OS: {os.name}")
    os._exit(-1)

print("Loading library from:", lib_path)
cuda_lib = ctypes.CDLL(str(lib_path))

cuda_lib.mandelbrot_gpu.argtypes = [
    ctypes.POINTER(ctypes.c_uint),
    ctypes.c_uint,
    ctypes.c_uint,
    ctypes.c_double
]



def mandelBrotWrapper(width,height,zoom):
    
    image = np.zeros((height, width), dtype=np.uint32)

    cuda_lib.mandelbrot_gpu(
        image.ctypes.data_as(ctypes.POINTER(ctypes.c_uint)),
        ctypes.c_uint(width),
        ctypes.c_uint(height),
        ctypes.c_double(zoom)
    )
    return image


    



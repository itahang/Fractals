import pytest
from pathlib import Path
import ctypes
import os

lib_path = ""

if os.name == "nt":
    lib_path = Path(__file__).parent.parent / "libs" / "mandelbrot.dll"
elif os.name == "posix":
    lib_path = Path(__file__).parent.parent / "libs" / "mandel.so"


def try_loadingLibrary():
    try:
        cuda_lib = ctypes.CDLL(str(lib_path))
    except OSError as e:
        pytest.fail(f"Fail to load cuda library")

def test_loading():
    try_loadingLibrary()

def test_function_exist():
    cuda_lib = ctypes.CDLL(str(lib_path))
    func = getattr(cuda_lib, "mandelbrot_gpu", None)
    assert func is not None, "mandelbrot_gpu function is missing"



import cv2
import base64
import numpy as np

def genImage(image: np.ndarray):
    image = (image & 0xFF).astype(np.uint8) 
    cv2.imwrite("static/temp1.png",image)

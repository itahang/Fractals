import cv2
import base64
import numpy as np

def image_to_base64(image: np.ndarray) -> str:
    image = (image & 0xFF).astype(np.uint8) 
    success, encoded_image = cv2.imencode('.png', image)
    if not success:
        raise ValueError("Image encoding failed")
    b64_str = base64.b64encode(encoded_image).decode('utf-8')
    return b64_str
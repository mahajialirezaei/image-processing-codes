# coding: utf-8

import cv2
import numpy as np
import math
def black_white_convertor(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    background_pixel = np.argmax(hist)

    mask = np.where(gray == background_pixel, 255, 0).astype(np.uint8)

    final_result = mask
    return final_result

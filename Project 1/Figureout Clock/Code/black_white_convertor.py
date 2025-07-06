# coding: utf-8

import cv2
import numpy as np
def black_white_convertor(image):
    bg = image[0,0]
    mask = np.all(image == bg, axis=-1)
    out = np.zeros_like(image)
    out[mask] = [255,255,255]
    return cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

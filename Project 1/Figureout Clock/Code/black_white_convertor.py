# coding: utf-8

import cv2
import numpy as np
def black_white_convertor(image):
    x = image[0, 0]
    mask = np.all(image == x, axis=-1)

    final_image = np.zeros_like(image)
    final_image[mask] = [255, 255, 255]

    final_image_gray = cv2.cvtColor(final_image, cv2.COLOR_BGR2GRAY)
    final_image = final_image_gray
    return final_image

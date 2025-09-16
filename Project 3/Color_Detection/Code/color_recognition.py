# coding: utf-8

import cv2
import numpy as np
def color_recognition(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
    row, col = otsu.shape
    cropped_region = otsu[int(row*0.4):int(row*0.6), int(col*0.1):int(col*0.9)]
    white_ratio = len(cropped_region[cropped_region == 255])
    black_ratio = len(cropped_region[cropped_region == 0])
    if white_ratio > black_ratio:
        color = "white"
    else:
        color = "black"

    return color

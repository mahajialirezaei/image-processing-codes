# coding: utf-8

import cv2
import numpy as np
def coin_counter(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    # Apply Erosion technique to remove noise
    eroded = cv2.erode(binary, kernel, iterations=1)
    eroded = cv2.medianBlur(eroded, 7)
    kernel = np.ones((3, 3), np.uint8)
    # Apply Dilation technique to fill coins
    # Apply Dilation on `eroded` variable and make sure the iterations been 3 times
    dilated = cv2.dilate(eroded, kernel, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by area to remove noise (we only select those contours which their area is more than 4000)
    min_area = 4000 # Adjust this based on your coin size
    max_area = 40000
    filtered_contours = [cnt for cnt in contours if max_area > cv2.contourArea(cnt) > min_area]
    return len(filtered_contours)

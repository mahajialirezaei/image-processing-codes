import cv2, numpy as np
from matplotlib import pyplot as plt


def detect_played(address):
    img = cv2.imread(address)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_bound_red1 = np.array([0, 100, 100])
    upper_bound_red1 = np.array([10, 255, 255])
    lower_bound_red2 = np.array([160, 100, 100])
    upper_bound_red2 = np.array([179, 255, 255])

    mask_red_1 = cv2.inRange(img, lower_bound_red1, upper_bound_red1)
    mask_red_2 = cv2.inRange(img, lower_bound_red2, upper_bound_red2)

    mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)

    lower_bound_yellow = np.array([20, 100, 100])
    upper_bound_yellow = np.array([30, 255, 255])

    mask_yellow = cv2.inRange(img, lower_bound_yellow, upper_bound_yellow)

    mask = cv2.bitwise_or(mask_red, mask_yellow)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    plt.imshow(mask, cmap='gray')
    plt.show()


detect_played('Data/test data_2.jpg')
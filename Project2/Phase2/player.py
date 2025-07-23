import cv2
import numpy as np


def detect_player(address):
    img_bgr = cv2.imread(address)

    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    img_ycrcb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)


    lower_red1 = np.array([0, 40, 25])
    upper_red1 = np.array([12, 255, 255])
    lower_red2 = np.array([160, 40, 25])
    upper_red2 = np.array([179, 255, 255])

    mask_red1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(img_hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    lower_yellow = np.array([20, 40, 25])
    upper_yellow = np.array([37, 255, 255])
    mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

    hsv_mask = cv2.bitwise_or(mask_red, mask_yellow)


    lower_ycrcb = np.array([0, 135, 85])
    upper_ycrcb = np.array([255, 180, 135])
    ycrcb_mask = cv2.inRange(img_ycrcb, lower_ycrcb, upper_ycrcb)

    mask = cv2.bitwise_and(hsv_mask, ycrcb_mask)

    mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    return mask

# from matplotlib import pyplot as plt
# ms = detect_player('Data/test Data_1.jpg')
# ms2 = detect_player('Data/test Data_2.jpg')
# ms3 = detect_player('Data/test Data_3.jpg')
# ms4 = detect_player('Data/test Data_4.jpg')
# plt.figure(figsize=(10, 10))
# plt.imshow(ms)
# plt.show()
# plt.imshow(ms2)
# plt.show()
# plt.imshow(ms3)
# plt.show()
# plt.imshow(ms4)
# plt.show()
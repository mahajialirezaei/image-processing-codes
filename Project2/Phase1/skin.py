import cv2
import numpy as np
# from matplotlib import pyplot as plt


# from matplotlib import pyplot as plt


def detect_skin(address):
    img = cv2.imread(address)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, w = img.shape[:2]

    sample_region = img_hsv[int(h*0.4):int(h*0.6), int(w*0.4):int(w*0.6)]

    mean = sample_region.reshape(-1, 3).mean(axis=0)
    hue_mean, sat_mean, val_mean = mean

    lower_bound = np.array([
        max(hue_mean - 20, 0),
        max(sat_mean - 50, 40),
        max(val_mean - 50, 40)
    ], dtype=np.uint8)
    upper_bound = np.array([
        min(hue_mean + 20, 179),
        sat_mean + 40,
        val_mean + 45
    ], dtype=np.uint8)

    mask = cv2.inRange(img_hsv, lower_bound, upper_bound)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    skin = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)


    return skin


sk = detect_skin('sample/image_two.jpg')
from matplotlib import pyplot as plt
plt.imshow(sk)
plt.show()
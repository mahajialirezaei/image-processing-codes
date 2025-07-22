import cv2, numpy as np
import matplotlib.pyplot as plt

def detect_skin(address):
    img = cv2.imread(address)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    x, y = img.shape[:2]
    expected = img_hsv[int(x//2 * 0.6):int(x//2 * 1.2), int(y//2 * 0.6):int(y//2 * 1.2)]
    hue_mean, sat_mean, val_mean = (0, 0, 0)
    numbers_pix = expected.shape[0] * expected.shape[1]
    mean = expected.reshape(-1, 3).mean(axis=0)
    hue_mean, sat_mean, val_mean = mean
    print(hue_mean, sat_mean, val_mean)

    upper_bound = np.array([
        min(hue_mean * 1.2, 179),
        min(sat_mean * 1.2, 255),
        min(val_mean * 1.2, 255)
    ], dtype=np.uint8)

    lower_bound = np.array([
        max(hue_mean * 0.8, 0),
        max(sat_mean * 0.8, 0),
        max(val_mean * 0.8, 0)
    ], dtype=np.uint8)

    mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
    plt.imshow(mask, cmap='gray')
    plt.show()


detect_skin('sample/image_one.jpg')
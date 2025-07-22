import cv2


def detect_skin(address):
    img = cv2.imread(address)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    x, y = img.shape[:2]
    expected = img_hsv[int(x//2 * 0.8):int(x//2 * 1.2), int(y//2 * 0.8):int(y//2 * 1.2)]
    hue_mean, sat_mean, val_mean = (0, 0, 0)
    numbers_pix = expected.shape[0] * expected.shape[1]
    for row in expected:
        for col in row:
            print(col)
            hue_mean += col[0]
            sat_mean += col[1]
            val_mean += col[2]
    hue_mean /= numbers_pix
    sat_mean /= numbers_pix
    val_mean /= numbers_pix
    upper_bound = [min(hue_mean * 1.2, 360), min(sat_mean * 1.2, 255) , min(val_mean * 1.2, 255)]
    lower_bound = [hue_mean * 0.8, sat_mean * 0.8, val_mean * 0.8]
    mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
    cv2.imshow('mask', mask)
    cv2.show()
detect_skin('sample/image_one.jpg')
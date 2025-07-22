import cv2


def detect_played(address):
    img = cv2.imread(address)
    lower_bound_red1 = [0, 100, 100]
    upper_bound_red1 = [10, 255, 255]
    lower_bound_red2 = [160, 100, 100]
    upper_bound_red2 = [179, 255, 255]

    mask_red_1 = cv2.inRange(img, lower_bound_red1, upper_bound_red1)
    mask_red_2 = cv2.inRange(img, lower_bound_red2, upper_bound_red2)

    mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)

    lower_bound_yellow = [20, 100, 100]
    upper_bound_yellow = [30, 255, 255]

    mask_yellow = cv2.inRange(img, lower_bound_yellow, upper_bound_yellow)

    mask = cv2.bitwise_or(mask_red, mask_yellow)


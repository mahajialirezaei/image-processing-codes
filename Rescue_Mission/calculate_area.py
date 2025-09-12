import cv2
import numpy as np


def gray_mask_bgr(img, diff_thresh=15, gray_min=50, gray_max=220):
    b, g, r = cv2.split(img)
    dbg = cv2.absdiff(b, g)
    dbr = cv2.absdiff(b, r)
    dgr = cv2.absdiff(g, r)

    diff_mask = (dbg <= diff_thresh) & (dbr <= diff_thresh) & (dgr <= diff_thresh)

    intensity = ((b.astype(np.int16) + g.astype(np.int16) + r.astype(np.int16)) // 3)
    intensity_mask = (intensity >= gray_min) & (intensity <= gray_max)

    mask = (diff_mask & intensity_mask).astype(np.uint8) * 255
    return mask


def check_all_col(res):
    for c, a in res.items():
        if a > 0:
            return True
    return False

def calculate_area(image):
    ranges = {
        'red': (np.array([0, 0, 100], dtype=np.uint8), np.array([120, 120, 255], dtype=np.uint8)),
        'green': (np.array([0, 100, 0], dtype=np.uint8), np.array([120, 255, 120], dtype=np.uint8)),
        'blue':   (np.array([100, 0,   0], dtype=np.uint8), np.array([255, 120, 120], dtype=np.uint8)),
        'yellow': (np.array([0, 150, 150], dtype=np.uint8), np.array([120, 255, 255], dtype=np.uint8)),
        'purple': (np.array([100, 0, 100], dtype=np.uint8), np.array([255, 120, 255], dtype=np.uint8)),
        'gray':   None
    }

    res = {c: 0 for c in ranges}

    for color, r in ranges.items():
        if color == 'gray':
            msk = gray_mask_bgr(image)
        else:
            msk = cv2.inRange(image, r[0], r[1])

        kernel = np.ones((5, 5), np.uint8)
        msk = cv2.morphologyEx(msk, cv2.MORPH_OPEN, kernel)
        msk = cv2.morphologyEx(msk, cv2.MORPH_CLOSE, kernel)

        cnts, _ = cv2.findContours(msk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            area = cv2.contourArea(c)
            arcLength = cv2.arcLength(c, True)

            if (arcLength / 4) ** 2 == area:
                res[color] += area
            else:
                res[color] += area * 3
        res[color] = int(res[color])
    txt = ''
    if check_all_col(res):
        for c, a in res.items():
            if a > 0:
                txt += c + ',' + ' ' + str(a) + '\n'
    else:
        txt = 'black' + ',' + ' ' + str(image.shape[0] * image.shape[1])


    return txt
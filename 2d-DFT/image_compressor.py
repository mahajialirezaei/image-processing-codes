import math

import cv2
import numpy as np
from scipy.fft import fft2, ifft2

def compress(image_path, block_size=32, tol=0.001):
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        raise FileNotFoundError(f"Cannot open image: {image_path}")
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY).astype(np.float64)

    H, W = img_gray.shape[:2]
    compressed = np.zeros_like(img_gray)

    for i in range(0, H, block_size):
        for j in range(0, W, block_size):
            blk = img_gray[i:i + block_size, j:j + block_size]
            F = fft2(blk)
            F_abs = np.abs(F)
            F_max = F_abs.max() if F_abs.size > 0 else 0.0
            threshold = tol * F_max
            mask = (F_abs >= threshold)
            F_compressed = F * mask
            inv_blk = ifft2(F_compressed)
            inv_blk_real = np.real(inv_blk)
            compressed[i:i + block_size, j:j + block_size] = inv_blk_real

    h_orig, w_orig = img_gray.shape
    result = compressed[:h_orig, :w_orig]
    result = np.clip(result, 0, 255)
    result_uint8 = np.rint(result).astype(np.uint8)
    return result_uint8

def mse(img1, img2):
    a = img1.astype(np.float64)
    b = img2.astype(np.float64)
    return np.mean((a - b) ** 2)
def psnr(img1, img2, max_pixel=255.0):
    m = mse(img1, img2)
    if m == 0:
        return float('inf')
    return 10.0 * math.log10((max_pixel ** 2) / m)

# img_bgr = cv2.imread('operahall.jpg')
# if img_bgr is None:
#     raise FileNotFoundError("Cannot open operahall.jpg")
# orig_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
# compressed = compress('operahall.jpg')
# mse1 = mse(orig_gray, compressed)
# psnr1 = psnr(compressed, orig_gray)
# print(mse1)
# print(psnr1)
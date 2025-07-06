# coding: utf-8
import cv2
import numpy as np
from scipy.stats import kurtosis, skew
def detect_gaussian_salt_pepper_noise(image):
    variance = np.var(image)
    std_dev = np.sqrt(variance)

    total_pixels = image.size

    # تعداد پیکسل های 0 و 255 برای نویز salt-and-pepper
    num_salt = np.sum(image == 255)
    num_pepper = np.sum(image == 0)
    ratio_salt_pepper = (num_salt + num_pepper) / total_pixels

    # شرایط تشخیص نویز salt and pepper
    if ratio_salt_pepper > 0.005:  # این مقدار ممکن است بسته به داده تغییر کند
        return "Salt-and-Pepper"

    # شرایط تشخیص Gaussian noise - واریانس بالا نسبت به تصویر بدون نویز
    # بسته به تصویر اصلی این مقدار را تنظیم کنید، عدد نمونه:
    if std_dev > 15:
        return "Gaussian"

    # در غیر اینصورت نویزی وجود ندارد
    return "No Noise"

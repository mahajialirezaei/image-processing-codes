# coding: utf-8

import cv2
import numpy as np
import math
def calculate_time(line_hour, line_minute, center):
    from math import degrees, atan2
    h_x_mid, h_y_mid = (line_hour[0] + line_hour[2]) / 2, (line_hour[1] + line_hour[3]) / 2
    m_x_mid, m_y_mid = (line_minute[0] + line_minute[2]) / 2, (line_minute[1] + line_minute[3]) / 2
    dy_h, dx_h = h_y_mid - center[1], h_x_mid - center[0]
    deg_h = (degrees(atan2(dy_h, dx_h)) + 90) % 360
    dy_m, dx_m = m_y_mid - center[1], m_x_mid - center[0]
    deg_m = degrees(atan2(dy_m, dx_m) + 90) % 360
    h = int(deg_h // 30) % 12
    m = int(deg_m // 6) % 60
    m = m//5 * 5
    if m == 60:
        m = 0
        h += 1
    h = str(h)
    m = str(m)
    if len(h) < 2:
        h = '0' + h
    if len(m) < 2:
        m = '0' + m

    time = h + ':' + m
    return time

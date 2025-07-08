# coding: utf-8

import cv2
import numpy as np
import math
def detect_clock(image):
    edges = cv2.Canny(image, 50, 150)

    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                              param1=30, param2=20, minRadius=238, maxRadius=243)

    if circles is None:
        print("دایره ساعت پیدا نشد!")
        return None, None, None

    circles = np.uint16(np.around(circles))
    circle = circles[0, 0]
    x, y, r = circle
    center = (x, y)

    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    cv2.circle(image_color, (x, y), r, (0, 255, 0), 2)
    cv2.circle(image_color, (x, y), 3, (0, 0, 255), -1)

    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=100, maxLineGap=10)

    if lines is None:
        print("هیچ خطی پیدا نشد!")
        return None, None, None, image_color

    valid_lines = []

    for i, line1 in enumerate(lines):
        x1, y1, x2, y2 = line1[0]
        length1 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        mid_x1, mid_y1 = (x1 + x2) / 2, (y1 + y2) / 2
        dist_from_center1 = np.sqrt((mid_x1 - center[0])**2 + (mid_y1 - center[1])**2)

        if dist_from_center1 < r / 2 and length1 > 100:
            angle1 = math.degrees(math.atan2(y2 - y1, x2 - x1))
            angle1 = (angle1 + 360) % 360  # زاویه بین 0 تا 360

            is_parallel = False
            for j, line2 in enumerate(valid_lines):
                x3, y3, x4, y4 = line2[0]
                length2 = np.sqrt((x4 - x3)**2 + (y4 - y3)**2)
                angle2 = math.degrees(math.atan2(y4 - y3, x4 - x3))
                angle2 = (angle2 + 360) % 360

                if abs(angle1 - angle2) < 10 or abs(angle1 - angle2) > 350:
                    is_parallel = True
                    if length1 > length2:
                        valid_lines[j] = line1
                    break
            if not is_parallel:
                valid_lines.append(line1)

    max_length1, max_length2 = 0, 0
    line_hour, line_minute = None, None

    for line in valid_lines:
        x1, y1, x2, y2 = line[0]
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if length > max_length1:
            max_length2 = max_length1
            line_hour = line_minute
            line_minute = line
            max_length1 = length
        elif length > max_length2:
            max_length2 = length
            line_hour = line

    if line_hour is not None:
        x1, y1, x2, y2 = line_hour[0]
        cv2.line(image_color, (x1, y1), (x2, y2), (0, 0, 255), 2)


    if line_minute is not None:
        x1, y1, x2, y2 = line_minute[0]
        cv2.line(image_color, (x1, y1), (x2, y2), (0, 255, 0), 2)



    return line_hour[0], line_minute[0], center

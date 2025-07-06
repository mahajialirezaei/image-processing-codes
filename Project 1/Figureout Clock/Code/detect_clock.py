# coding: utf-8

import cv2
import numpy as np
def detect_clock(binary_image):
    gray = black_white_convertor(binary_image)
    gray_blur = cv2.GaussianBlur(gray, (9,9), 2)

    edges = cv2.Canny(gray_blur, threshold1=50, threshold2=150)

    h, w = gray.shape
    minR = int(min(h,w)*0.4)
    maxR = int(min(h,w)*0.5)

    circles = cv2.HoughCircles(
        image=gray_blur,
        method=cv2.HOUGH_GRADIENT,
        dp=1.0,
        minDist=100,
        param1=200,
        param2=60,
        minRadius=minR,
        maxRadius=maxR
    )

    circles = np.uint16(np.around(circles[0]))
    cx, cy, radius = max(circles, key=lambda x: x[2])
    print(cx, cy, radius)
    img3channel = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.circle(img3channel, (cx, cy), radius, (0,255,0), 2)


    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi/180,
        threshold=50,
        minLineLength=int(radius*0.3),
        maxLineGap=20
    )

    def line_length(l):
        x1,y1,x2,y2 = l
        return np.hypot(x2-x1, y2-y1)

    valid = []
    for l in lines[:,0]:
        x1,y1,x2,y2 = l
        if (np.hypot(x1-cx, y1-cy) < radius*0.2) or (np.hypot(x2-cx, y2-cy) < radius*0.2):
            valid.append(l)



    def valid_lines_cr(ls_lines):
        sorted(valid, key=line_length, reverse=True)
        line_minute = ls_lines[0]
        line_hour = ls_lines[1]
        if line_minute[0] / line_minute[1] - line_hour[0] / line_hour[1] < 0.1:
            ls_lines.remove(line_minute)
            return valid_lines_cr(ls_lines)
        return line_minute, line_hour

    line_minute, line_hour = valid_lines_cr(valid)

    cv2.line(img3channel, (line_minute[0],line_minute[1]), (line_minute[2],line_minute[3]), (0,255,0), 3)
    cv2.line(img3channel, (line_hour[0],line_hour[1]),     (line_hour[2],line_hour[3]),     (255,0,0), 3)

    plt.figure(figsize=(6,6))
    plt.imshow(cv2.cvtColor(img3channel, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Clock")
    plt.show()
    return img3channel

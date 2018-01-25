#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import imutils
import sys
import platform
from cv_image_show import print_version_params, simple_image_show
from math import sqrt

def image_mask(image, lower_limit=(163, 77, 94), upper_limit=(188, 255, 169), erode_iters=2, dilate_iters=2):
    """
    Fuction takes in an OpenCV image object or frame and outputs a mask object of the same size
    :param image: an OpenCV image object, from cv2.capture()
    :param lower_limit: lower hsv limit, tuple of the form (h,s,v), Default = (163, 77, 94)
    :param upper_limit: upper hsv limit, tuple of the form (h,s,v), Default = (188, 255, 169)
    :param erode_iters: number of cv2.erode() iterations. Default=2
    :param dilate_iters: number of cv2.dilate() iterations. Default=2
    :return: mask, an OpenCV image object
    """

    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)  #convert to hsv colorspace

    # construct mask
    mask = cv2.inRange(hsv, lower_limit, upper_limit)
    mask = cv2.erode(mask, None, iterations=erode_iters)
    mask = cv2.dilate(mask, None, iterations=dilate_iters)

    return(mask)


def measure_dot_distance(mask_image, int_out=False):
    """

    :param mask_image: an OpenCV mask image object. Binary mask like the output of the cv_tools.image_mask() function
    :param  int_out: Set to True to output and integer. Default = False, output is a float
    :return: d, distance between two contour ojects in the mask
    """
    # find the contours of the mask
    cnts = cv2.findContours(mask_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # only proceed if at least 1 contour if found
    if len(cnts) > 0:
        # find the largest contour first
        c1 = cnts[0]
        ((x, y), radius) = cv2.minEnclosingCircle(c1)
        M1 = cv2.moments(c1)
        center1 = (int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"]))
        #print('Center of Dot 1 coordinates = {}'.format(center1))

        c2 = cnts[1]
        ((x, y), radius) = cv2.minEnclosingCircle(c2)
        M2 = cv2.moments(c2)
        center2 = (int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"]))
        #print('Center of Dot 2 coordinates = {}'.format(center2))

        d = (center1[0] - center2[0], center1[1] - center2[1])
        d = sqrt(d[0] ** 2 + d[1] ** 2)
        # print('distance between dots: {} px'.format(round(d,2)))
        if int_out==True:
            d =int(d)
    return (d)

def save_one_frame(video_file, width=300, show_image=True):
    cap = cv2.VideoCapture(video_file)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if frame is not None:
            frame = imutils.resize(frame, width=width)
            if show_image == True:
                cv2.imshow('Press [q] to close', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    return(frame)

#image = save_one_frame('IMG_3391.MOV')

#cv2.imwrite('big_red_dots.png', image)
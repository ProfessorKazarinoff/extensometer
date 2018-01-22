#!/usr/bin/env python

import cv2
import numpy as np
import imutils
import sys
import platform
from cv_image_show import print_version_params, simple_image_show

def red_dot_pixel_distance(image_path):
    lowerRed = (163, 77, 94)     # use https://github.com/jrosebr1/imutils/blob/master/bin/range-detector
    upperRed =  (188, 255, 169)

    # import the image, resize and convert to hsv
    frame = cv2.imread(image_path)              # import image
    frame = imutils.resize(frame,height=600)     # resize
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  #convert to hsv colorspace

    # construct mask
    mask = cv2.inRange(hsv,lowerRed,upperRed)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow('mask',mask)
    cv2.waitKey(0)
    # see: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
    pixel_distance = 32
    return(pixel_distance)


def main():
    print_version_params()
    simple_image_show('tensile_bar_with_red_dots_cropped.jpg')
    red_dot_pix_dist = red_dot_pixel_distance('tensile_bar_with_red_dots_cropped.jpg')
    print('Distance in pixels between the two red dots: {} px'.format(red_dot_pix_dist))

if __name__ =="__main__":
    main()

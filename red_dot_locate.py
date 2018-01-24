#!/usr/bin/env python

import cv2
import numpy as np
import imutils
import sys
import platform
from cv_image_show import print_version_params, simple_image_show
from math import sqrt

def make_red_mask(image_path):
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
    cv2.imshow('Press [ESC] to proceed',mask)
    cv2.waitKey(0)
    # see: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

    return(mask)

def measure_dot_distance(mask_image):
    #find the contours of the mask
    cnts = cv2.findContours(mask_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    #only proceed if at least 1 contour if found
    if len(cnts) > 0:
        #find the largest contour first
        c1 = cnts[0]
        ((x, y), radius) = cv2.minEnclosingCircle(c1)
        M1 = cv2.moments(c1)
        center1 = (int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"]))
        print(center1)

        
        c2 = cnts[1]
        ((x, y), radius) = cv2.minEnclosingCircle(c2)
        M2 = cv2.moments(c2)
        center2 = (int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"]))
        print(center2)


        d = (center1[0]-center2[0], center1[1]-center2[1])
        d = sqrt(d[0]**2 + d[1]**2)
        #print('distance between dots: {} px'.format(round(d,2)))

        return(d)

def main():
    print_version_params()
    simple_image_show('tensile_bar_with_red_dots_cropped.jpg')
    mask = make_red_mask('tensile_bar_with_red_dots_cropped.jpg')
    #print('Distance in pixels between the two red dots: {} px'.format(red_dot_pix_dist))
    dotdistance = measure_dot_distance(mask)
    print('distance between dots: {} px'.format(round(dotdistance, 2)))

if __name__ =="__main__":
    main()

#!/usr/bin/env python

import cv2
import numpy as np
import imutils
import sys
import platform
import matplotlib.pyplot as plt
from cv_image_show import print_version_params, simple_image_show

def matpltlib_hsv(image_path):
    #lowerRed = (169, 92, 115)     # red Hue values: 1-10 and red Hue values: 160-180
    #upperRed =  (175, 175, 150)

    # import the image, resize and convert to hsv
    frame = cv2.imread(image_path)              # import image
    frame = imutils.resize(frame,height=600)     # resize
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  #convert to hsv colorspace

    plt.imshow(hsv)
    plt.show()
    # construct mask
    #mask = cv2.inRange(hsv,lowerRed,upperRed)
    #mask = cv2.erode(mask, None, iterations=2)
    #mask = cv2.dilate(mask, None, iterations=2)
    #cv2.imshow('mask',mask)
    #cv2.waitKey(0)
    #pixel_distance = 32
    #return(pixel_distance)


def main():
    print_version_params()
    matpltlib_hsv('tensile_bar_with_red_dots_cropped.jpg')

if __name__ =="__main__":
    main()


cv2.waitKey(0)
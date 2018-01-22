import cv2
import numpy as np
import imutils
import sys
import platform

def print_version_params():
    """
    prints out the Operating system version and all the installed package verisons.
    :return:
    """
    print('Operating System: {} {}'.format(platform.uname()[0], platform.uname()[2]))
    print('Python version: {}.{}.{}'.format(sys.version_info.major,sys.version_info.minor,sys.version_info.micro))
    print('OpenCV version: {}'.format(cv2.__version__))
    print('Numpy version: {}'.format(np.__version__))
    print('imutils version: {}'.format(imutils.__version__))

def simple_image_show(path_to_image):
    """
    Shows an image in a new window using OpenCV. Path to image must contain quotes and .jpg or other extension
    :param path_to_image:
    :return:
    """
    image = cv2.imread(path_to_image)
    cv2.imshow("Image Title", imutils.resize(image, height=600))
    cv2.waitKey(0)

def main():
    print_version_params()
    simple_image_show('tensile_bar_with_red_dots_cropped.jpg')

if __name__ =='__main__':
    main()
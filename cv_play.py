import cv2
import numpy as np
import imutils
import sys

def main():
    print('Python version: {}.{}.{}'.format(sys.version_info.major,sys.version_info.minor,sys.version_info.micro))
    print('OpenCV version: {}'.format(cv2.__version__))
    print('Numpy version: {}'.format(np.__version__))
    print('imutils version: {}'.format(imutils.__version__))

    image = cv2.imread("Plastic_spec_s.jpg")
    cv2.imshow("fracture", imutils.resize(image, width=400))
    cv2.waitKey(0)

if __name__ =='__main__':
    main()
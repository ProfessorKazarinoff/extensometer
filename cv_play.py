import cv2
import numpy as np
import imutils

def main():
    print('OpenCV version: {}'.format(cv2.__version__))
    print('Numpy version: {}'.format(np.__version__))
    print('imutils version: {}'.format(imutils.__version__))

    image = cv2.imread("fracture.png")
    cv2.imshow("fracture", imutils.resize(image, width=400))
    cv2.waitKey(0)

if __name__ =='__main__':
    main()
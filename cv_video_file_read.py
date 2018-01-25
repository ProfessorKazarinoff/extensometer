import cv2
import numpy as np
import imutils


cap = cv2.VideoCapture('IMG_3391.MOV')


if cap:
    print('captured video')
    print(cap.grab())



while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is not None:
        frame = imutils.resize(frame, height=300)

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #cv2.imshow('frame',gray)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

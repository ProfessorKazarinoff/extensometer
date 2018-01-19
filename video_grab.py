import numpy as np
import cv2
import time
from imutils.video import VideoStream
import imutils

cap = cv2.VideoCapture(0)
cap.set(3,160)
cap.set(4,120)

#vs = VideoStream(0,False,(320,240),15)
while True:
    ret, frame = cap.read()
    #frame = imutils.resize(frame, width=400)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)

    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
#
# if cap.isOpened():
#     print('Capture is open')
# else:
#     print('Capture is closed')
#     print('Opening Capture')
#     try:
#         cap.open()
#     except:
#         print('Tried to open the capture, but could not')
#
# check, read = cap.read()
# print(check)
# print(read)
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# When everything done, release the capture
cap.release()
#cv2.destroyAllWindows()
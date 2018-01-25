import cv2
import numpy as np
import imutils
import cv_tools

cap = cv2.VideoCapture('IMG_3391.MOV')

if cap:
    print('captured video')
    print(cap.grab())



while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is not None:
        frame = imutils.resize(frame, height=300)
        mask = cv_tools.image_mask(frame, (0, 145, 129), (255, 255, 255) )

        d = cv_tools.measure_dot_distance(mask, True)
        cv2.putText(frame, "Distance: {} px".format(d),
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
        #cv2.imshow('frame',gray)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

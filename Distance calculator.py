import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low = np.array([42, 51, 72])
    high = np.array([102, 255, 255])

    mask = cv2.inRange(hsv, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #print(len(contours))

    for contour in contours:
        if cv2.contourArea(contour) > 300:
            cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)
            Distance = 1134.6*((cv2.contourArea(contour))**(-0.497))

            text = 'Distance = ' + str(Distance)
            cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    cv2.imshow('result', result)
    cv2.imshow('mask', mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
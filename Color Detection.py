import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, frame =cap.read()

    if not success:
        print("Webcame not accessible")
        break

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Original Feed", frame)

    cv2.imshow("Color Mask", mask)

    cv2.imshow("Detected Blue", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
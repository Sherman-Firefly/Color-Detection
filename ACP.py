import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, frame =cap.read()

    if not success:
        print("Webcame not accessible")
        break

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    red_lower = np.array([136, 87, 111]) 
    red_upper = np.array([180, 255, 255]) 
    red_mask = cv2.inRange(hsv, red_lower, red_upper) 

	
    green_lower = np.array([25, 52, 72]) 
    green_upper = np.array([102, 255, 255]) 
    green_mask = cv2.inRange(hsv, green_lower, green_upper) 

	
    blue_lower = np.array([94, 80, 2]) 
    blue_upper = np.array([120, 255, 255]) 

    bmask = cv2.inRange(hsv, blue_lower, blue_upper)
    bresult = cv2.bitwise_and(frame, frame, mask=bmask)

    rmask = cv2.inRange(hsv, red_lower, red_upper)
    rresult = cv2.bitwise_and(frame, frame, mask=rmask)

    gmask = cv2.inRange(hsv, green_lower, green_upper)
    gresult = cv2.bitwise_and(frame, frame, mask=gmask)

    cv2.imshow("Original Feed", frame)

    cv2.imshow("Color Mask", bmask)
    cv2.imshow("Detected Blue", bresult)

    cv2.imshow("REd Color Mask", rmask)

    cv2.imshow("Detected Red", rresult)
    
    cv2.imshow("GreenColor Mask", gmask)

    cv2.imshow("Detected Green", gresult)
    
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
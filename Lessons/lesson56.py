import cv2
import numpy as np
camera = cv2.VideoCapture(0)
frame_count = 0
#camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
while True:
    success, frame = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red1 = np.array([0,120,70])
    high_red1 = np.array([10,255,255])
    low_red2 = np.array([170, 120, 70])
    high_red2 = np.array([179, 255, 255])
    mask1 = cv2.inRange(hsv, low_red1, high_red1)
    mask2 = cv2.inRange(hsv, low_red2, high_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    kernel = np.ones((3,3), np.uint8)
    result = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    frame_count+=1
    if frame_count == 100:
        background = frame.copy()
        print (background.shape)
    if not success:
        break
    inverse_mask = cv2.bitwise_not(result)
    #cv2.imshow("Invisible cloak", frame)
    #cv2.imshow("Masked frame", result)
    if frame_count>100:
        cloak = cv2.bitwise_and(background,background,mask = result)
        current = cv2.bitwise_and(frame,frame, mask = inverse_mask)
        cloak_region = cv2.add(cloak,current)
        cv2.imshow("Final Cloak",cloak_region)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
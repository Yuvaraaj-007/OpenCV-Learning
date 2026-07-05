import cv2
import pyautogui as pt
import mediapipe as mp
import math
import numpy as np
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
camera = cv2.VideoCapture(0)
pre_x = 0
pre_y = 0
smth = 5
#camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    success, frame = camera.read()
    if not success:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            tip = hand_landmarks.landmark[8]
            tip1 = hand_landmarks.landmark[4]
            pixel_x = int(tip.x*frame.shape[1])
            pixel_y = int(tip.y*frame.shape[0])
            pixel_x1= int(tip1.x*frame.shape[1])
            pixel_y1 = int(tip1.y*frame.shape[0])
            distance = math.sqrt((pixel_x-pixel_x1)**2 + (pixel_y-pixel_y1)**2)
            cv2.circle(frame, (pixel_x,pixel_y), 10, (0,255,0), 2)
            cv2.circle(frame, (pixel_x1,pixel_y1), 10, (0,255,0), 2)
            width, height = pt.size()
            x = np.interp(pixel_x, (0,frame.shape[1]),(0, width))
            y = np.interp(pixel_y, (0,frame.shape[0]),(0, height))
            cur_x = pre_x+(x-pre_x)/smth
            cur_y = pre_y+(y-pre_y)/smth
            pt.moveTo(cur_x, cur_y)
            pre_x = cur_x
            pre_y = cur_y
            #print(pixel_y,pixel_y1)
            if distance<18:
                   pt.click()
    cv2.imshow("Mouse detection", frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
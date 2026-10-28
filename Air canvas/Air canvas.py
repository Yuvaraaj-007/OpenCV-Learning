import cv2
import mediapipe as mp
import numpy as np
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
camera = cv2.VideoCapture(0)
x = 0
y = 0
success, frame = camera.read()
if not success:
    exit()
canvas = np.zeros_like(frame)
color = (0, 0, 255)
while True:
    success, frame = camera.read()
    if not success:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    cv2.rectangle(frame, (5,10),   (55,50),  (0,0,180), -1)   
    cv2.rectangle(frame, (65,10),  (115,50), (34, 139, 34), -1)   
    cv2.rectangle(frame, (125,10), (175,50), (180,0,0), -1)   
    cv2.rectangle(frame, (185,10), (235,50), (0,255,255), -1) 
    cv2.rectangle(frame, (245,10), (295,50), (0,0,0), -1)     
    cv2.rectangle(frame, (305,10), (355,50), (255,255,255), -1)
    cv2.putText(frame, "Clear", (310,35),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                tip = hand_landmarks.landmark[8]
                joint = hand_landmarks.landmark[6]
                tip1 = hand_landmarks.landmark[12]
                joint1 = hand_landmarks.landmark[16]
                pixel_x = int(tip.x*frame.shape[1])
                pixel_y = int(tip.y*frame.shape[0])
                i_up = tip.y < joint.y
                m_up = tip1.y < joint.y
                #print(pixel_x,pixel_y)
                if i_up and not m_up:
                    #cv2.putText(frame, f"Finger is up", (10,40),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
                    if x!=0 and y!=0:
                        if pixel_y < 50:
                            if 5 <= pixel_x <= 55:
                                color = (0, 0, 180)      
                            elif 65 <= pixel_x <= 115:
                                color = (34, 139, 34)
                            elif 125 <= pixel_x <= 175:
                                color = (180, 0, 0)   
                            elif 185 <= pixel_x <= 235:
                                color = (0, 255, 255)   
                            elif 245 <= pixel_x <= 295:
                                color = (0, 0, 0)   
                            elif 305 <= pixel_x <= 385:
                                canvas[:] = 0
                        #cv2.line(canvas, (x,y), (pixel_x,pixel_y), color,2)
                        cv2.line(canvas, (x, y), (pixel_x, pixel_y), color, 10, cv2.LINE_AA)
                    x = pixel_x
                    y = pixel_y
                else:
                    #cv2.putText(frame, f"Finger is folded", (10,40),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
                    x=0
                    y=0
                cv2.circle(frame, (pixel_x,pixel_y), 8, (0,255,0), 2)
    output = cv2.add(frame, canvas)
    cv2.imshow("Hand writing", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
camera.release()
cv2.destroyAllWindows() 
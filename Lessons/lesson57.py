import cv2
import mediapipe as mp
import pyautogui as pt
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
camera = cv2.VideoCapture(0)
pre_x = 0
pre_y = 0
frame_count=0
while True:
    success, frame = camera.read()
    if not success:
        break
    frame_count+=1
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            wrist = hand_landmarks.landmark[0]
            x = int(wrist.x*frame.shape[1])
            y = int(wrist.y*frame.shape[0])
            threshold = 40
            cv2.circle(frame, (x,y),20,(255,0,0))
            dx = x-pre_x
            dy = y-pre_y
            pre_x = x
            pre_y = y
            if dx>threshold:
                cv2.putText(frame, "Right", (10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                pt.keyDown('right')
            if dx<-threshold and frame_count==6:
                cv2.putText(frame, "Left", (10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            if dy<-threshold and frame_count==6:
                cv2.putText(frame, "Up", (10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            if dy>threshold and frame_count==6:
                cv2.putText(frame, "Down", (10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow("Subway surfers",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
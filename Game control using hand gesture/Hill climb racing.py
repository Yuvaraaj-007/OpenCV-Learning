import cv2
import pyautogui as pt
import mediapipe as mp
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
camera = cv2.VideoCapture(0)
previous_action = "Idle"
while True:
    success, frame = camera.read()
    if not success:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    #print(frame.shape)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_up = 0
            fingerindex = [(8,6), (12,10), (16,14) , (20,18)]
            for (i,j) in fingerindex:
                tip = hand_landmarks.landmark[i]
                joint = hand_landmarks.landmark[j]
                #if  (i,j) == (8,6) or (i,j) == (12,10) or (i,j) == (16,14) or (i,j) == (20,18):
                if tip.y<joint.y:
                    fingers_up = fingers_up+1
            if fingers_up==4:
                current_action = "Gas"
                cv2.putText(frame, "Action  : Gas", (10,40), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),2)
                previous_action = current_action
                if previous_action == "Gas":
                    pt.keyUp('left')
                    pt.keyDown('right')
            elif fingers_up==0:
                current_action = "brake"
                cv2.putText(frame, "Action : brake", (10,40), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                previous_action = current_action
                if previous_action=="brake":
                    pt.keyUp('right')
                    pt.keyDown('left')
            #else:
                #pt.keyUp('right')
                #pt.keyDown('left')
                #else:
                    #cv2.putText(frame, "Idle", (10,40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),2)
    cv2.imshow("Hand gesture", frame)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
camera.release()
cv2.destroyAllWindows()
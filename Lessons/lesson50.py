import cv2
import mediapipe as mp
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
camera = cv2.VideoCapture(0)
while True:
    success, frame = camera.read()
    if not success:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    count = 0
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingerindex = [(8,6), (12,10), (16,14) , (20,18), (4,3)]
            for (i,j) in fingerindex:    
                    tip = hand_landmarks.landmark[i]
                    joint = hand_landmarks.landmark[j]
                    if (i,j)==(8,6):
                        if tip.y > joint.y:
                            cv2.putText(frame, "Index : Folded", (10,40),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                        else:
                            cv2.putText(frame, "Index : Up", (10,40),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)              
                            count+=1
                    if (i,j)==(12,10):
                        if tip.y > joint.y:
                            cv2.putText(frame, "Middle : Folded", (10,70),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                        else:
                            cv2.putText(frame, "Middle : Up", (10,70),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                            count+=1
                    if (i,j)==(16,14):
                        if tip.y > joint.y:
                            cv2.putText(frame, "Ring : Folded", (10,100),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                        else:
                            cv2.putText(frame, "Ring : Up", (10,100),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                            count+=1
                    if (i,j)==(20,18):
                        if tip.y > joint.y:
                            cv2.putText(frame, "Little : Folded", (10,130),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                        else:
                            cv2.putText(frame, "Little : Up", (10,130),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                            count+=1
                    if (i,j)==(4,3):
                        if tip.x > joint.x:
                            cv2.putText(frame, "Thumb : Folded", (10,160),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                        else:
                            cv2.putText(frame, "Thumb : Up", (10,160),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                            count+=1
            cv2.putText(frame, f"Number of fingers rised : {count}" , (10,190), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv2.imshow("Hand detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
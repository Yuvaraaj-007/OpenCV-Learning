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
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            #hand_landmarks.landmarks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            w_x = int(hand_landmarks.landmark[0].x*frame.shape[1])
            w_y = int(hand_landmarks.landmark[0].y*frame.shape[0])
            normalized = []
            abs_normalized = []
            for i in hand_landmarks.landmark:
                landmarks_x = int(i.x*frame.shape[1])
                landmarks_y = int(i.y*frame.shape[0])
                dx = landmarks_x - w_x
                dy = landmarks_y - w_y
                normalized.append(dx)
                normalized.append(dy)
                abs_normalized.append(abs(dx))
                abs_normalized.append(abs(dy))
            max_dx = max(abs_normalized)
            #max_dy = max(abs_normalized)
            sc = []
            for j in normalized:
                sc_x = j/max_dx
                sc.append(sc_x)
    cv2.imshow("ASL translator",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
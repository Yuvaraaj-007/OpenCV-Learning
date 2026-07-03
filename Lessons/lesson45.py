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
    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        count = len(results.multi_hand_landmarks)
        for  hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
        cv2.putText(frame, f"Total hands found : {count}", (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)  
    cv2.imshow("Hand Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
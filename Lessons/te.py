import cv2 
import mediapipe as mp
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw = mp.solutions.drawing_utils
camera = cv2.VideoCapture(0)
while True:
    success, frame = camera.read()
    if not success:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Hand detection", frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
camera.read()
cv2.destroyAllWindows()
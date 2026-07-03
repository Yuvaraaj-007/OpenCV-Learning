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
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        landmark = hand_landmarks.landmark[8]
        cv2.putText(frame, f"X coordinate : {landmark.x:.2f}",(10,40), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        pixel_x = int(landmark.x * frame.shape[1])
        print(pixel_x)
    cv2.imshow("Hand detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
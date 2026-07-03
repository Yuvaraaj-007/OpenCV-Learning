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
            index = [4, 8, 12, 16, 20]
            for i in index:
                landmark = hand_landmarks.landmark[i]
                pixel_x = int(landmark.x * frame.shape[1])
                pixel_y = int(landmark.y * frame.shape[0])
                cv2.circle(frame, (pixel_x,pixel_y),2,(0,255,0),2)
    cv2.imshow("Hand detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
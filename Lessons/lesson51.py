import cv2
import mediapipe as mp
import math
import numpy as np
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
camera = cv2.VideoCapture(0)
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(volume.GetVolumeRange())
while True:
    success , frame = camera.read()
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
            pixel_x1 = int(tip1.x*frame.shape[1])
            pixel_y1 = int(tip1.y*frame.shape[0])
            distance = math.sqrt(((pixel_x-pixel_x1)**2)+((pixel_y-pixel_y1)**2))
            cv2.circle(frame, (pixel_x,pixel_y),8,(0,255,0),2)
            cv2.circle(frame, (pixel_x1,pixel_y1),8,(0,255,0),2)
            cv2.line(frame, (pixel_x,pixel_y),(pixel_x1,pixel_y1),(0,0,255),2)
            #print(distance)
            volume_percentage = np.interp(distance, (9,120),(0,100))
            volume_level = np.interp(distance, (9,120), (-65.25, 0.0))
            volume.SetMasterVolumeLevel(volume_level, None)
            cv2.putText(frame, (f"Volume : {volume_percentage}%"),(10,40),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    cv2.imshow("Volume adjusting",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
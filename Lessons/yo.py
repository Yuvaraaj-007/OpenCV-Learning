import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
while True:
    success, frame = camera.read()
    if not success:
        break
    result = model(frame)
    phone_detected = 0
    for box in result[0].boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
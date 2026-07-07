import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
camera = cv2.VideoCapture(0)
while True:
    success, frame = camera.read()
    if not success:
        break
    result = model(frame)
    for box in result[0].boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
    print(class_id,class_name)
    cv2.imshow("Project",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
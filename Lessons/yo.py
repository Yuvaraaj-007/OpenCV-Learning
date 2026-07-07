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
        if box.conf[0]>0.5 and class_name == 'cell phone':
            phone_detected+=1
            x1,y1,x2,y2 = box.xyxy[0]
            x1,x2,y1,y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)
    if phone_detected>0:
        cv2.putText(frame, f"Phone detected : {phone_detected}", (10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.putText(frame, f"{box.conf}",(10,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    else:
        cv2.putText(frame, "Hall is safe", (10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv2.imshow("YOLO", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
import cv2
face = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)
while True:
    succes , frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=3)
    for i, (x,y,w,h) in enumerate(faces, start =1):
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame, f"Faces detected {i}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, f"Total faces found : {len(faces)}", (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
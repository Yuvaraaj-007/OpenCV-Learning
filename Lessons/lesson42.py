import cv2
face = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
image = cv2.imread("Images/persons.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=3)
for(x,y,w,h) in faces:
    cv2.rectangle(image, (x,y),(x+w,y+h),(0,255,0),2)
for i in range(1,len(faces)+1):
    print("Face", i, "detected")
cv2.imshow("Face Detection", image)
print("Total faces found : ",len(faces))
cv2.waitKey(0)
cv2.destroyAllWindows()
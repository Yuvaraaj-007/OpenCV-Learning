import cv2
camera = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("Videos/my_recording.avi",fourcc,20.0,(640,480))
while True:
    success, frame = camera.read()
    if not success:
        break
    out.write(frame)
    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
out.release()
cv2.destroyAllWindows()
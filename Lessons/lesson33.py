import cv2

video = cv2.VideoCapture("Videos/sample.mp4")

while True:
    success, frame = video.read()

    if not success:
        print("End of video")
        break

    cv2.imshow("Video", frame)

    key = cv2.waitKey(100) & 0xFF

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
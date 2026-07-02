import cv2
image = cv2.imread("Images/flower.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Gray", gray)
cv2.imshow("Binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
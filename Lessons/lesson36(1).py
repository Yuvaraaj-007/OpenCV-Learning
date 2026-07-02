import cv2
image = cv2.imread("Images/flower.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print("Original image shape : ",image.shape)
print("HSV image shape : ",hsv.shape)
cv2.imshow("Original",image)
cv2.imshow("HSV",hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
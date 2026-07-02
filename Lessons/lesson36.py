import cv2
image = cv2.imread("Images/flower.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Original image shape : ",image.shape)
print("Gray image shape : ",gray.shape)
cv2.imshow("Original",image)
cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
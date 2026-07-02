import cv2
image = cv2.imread("Images/flower.jpg")
blur = cv2.GaussianBlur(image,(11,11),0)
cv2.imshow("Original image",image)
cv2.imshow("Blur image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
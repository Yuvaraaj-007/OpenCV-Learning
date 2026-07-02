import cv2
image = cv2.imread("Images/flower.jpg")
horizontal = cv2.flip(image, 1)
cv2.imshow("Horizontal : ",horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
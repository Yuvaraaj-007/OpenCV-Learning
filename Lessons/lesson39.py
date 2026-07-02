import cv2
image = cv2.imread("Images/flower.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray,100,200)
cv2.imshow("Original image",image)
cv2.imshow("Grayscale",gray)
cv2.imshow("Edge",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
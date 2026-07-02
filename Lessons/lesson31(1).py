import cv2
image = cv2.imread("Images/flower.jpg")
print("Original shape : ",image.shape)
cv2.imshow("Original image : ",image)
cropped = image[50:250, 100:300]
print("Cropped shape : ",cropped.shape)
cv2.imshow("Cropped image : ",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
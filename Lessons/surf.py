import cv2
img = cv2.imread("Images/mahirat.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create(nfeatures=1000)
keypoints, description = orb.detectAndCompute(gray,None)
result = cv2.drawKeypoints(img, keypoints, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("SURF Features", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
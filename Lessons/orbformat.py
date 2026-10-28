
import cv2
import os
base_path = os.path.join(os.path.dirname(__file__),"..","Images")
image1 = cv2.imread(os.path.join(base_path, "flower.jpg"))
image2 = cv2.imread(os.path.join(base_path, "flower.jpg"))
if image1 is None or image2 is None:
    print("Error: flower.jpg not found in the Images folder!")
    exit()
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create(nfeatures=1000)
keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)
if descriptors1 is None or descriptors2 is None:
    print("Error: No features detected in the image!")
    exit()
matcher = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches = matcher.match(descriptors1, descriptors2)
matches = sorted(matches, key=lambda match: match.distance)
output = cv2.drawMatches(image1,keypoints1,image2,keypoints2,matches[:50],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
print("Keypoints in Image 1:", len(keypoints1))
print("Keypoints in Image 2:", len(keypoints2))
print("Total matches:", len(matches))
print("Displayed matches:", min(50, len(matches)))
cv2.imshow("ORB Feature Matching", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
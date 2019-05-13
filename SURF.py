import cv2
import numpy as np

img = cv2.imread('download.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image',img)

surf = cv2.xfeatures2d.SURF_create()


# kp will be a list of keypoints and des is a numpy array of shape to match keypoints in different images
kp, des = surf.detectAndCompute(gray,None)

for m in des:
    print(m)

# function which draws the small circles on the locations of keypoints.
img=cv2.drawKeypoints(gray,kp,img)

cv2.imshow('SURF Keypoints',img)

# cv2.imwrite('sift_keypoints.jpg',img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
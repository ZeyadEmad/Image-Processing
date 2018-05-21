import cv2
import numpy as np

img = cv2.imread('home.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image',img)

sift = cv2.xfeatures2d.SIFT_create()
# sift.detect() function finds the keypoint in the images.
# You can pass a mask if you want to search only a part of image.
# Each keypoint is a special structure which has many attributes
# like its (x,y) coordinates, size of the meaningful neighbourhood,
# angle which specifies its orientation, response that specifies strength of keypoints etc.
# kp = sift.detect(gray,None)

# kp will be a list of keypoints and des is a numpy array of shape to match keypoints in different images
kp, des = sift.detectAndCompute(gray,None)

for m in des:
    print(m)

# function which draws the small circles on the locations of keypoints.
img=cv2.drawKeypoints(gray,kp,img)

cv2.imshow('SIFT Keypoints',img)

# cv2.imwrite('sift_keypoints.jpg',img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
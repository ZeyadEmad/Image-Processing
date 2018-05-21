import cv2
import numpy as np

img = cv2.imread('Lens.png', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
abs_grad_y = cv2.convertScaleAbs(grad_y)

dst = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)

cv2.imshow('Original', img)
cv2.imshow('Sobel', dst)

cv2.waitKey(0)
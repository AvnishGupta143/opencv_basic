import cv2 as cv
import numpy as np
def nothing(x):
	pass

img1 = cv.imread("apple.jpg")
img2 = cv.imread("balloon.jpg")
img2_gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow("img2_gray",img2_gray)

cv.namedWindow("mask")
cv.createTrackbar('threshold','mask',0,255,nothing)

while(1):
	threshold = cv.getTrackbarPos("threshold","mask")
	ret, mask = cv.threshold(img2_gray, threshold , 255, cv.THRESH_BINARY)
	mask_inv = cv.bitwise_not(mask)

	cv.imshow("mask",mask)
	cv.imshow("mask_inv",mask_inv)

	if cv.waitKey(10) & 0xFF == ord('c'): break 

cv.destroyAllWindows() 

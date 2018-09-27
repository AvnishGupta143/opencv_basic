import cv2 as cv
import numpy as np
def nothing(x):
	pass

img2 = cv.imread("balloon.jpg")
img2_gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow("img2_gray",img2_gray)
rows,cols,channels = img2.shape

cv.namedWindow("mask")
cv.createTrackbar('threshold','mask',0,255,nothing)

while(1):
	threshold = cv.getTrackbarPos("threshold","mask")
	ret, mask = cv.threshold(img2_gray, threshold , 255, cv.THRESH_BINARY)
	mask_inv = cv.bitwise_not(mask)

	cv.imshow("mask",mask)
	cv.imshow("mask_inv",mask_inv)
	
	img1 = cv.imread("apple.jpg")
	roi = img1[0:rows, 0:cols]
	cv.imshow("roi",img1_copy)
	img1_bg = cv.bitwise_and(roi,roi,mask = mask)
	cv.imshow("img1_bg",img1_bg)

	img2_fg = cv.bitwise_and(img2,img2,mask = mask_inv)
	cv.imshow("img2_fg",img2_fg)

	dst = cv.add(img1_bg,img2_fg)
	img1[0:rows, 0:cols ] = dst
	cv.imshow('res',img1)
	if cv.waitKey(30) & 0xFF == ord('c'): break 

cv.destroyAllWindows()

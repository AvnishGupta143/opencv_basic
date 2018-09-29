import cv2 as cv
import numpy as np

def nothing(x):
	pass

img = np.zeros((512,512,3),np.uint8)
cv.namedWindow("image")

cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

while(1):
	cv.imshow('image',img)
	if cv.waitKey(1) == ord('c'): break
	
	r = cv.getTrackbarPos('R','image')
	b = cv.getTrackbarPos('B','image')
	g = cv.getTrackbarPos('G','image')

	img[:] = [b,g,r]

	hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
	h,s,v = hsv[256,256,:]

	print("H:",h,"  S:",s,"  V:",v)

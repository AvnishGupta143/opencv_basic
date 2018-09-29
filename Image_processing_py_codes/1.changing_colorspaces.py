import cv2 as cv
import numpy as np

def nothing(x):
	pass

#To get other flags, just run following commands in your Python terminal : 
#>>> import cv2 as cv
#>>> flags = [i for i in dir(cv) if i.startswith('COLOR_')]
#>>> print( flags )

#For color conversion, we use the function cv.cvtColor(input_image, flag) where flag determines the type of conversion.

img_ = np.zeros((512,512,3),dtype=np.uint8)
cv.namedWindow("image")
img = cv.cvtColor(img_,cv.COLOR_BGR2HSV)
cv.createTrackbar('H','image',0,179,nothing)
cv.createTrackbar('S','image',0,255,nothing)
cv.createTrackbar('V','image',0,255,nothing)

while(1):
	if cv.waitKey(1) == ord('c'): break
	
	h = cv.getTrackbarPos('H','image')
	s = cv.getTrackbarPos('S','image')
	v = cv.getTrackbarPos('V','image')

	img[:] = [h,s,v]
	img_ = cv.cvtColor(img,cv.COLOR_HSV2BGR)
	cv.imshow('image',img_)


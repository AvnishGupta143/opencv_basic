import cv2 as cv
import numpy as np

def nothing(x):
	pass

img = np.zeros((512,512,3),np.uint8)
cv.namedWindow("image")

#For cv.getTrackbarPos() function, first argument is the trackbar name, second one is the window name to which it is attached, third argument is the default value, fourth one is the maximum value and fifth one is the callback function which is executed everytime trackbar value changes. The callback function always has a default argument which is the trackbar position.
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,2,nothing)

while(1):
	cv.imshow('image',img)
	if cv.waitKey(1) == ord('c'): break
	
	r = cv.getTrackbarPos('R','image')
	b = cv.getTrackbarPos('B','image')
	g = cv.getTrackbarPos('G','image')
	s = cv.getTrackbarPos(switch,'image')
	
	if s == 0:	img[:] = 0
	elif s ==1:
		img[:] = [b,g,r]
		img[256::] = [r,g,b]
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.putText(img,'BGR',(0,100), font, 4,(255,255,255),2,cv.LINE_AA)
		cv.putText(img,'RGB',(0,511), font, 4,(255,255,255),2,cv.LINE_AA)
	else:		img[:] = [b,g,r]

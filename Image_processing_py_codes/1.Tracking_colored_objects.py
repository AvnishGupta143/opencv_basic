import cv2 as cv
import numpy as np

lower = np.array([0,0,0])
upper = np.array([0,0,0])

def check_limit():
	
	global lower,upper		
	if upper[0]>179: upper[0]=179
	if upper[1]>255: upper[1]=255
	if upper[2]>255: upper[2]=255

	if lower[0]<0 : lower[0]=0
	if lower[1]<0 : lower[1]=0
	if lower[2]<0 : lower[2]=0

def pick_color(event,x,y,flags,param):
	
	global lower,upper,hsv
	if event == cv.EVENT_LBUTTONDOWN:
		#print("coordinates:",x,y)
		pixel = hsv[y,x,:]

		#HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
		upper =  np.array([pixel[0] + 10, 255 , pixel[2]+60])
		lower =  np.array([pixel[0] - 10, 100 , pixel[2]-60])
		
		check_limit()	
		print(lower, upper)

cap = cv.VideoCapture(0)
while True:
	ret,frame = cap.read()
	#print("fr",frame.shape)
	
	hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	#print("hsv",hsv.shape)
	cv.imshow("frame",frame)
	cv.setMouseCallback("frame", pick_color)

	#threshold the HSV to get the color at which we clicked
	mask = cv.inRange(hsv,lower,upper)
	
	#bitwise AND mask and original image
	res =cv.bitwise_and(frame,frame,mask = mask)
	
	cv.imshow('mask',mask)
	cv.imshow('res',res)
	if cv.waitKey(10) & 0xFF == ord('c'): break

cv.destroyAllWindows()

#How to find HSV values to track? 
# It is very simple and you can use the same function, cv.cvtColor(). Instead of passing an image, you just pass the BGR values you want. For example, to find the HSV value of Green, try following commands in Python terminal: 
#>>> green = np.uint8([[[0,255,0 ]]])
#>>> hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
#>>> print( hsv_green )
#[[[ 60 255 255]]]
#Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively



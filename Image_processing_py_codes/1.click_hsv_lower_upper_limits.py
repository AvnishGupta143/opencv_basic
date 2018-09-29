import cv2 
import numpy as np

def check_limit(lower,upper):
			
		if upper[0]>179: upper[0]=179
		if upper[1]>255: upper[1]=255
		if upper[2]>255: upper[2]=255

		if lower[0]<0 : lower[0]=0
		if lower[1]<0 : lower[1]=0
		if lower[2]<0 : lower[2]=0
		
		return lower,upper

def pick_color(event,x,y,flags,param):
	global image_hsv,img_bgr
	if event == cv2.EVENT_LBUTTONDOWN:
		pixel = image_hsv[x,y]

		#HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
		upper =  np.array([pixel[0] + 10, pixel[1]+10 , pixel[2]+40])
		lower =  np.array([pixel[0] - 10, pixel[1]-10 , pixel[2]-40])
		
		lower,upper = check_limit(lower,upper)	
		print(lower, upper)

image_bgr = cv2.imread("apple.jpg")
cv2.imshow("BGR",image_bgr)

image_hsv = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",image_hsv)
	
#CALLBACK FUNCTION
cv2.setMouseCallback("HSV", pick_color)

cv2.waitKey(0)
cv2.destroyAllWindows()

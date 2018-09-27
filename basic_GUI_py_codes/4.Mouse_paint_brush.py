#for all the getting events running on dir(cv2)
#events = [i for i in dir(cv) if 'EVENT' in i]
#print( events )

import cv2 as cv
import numpy as np
import random

rot = 0
ix,iy = -1,-1
drawing_mode=False
mode = True

def draw(event,x,y,flags,param):
	global ix,iy,drawing_mode,mode,rot
	if event == cv.EVENT_LBUTTONDBLCLK:
		rot += 60
		clr = [0,255,0]
		random.shuffle(clr)
		cv.ellipse(img,(x,y),(75,75),rot,0,300,tuple(clr),50)

	if event == cv.EVENT_LBUTTONDOWN:
		drawing_mode = True
		ix,iy=x,y
	elif event == cv.EVENT_MOUSEMOVE:
		if drawing_mode == True:
			if mode == True:
	        		cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
			else:
				cv.circle(img,(x,y),5,(0,0,255),-1)
	elif event == cv.EVENT_LBUTTONUP:
		drawing_mode = False
		if mode == True:
			cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
		else:
			cv.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw)

print("Double click to draw ellipse")
print("press m to toggle bw circle and rectangle")

while(1):
	cv.imshow('image',img)
	k = cv.waitKey(1) & 0xFF
	if k == ord('m'):
		mode = not mode
		print("mode: ",mode)
	elif k == 27:	
		break

cv.destroyAllWindows()


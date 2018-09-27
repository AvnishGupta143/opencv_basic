import cv2 as cv
import numpy as np
def nothing(x):
	pass

#There is a difference between OpenCV addition and Numpy addition. OpenCV addition is a saturated operation while Numpy addition is a modulo operation. OpenCV function will provide a better result. cv.add(x,y)

img1 = cv.imread("balloon.jpg")
img2 = cv.imread("balloon2.jpg")

img3 = img1 + img2 #numpy addition
img4 = cv.add(img1,img2) #opencv addition

cv.imshow("numpy addition",img3)
cv.imshow("opencv addition",img4)

#Image Blending : This is also image addition, but different weights are given to images so that it gives a feeling of blending or transparency. Images are added as per the equation below:  g(x)=(1−α)f0(x)+αf1(x) ::::α from 0→1::::
#cv.addWeighted() applies following equation on the image.  dst=α⋅img1+β⋅img2+γ
cv.namedWindow("image blender")
cv.createTrackbar('alpha','image blender',0,100,nothing)
while(1):
	alpha = float(cv.getTrackbarPos('alpha','image blender')/100)
	img5 = cv.addWeighted(img1,1-alpha,img2,alpha,0)
	cv.imshow('image blender',img5)
	if cv.waitKey(1) & 0xFF == ord('c'):break 

cv.destroyAllWindows()

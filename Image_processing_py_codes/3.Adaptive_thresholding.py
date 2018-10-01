import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
	pass

#in simple thresholding we used global value as threshold value. But it may not be good in all the conditions where image has different lighting conditions in different areas. In that case, we go for adaptive thresholding. In this, the algorithm calculate the threshold for a small regions of the image. So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.

#It has three ‘special’ input params and only one output argument.
#Adaptive Method - It decides how thresholding value is calculated.

#    cv.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
#    cv.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.

#Block Size - It decides the size of neighbourhood area.

#C - It is just a constant which is subtracted from the mean or weighted mean calculated.\

#dst = cv.adaptiveThreshold( src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])

img = cv.imread("rect.jpeg",0)
cv.namedWindow("org_image")

cv.createTrackbar("block_sz","org_image",3,120,nothing)

cv.imshow("org_image",img)
while True:
	
	block_sz = cv.getTrackbarPos("block_sz","org_image")
	if block_sz%2 == 0:block_sz+=1	
	
	ad_thresh1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,block_sz,1.8) 			
	ad_thresh2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,block_sz,1.8)
	
	cv.imshow("mean_adaptive",ad_thresh1)
	cv.imshow("gaussian_adaptive",ad_thresh2)	
	if cv.waitKey(20) & 0xFF == ord("c"): break

cv.destroyAllWindows()

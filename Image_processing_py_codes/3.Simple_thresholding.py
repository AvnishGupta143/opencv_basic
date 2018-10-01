import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
	pass

#If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). The function used is cv.threshold. First argument is the source image, which should be a grayscale image. Second argument is the threshold value which is used to classify the pixel values. Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value. OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. 
# retval, dst = cv.threshold(src, thresh, maxval, type[, dst])
# Two outputs are obtained. First one is a retval which will be explained later. Second output is our thresholded image.
#he function applies fixed-level thresholding to a multiple-channel array. The function is typically used to get a bi-level (binary) image out of a grayscale image ( cv::compare could be also used for this purpose) or for removing a noise, that is, filtering out pixels with too small or too large values.

img = cv.imread("rect.jpeg",0)
cv.namedWindow("image")
cv.createTrackbar("thresh_val","image",0,255,nothing)


while True:
	cv.imshow("image",img)
	thresh_val = cv.getTrackbarPos("thresh_val","image")	
	
	ret,thresh1 = cv.threshold(img,thresh_val,255,cv.THRESH_BINARY)
	ret,thresh2 = cv.threshold(img,thresh_val,255,cv.THRESH_BINARY_INV)
	ret,thresh3 = cv.threshold(img,thresh_val,255,cv.THRESH_TRUNC)
	ret,thresh4 = cv.threshold(img,thresh_val,255,cv.THRESH_TOZERO)
	ret,thresh5 = cv.threshold(img,thresh_val,255,cv.THRESH_TOZERO_INV)
	
	titles = ['BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
	images = [thresh1, thresh2, thresh3, thresh4, thresh5]
	
	for i in range(5):
		#plt.subplot(2,3,i+1)
		cv.imshow(titles[i],images[i])
		#plt.title(titles[i])
		#plt.xticks([]),plt.yticks([])

	#plt.show()
	if cv.waitKey(25) & 0xFF == ord('c'): break

cv.destroyAllWindows()

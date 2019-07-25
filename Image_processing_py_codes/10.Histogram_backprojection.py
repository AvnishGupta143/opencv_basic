import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi.jpg')
cv.imshow("image",img)

# It is used for image segmentation or finding objects of interest in an image. In simple words, it creates an image of the same size (but single channel) as that of our input image, where each pixel corresponds to the probability of that pixel belonging to our object. In more simpler worlds, the output image will have our object of interest in more white compared to remaining part. 
# Histogram Backprojection is used with camshift algorithm
# We create a histogram of an image containing our object of interest. The object should fill the image as far as possible for better results. And a color histogram is preferred over grayscale histogram, because color of the object is a better way to define the object than its grayscale intensity. We then "back-project" this histogram over our test image where we need to find the object, ie in other words, we calculate the probability of every pixel belonging to the object and show it. The resulting output on proper thresholding gives us the object alone.

### 1.USING NUMPY

# Extract the object you want to track from the image
# roi is the object or region of object we need to find
roi = img[266:318,21:150]
cv.imshow("i",roi)
hsv_obj = cv.cvtColor(roi,cv.COLOR_BGR2HSV)

# img is the image we search in
hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# First we need to calculate the color histogram of both the object we need to find (let it be 'M') and the image where we are going to search (let it be 'I'). 
M = cv.calcHist([hsv_obj],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv.calcHist([hsv_img],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# Find the ratio R = M/I. Then backproject R, ie use R as palette and create a new image with every pixel as its corresponding probability of being target. ie B(x,y) = R[h(x,y),s(x,y)] where h is hue and s is saturation of the pixel at (x,y). After that apply the condition B(x,y)=min[B(x,y),1].
R = M/I
h,s,v = cv.split(hsv_img)
B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(hsv_img.shape[:2])

# Now apply a convolution with a circular disc, B=D∗B, where D is the disc kernel. 
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cv.filter2D(B,-1,disc,B)
B = np.uint8(B)
# Normalizes the norm or value range of an array. The function cv::normalize normalizes scale and shift the input array elements so that ||dst||Lp = alpha (where p=Inf, 1 or 2) when normType=NORM_INF, NORM_L1, or NORM_L2, respectively; or so that                 minIdst(I) = alpha,maxIdst(I)=beta
# dst = cv.normalize( src, dst[, alpha[, beta[, norm_type[, dtype[, mask]]]]] )
# alpha - norm value to normalize to or the lower range boundary in case of the range normalization.
# beta - upper range boundary in case of the range normalization; it is not used for the norm normalization.
# norm_type - normalization type (see cv::NormTypes). 
cv.normalize(B,B,0,255,cv.NORM_MINMAX)

#Now the location of maximum intensity gives us the location of object. If we are expecting a region in the image, thresholding for a suitable value gives a nice result. 
ret,thresh = cv.threshold(B,10,255,0)

cv.imshow("segmented ground",thresh)

### 2.USING OPENCV

# OpenCV provides an inbuilt function cv.calcBackProject(). Its parameters are almost same as the cv.calcHist() function. One of its parameter is histogram which is histogram of the object and we have to find it. Also, the object histogram should be normalized before passing on to the backproject function. It returns the probability image. Then we convolve the image with a disc kernel and apply threshold.

# calculating object histogram
roihist = cv.calcHist([hsv_obj],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# normalize histogram and apply backprojection
cv.normalize(roihist,roihist,0,255,cv.NORM_MINMAX)
# dst =	cv.calcBackProject(	images, channels, hist, ranges, scale[, dst] )
dst = cv.calcBackProject([hsv_img],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cv.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv.threshold(dst,50,255,0)
thresh = cv.merge((thresh,thresh,thresh))
res = cv.bitwise_and(img,thresh)
res = np.vstack((img,thresh,res))
cv.imshow('result OpenCV',res)

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
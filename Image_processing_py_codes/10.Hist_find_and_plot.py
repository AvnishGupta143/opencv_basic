import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("messi.jpg")
img_gray = cv.imread("messi.jpg",0)

#You can consider histogram as a graph or plot, which gives you an overall idea about the intensity distribution of an image. It is a plot with pixel values (ranging from 0 to 255, not always) in X-axis and corresponding number of pixels in the image on Y-axis.
#By looking at the histogram of an image, you get intuition about contrast, brightness, intensity distribution etc of that image. 

#some terminologies related with histograms - 
#1.BINS -  It is the number of subdivisions in each dim.If the histogram shows the number of pixels for every pixel value, ie from 0 to 255. ie you need 256 values to show the above histogram. Than the number of bins would be 256.For example, you need to find the number of pixels lying between 0 to 15, then 16 to 31, ..., 240 to 255. You will need only 16 values to represent the histogram. Hence number of bins is 16.
#2.DIMS - DIMS : It is the number of parameters for which we collect the data. In this case, we collect data regarding only one thing, intensity value. So here it is 1.
#3.RANGE - It is the range of intensity values you want to measure. Normally, it is [0,256], ie all intensity values. 

# CALCULATING HISTOGRAM
# Histogram can be calculate using opencv or numpy
#1. Using Opencv:
#we use cv.calcHist() function to find the histogram. Let's familiarize with the function and its parameters :
#cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
#images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
#channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
#mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. 
#histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
#ranges : this is our RANGE. Normally, it is [0,256].

hist_cv = cv.calcHist([img_gray],[0],None,[256],[0,256])

#hist_cv is a 256x1 array, each value corresponds to number of pixels in that image with its corresponding pixel value.

# Using Numpy:
#numpy also provides you a function, np.histogram().
# hist is same as we calculated before. But bins will have 257 elements, because Numpy calculates bins as 0-0.99, 1-1.99, 2-2.99 etc. So final range would be 255-255.99. To represent that, they also add 256 at end of bins. But we don't need that 256. Upto 255 is sufficient.
#Numpy has another function, np.bincount() which is much faster than (around 10X) np.histogram(). So for one-dimensional histograms, you can better try that. Set minlength = 256 in np.bincount. 
#For example, hist = np.bincount(img.ravel(),minlength=256)

hist_np	 = np.histogram(img_gray.ravel(),256,[0,256])

# PLOTTING HISTOGRAM
#1.Short Way : use Matplotlib plotting functions
plt.figure(1)
plt.hist(img_gray.ravel(),256,[0,256])
plt.show()

plt.figure(2)
color = ('b','g','r')
for i,col in enumerate(color):
    hist_color = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist_color,color = col)
    plt.xlim([0,256])
plt.show()

#2.Long Way : use OpenCV drawing functions
#Here you adjust the values of histograms along with its bin values to look like x,y coordinates so that you can draw it using cv.line() or cv.polyline()

#APPLICATION OF MASK

mask = np.zeros(img_gray.shape,np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img_gray,img_gray,mask = mask)
hist_full = cv.calcHist([img_gray],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img_gray],[0],mask,[256],[0,256])
plt.figure(3)
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()
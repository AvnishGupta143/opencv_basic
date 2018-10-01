import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#In global thresholding, we used an arbitrary value for threshold value, right? So, how can we know a value we selected is good or not? Answer is, trial and error method. But consider a bimodal image (In simple words, bimodal image is an image whose histogram has two peaks). For that image, we can approximately take a value in the middle of those peaks as threshold value, right ? That is what Otsu binarization does. So in simple words, it automatically calculates a threshold value from image histogram for a bimodal image
#For this, our cv.threshold() function is used, but pass an extra flag, cv.THRESH_OTSU. For threshold value, simply pass zero. Then the algorithm finds the optimal threshold value and returns you as the second output, retVal. If Otsu thresholding is not used, retVal is same as the threshold value you used.

img = cv.imread("noisy2.jpeg",0)

#GLOBAL THRESHOLDING
ret1,th_global = cv.threshold(img,127,255,cv.THRESH_BINARY)

#OTSU THRESHOLDING
ret2, th_otsu = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

blur = cv.GaussianBlur(img,(5,5),0)
ret3, th_otsu_gauss = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th_global,
          img, 0, th_otsu,
          blur, 0, th_otsu_gauss]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
	
	plt.subplot(3,3,i*3+1), plt.imshow(images[i*3],'gray')
	plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
	
	plt.subplot(3,3,i*3+2), plt.hist(images[i*3].ravel(),256)
	plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])

	plt.subplot(3,3,i*3+3), plt.imshow(images[i*3+2],'gray')
	plt.title(titles[i*3+2]), plt.xticks([]),plt.yticks([])

plt.show()
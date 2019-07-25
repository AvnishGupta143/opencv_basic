import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("ice.jpg",0)

#Consider an image whose pixel values are confined to some specific range of values only. For eg, brighter image will have all pixels confined to high values. But a good image will have pixels from all regions of the image. So you need to stretch this histogram to either ends and that is what Histogram Equalization does. This normally improves the contrast of the image.
hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

#We need the full spectrum. For that, we need a transformation function which maps the input pixels in brighter region to output pixels in full region. That is what histogram equalization does.

#USING NUMPY-----------

#masking the value 0 so that the cdf_m.min() is not equal to zero
cdf_m = np.ma.masked_equal(cdf,0)
#applying the histogram equalisation
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
#filling the masked value as 0 again
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]  #this is the histogram equalised image with adjusted contrast

#these are the steps to see the histogram and cdf of the new image
hist,bins = np.histogram(img2.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

cv.imshow("original",img)
cv.imshow("histogram_equalised",img2)
if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()

#Another important feature is that, even if the image was a darker image (instead of a brighter one we used), after equalization we will get almost the same image as we got. As a result, this is used as a "reference tool" to make all images with same lighting conditions. This is useful in many cases. For example, in face recognition, before training the face data, the images of faces are histogram equalized to make them all with same lighting conditions.

#USING OPENCV FUNCTION----------

#OpenCV has a function to do this, cv.equalizeHist(). Its input is just grayscale image and output is our histogram equalized image.
# dst = cv.equalizeHist( src[, dst] )
img = cv.imread('ice.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv.imwrite('equ.png',res)

#The first histogram equalization we just saw, considers the global contrast of the image. In many cases, it is not a good idea.
#Histogram equalization is good when histogram of the image is confined to a particular region. It won't work good in places where there is large intensity variations where histogram covers a large region, ie both bright and dark pixels are present. 
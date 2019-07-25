import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi.jpg')

#we calculated and plotted one-dimensional histogram. It is called one-dimensional because we are taking only one feature into our consideration, ie grayscale intensity value of the pixel. But in two-dimensional histograms, you consider two features. Normally it is used for finding color histograms where two features are Hue & Saturation values of every pixel.

### For color histograms, we need to convert the image from BGR to HSV. or 2D histograms,

##FINDING 2D HISTOGRAM

# using the same function, cv.calcHist().
# Its parameters will be modified as follows:
# channels = [0,1] because we need to process both H and S plane.
# bins = [180,256] 180 for H plane and 256 for S plane.
# range = [0,180,0,256] Hue value lies between 0 and 180 & Saturation lies between 0 and 256.

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
hist_cv = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

#2.USING NUMPY
#Numpy also provides a specific function for this : np.histogram2d()
#First argument is H plane, second one is the S plane, third is number of bins for each and fourth is their range.
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist_np, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])

#hist_cv and hist_np are exatly same

##PLOTTING 2D HISTOGRAM

#1.USING OPENCV
#The result we get is a two dimensional array of size 180x256. So we can show them as we do normally, using cv.imshow() function. It will be a grayscale image and it won't give much idea what colors are there, unless you know the Hue values of different colors.

cv.imshow("plot_using_cv",hist_np)

#2.USING MATPLOTLIB
#We can use matplotlib.pyplot.imshow() function to plot 2D histogram with different color maps. It gives us a much better idea about the different pixel density. But this also, doesn't gives us idea what color is there on a first look, unless you know the Hue values of different colors. 
#While using this function, remember, interpolation flag should be nearest for better results.

plt.imshow(hist_cv,interpolation = 'nearest')
plt.title("plot_using_matplotlib")
plt.show()

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
#3.refer 10.Histogram_color.py
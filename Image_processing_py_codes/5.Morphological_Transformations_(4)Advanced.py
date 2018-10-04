import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("binary.png")

###We manually created a structuring elements in th previous examples with help of Numpy. It is rectangular shape. But in some cases, you may need elliptical/circular shaped kernels. So for this purpose, OpenCV has a function, cv.getStructuringElement(). You just pass the shape and size of the kernel, you get the desired kernel. 
k1 = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
k2 = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
k3 = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))

##1.Opening is just another name of erosion followed by dilation. It is useful in removing noise

opening = cv.morphologyEx(img, cv.MORPH_OPEN, k3)

##2.Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object. 

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, k3)

##3.Morphological Gradient: t is the difference between dilation and erosion of an image.

Gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, k3)

##4.Top Hat: It is the difference between input image and Opening of the image. Below example is done for a 9x9 kernel. 

TopHat = cv.morphologyEx(img, cv.MORPH_TOPHAT, k3)

##5.Black Hat: It is the difference between the closing of the input image and input image. 

BlackHat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, k3)

cv.imshow("original",img)
cv.imshow("opening",opening)
cv.imshow("closing",closing)
cv.imshow("Gradient",Gradient)
cv.imshow("TopHat",TopHat)
cv.imshow("BlackHat",BlackHat)

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()

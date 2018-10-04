import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("binary.png")

### dst = cv.morphologyEx( src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])
#op: Type of a morphological operation, see cv::MorphTypes :: cv.MORPH_OPEN ,cv.MORPH_CLOSE ,cv.MORPH_GRADIENT, cv.MORPH_TOPHAT, cv.MORPH_BLACKHAT, cv.MORPH_HITMISS
#kernel: Structuring element. It can be created using cv::getStructuringElement.
#anchor: Anchor position with the kernel. Negative values mean that the anchor is at the kernel center.
#iterations: Number of times erosion and dilation are applied. 
k = np.ones((5,5),np.uint8) 

##1.Opening is just another name of erosion followed by dilation. It is useful in removing noise

opening = cv.morphologyEx(img, cv.MORPH_OPEN, k)

##2.Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object. 

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, k)

##3.Morphological Gradient: t is the difference between dilation and erosion of an image.

Gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, k)

##4.Top Hat: It is the difference between input image and Opening of the image. Below example is done for a 9x9 kernel. 

TopHat = cv.morphologyEx(img, cv.MORPH_TOPHAT, k)

##5.Black Hat: It is the difference between the closing of the input image and input image. 

BlackHat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, k)

cv.imshow("original",img)
cv.imshow("opening",opening)
cv.imshow("closing",closing)
cv.imshow("Gradient",Gradient)
cv.imshow("TopHat",TopHat)
cv.imshow("BlackHat",BlackHat)

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()


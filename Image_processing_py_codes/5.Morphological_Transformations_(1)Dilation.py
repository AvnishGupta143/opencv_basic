import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("binary.png")

#It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.

# dst = cv.dilate( src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )
##iterations	number of times erosion is applied. 
#kernel	structuring element used for erosion; if element=Mat(), a 3 x 3 rectangular structuring element is used. Kernel can be created using getStructuringElement. 
#anchor	position of the anchor within the element; default value (-1, -1) means that the anchor is at the element center. 
k = np.ones((5,5),np.uint8) 

dilation = cv.dilate(img,k, iterations = 1)

cv.imshow("original",img)
cv.imshow("dilation",dilation)

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
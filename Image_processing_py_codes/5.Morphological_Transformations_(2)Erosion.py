import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, Closing, Gradient etc also comes into play.


#The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always try to keep foreground in white). So what it does? The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
#So what happends is that, all the pixels near boundary will be discarded depending upon the size of kernel. So the thickness or size of the foreground object decreases or simply white region decreases in the image. It is useful for removing small white noises 

img = cv.imread("binary.png")

k = np.ones((5,5),np.uint8)
#erosion = dst = cv.erode( src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )
#iterations	number of times erosion is applied. 
#kernel	structuring element used for erosion; if element=Mat(), a 3 x 3 rectangular structuring element is used. Kernel can be created using getStructuringElement. 
#anchor	position of the anchor within the element; default value (-1, -1) means that the anchor is at the element center. 

erosion = cv.erode(img,k, iterations = 1)

cv.imshow("original",img)
cv.imshow("erosion",erosion)

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()


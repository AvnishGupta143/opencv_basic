import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
	pass

img = cv.imread("threshold.jpg")
cv.namedWindow("original")
#1.Noise Reduction::Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5x5 Gaussian filter. We have already seen this in previous chapters.

#2.Finnding Intensity Gradient of the Image:: Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction (G_x) and vertical direction (G_y). From these two images, we can find edge gradient and direction for each pixel as follows:
#          Edge_Gradient ; (G) = sqrt{G_x^2 + G_y^2} 
#          Angle ; (theta) = tan^{-1} ({G_y}/{G_x})
#Gradient direction is always perpendicular to edges. It is rounded to one of four angles representing vertical, horizontal and two diagonal directions.

#3.Non-maximum Suppression::After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitute the edge. 

#4.Hysteresis Thresholding::This stage decides which are all edges are really edges and which are not. For this, we need two threshold values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they are connected to “sure-edge” pixels, they are considered to be part of edges. Otherwise, they are also discarded.

#OpenCV puts all the above in single function, cv2.Canny(). We will see how to use it. First argument is our input image. Second and third arguments are our minVal and maxVal respectively. Third argument is aperture_size. It is the size of Sobel kernel used for find image gradients. By default it is 3. Last argument is L2gradient which specifies the equation for finding gradient magnitude. If it is True, it uses the equation mentioned above which is more accurate, otherwise it uses this function: Edge_Gradient; (G) = |G_x| + |G_y|. By default, it is False.

#edges = cv.Canny( image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
#threshold1	first threshold for the hysteresis procedure.
#threshold2	second threshold for the hysteresis procedure.
##apertureSize	aperture size for the Sobel operator.
#L2gradient	a flag, indicating whether a more accurate L2 norm =sqrt((dI/dx)^2+(dI/dy)^2) should be used to calculate the image gradient magnitude ( L2gradient=true ), or whether the default L1 norm =|dI/dx|+|dI/dy| is enough ( L2gradient=false ).

cv.createTrackbar("minVal","original",0,255,nothing)
cv.createTrackbar("maxVal","original",0,255,nothing)
cv.imshow("original",img)

while 1:

	minVal = cv.getTrackbarPos("minVal","original")
	maxVal = cv.getTrackbarPos("maxVal","original")

	edges = cv.Canny(img,minVal,maxVal, L2gradient=True)

	cv.imshow("edges",edges)

	if cv.waitKey(10) & 0xFF == ord('c'): break

cv.destroyAllWindows()

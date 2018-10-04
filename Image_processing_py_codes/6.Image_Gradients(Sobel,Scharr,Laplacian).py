import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#OpenCV provides three types of gradient filters or High-pass filters, Sobel, Scharr and Laplacian.

img = cv.imread('apple.jpg',0)
cv.imshow("original",img)
#Sobel operators is a joint Gausssian smoothing plus differentiation operation, so it is more resistant to noise. You can specify the direction of derivatives to be taken, vertical or horizontal (by the arguments, yorder and xorder respectively). You can also specify the size of kernel by the argument ksize. If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter
#dst = cv.Sobel( src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]] )
#Calculates the first, second, third, or mixed image derivatives using an extended Sobel operator.
#In all cases except one, the ksize×ksize separable kernel is used to calculate the derivative. When ksize = 1, the 3×1 or 1×3 kernel is used (that is, no Gaussian smoothing is done). ksize = 1 can only be used for the first or the second x- or y- derivatives.
#There is also the special value ksize = CV_SCHARR (-1) that corresponds to the 3×3 Scharr filter that may give more accurate results than the 3×3 Sobel.
#ddepth	output image depth, see combinations; in the case of 8-bit input images it will result in truncated derivatives.
#dx	order of the derivative x.
#dy	order of the derivative y.
#ksize	size of the extended Sobel kernel; it must be 1, 3, 5, or 7.
#scale	optional scale factor for the computed derivative values; by default, no scaling is applied (see cv::getDerivKernels for details).  
#The function calculates an image derivative by convolving the image with the appropriate kernel: dst=∂xorder+yorder(src)/(∂xxorder*∂yyorder)

sobelx = cv.Sobel(img,cv.CV_8U,1,0,ksize=3)
sobely = cv.Sobel(img,cv.CV_8U,0,1,ksize=3)

cv.imshow("sobelx_8U",sobelx)
cv.imshow("sobely_8U",sobely)

#The function calculates the Laplacian of the source image by adding up the second x and y derivatives calculated using the Sobel operator:
#dst = Δsrc = ∂2src/∂x2 + ∂2src/∂y2
#This is done when ksize > 1. When ksize == 1, the Laplacian is computed by filtering the image with the following 3×3 aperture: [[0,1,0],[1,−4,1],[0,1,0]]
# dst = cv.Laplacian( src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]] )

Laplacian = cv.Laplacian(img,cv.CV_8U)

cv.imshow("Laplacian_8U",Laplacian)

#Calculates the first x- or y- image derivative using Scharr operator.
#The function computes the first x- or y- spatial image derivative using the Scharr operator.
#dst = cv.Scharr( src, ddepth, dx, dy[, dst[, scale[, delta[, borderType]]]])

Scharr = cv.Scharr(img,cv.CV_8U,1,0)

cv.imshow("Scharr_8U",Scharr)

####In our last example, output datatype is cv.CV_8U or np.uint8. But there is a slight problem with that. Black-to-White transition is taken as Positive slope (it has a positive value) while White-to-Black transition is taken as a Negative slope (It has negative value). So when you convert data to np.uint8, all negative slopes are made zero. In simple words, you miss that edge.
####If you want to detect both edges, better option is to keep the output datatype to some higher forms, like cv.CV_16S, cv.CV_64F etc, take its absolute value and then convert back to cv.CV_8U.

#Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx_64F =  cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
sobely_64F =  cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
Laplacian_64F = cv.Laplacian(img,cv.CV_64F)

abs_sobelx_64F = np.absolute(sobelx_64F)
abs_sobely_64F = np.absolute(sobely_64F)
abs_Laplacian_64F = np.absolute(Laplacian_64F)

sobelx_conv = np.uint8(abs_sobelx_64F)
sobely_conv = np.uint8(abs_sobely_64F)
Laplacian_conv = np.uint8(abs_Laplacian_64F)

cv.imshow("sobelx_64F",sobelx_64F)
cv.imshow("sobely_64F",sobely_64F)
cv.imshow("Laplacian_64F",Laplacian_64F)
cv.imshow("sobelx_conv",sobelx_conv)
cv.imshow("sobely_conv",sobely_conv)
cv.imshow("Laplacian_conv",Laplacian_conv)

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noises. It actually removes high frequency content (eg: noise, edges) from the image. So edges are blurred a little bit in this operation. (Well, there are blurring techniques which doesn't blur the edges too).

### 1. AVERAGING
#This is done by convolving image with a normalized box filter. It simply takes the average of all the pixels under kernel area and replace the central element. This is done by the function cv.blur() or cv.boxFilter().
#A 3x3 normalized box filter would look like below:
#    K=[[111],[111],[111]]/9
#If you don't want to use normalized box filter, use cv.boxFilter(). Pass an argument normalize=False to the function.

img = cv.imread("noisy2.jpeg")

# dst = cv.blur( src, ksize[, dst[, anchor[, borderType]]] )
# dst = cv.boxFilter( src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]] )
# anchor = -1 by defualt i.e. the pixel will be mapped at the central element of the kernel
#K=[[111.....],[111.....]......,[111.....]]/alpha  : alpha = 1/ksize.width*ksize.height if normalize = True else alpha = 1

average = cv.blur(img,(5,5))

cv.imshow("original",img)
cv.imshow("average",average)


### 2.GAUSSAIN BLURRING
#In this, instead of box filter, gaussian kernel is used. It is done with the function, cv.GaussianBlur(). We should specify the width and height of kernel which should be positive and odd. We also should specify the standard deviation in X and Y direction, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as same as sigmaX. If both are given as zeros, they are calculated from kernel size. Gaussian blurring is highly effective in removing gaussian noise from the image.
#If you want, you can create a Gaussian kernel with the function, cv.getGaussianKernel().
# dst = cv.GaussianBlur( src, ksize, sigmaX[, dst[, sigmaY[, borderType]]] )

gaussian = cv.GaussianBlur(img,(7,7),0)

cv.imshow("gaussian",gaussian)


### 3.MEDAIN BLURRING
#Here, the function cv.medianBlur() takes median of all the pixels under kernel area and central element is replaced with this median value. This is highly effective against salt-and-pepper noise in the images. Interesting thing is that, in the above filters, central element is a newly calculated value which may be a pixel value in the image or a new value. But in median blurring, central element is always replaced by some pixel value in the image. It reduces the noise effectively. Its kernel size should be a positive odd integer.
#dst = cv.medianBlur( src, ksize[, dst])

median = cv.medianBlur(img,11)

cv.imshow("median",median)

### 4.BILATERAL FILTERING
#cv.bilateralFilter() is highly effective in noise removal while keeping edges sharp. But the operation is slower compared to other filters. We already saw that gaussian filter takes the a neighbourhood around the pixel and find its gaussian weighted average. This gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It doesn't consider whether pixels have almost same intensity. It doesn't consider whether pixel is an edge pixel or not. So it blurs the edges also, which we don't want to do.
#Bilateral filter also takes a gaussian filter in space, but one more gaussian filter which is a function of pixel difference. Gaussian function of space make sure only nearby pixels are considered for blurring while gaussian function of intensity difference make sure only those pixels with similar intensity to central pixel is considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.
# dst = cv.bilateralFilter( src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
#sigmaColor	Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace) will be mixed together, resulting in larger areas of semi-equal color.
#sigmaSpace	Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor ). When d>0, it specifies the neighborhood size regardless of sigmaSpace. Otherwise, d is proportional to sigmaSpace. 
#Sigma values: For simplicity, you can set the 2 sigma values to be the same. If they are small (< 10), the filter will not have much effect, whereas if they are large (> 150), they will have a very strong effect, making the image look "cartoonish".
#Filter size: Large filters (d > 5) are very slow, so it is recommended to use d=5 for real-time applications, and perhaps d=9 for offline applications that need heavy noise filtering.

bilateralFilter = cv.bilateralFilter(img,9,250,250)

cv.imshow("bilateralFilter",bilateralFilter)

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
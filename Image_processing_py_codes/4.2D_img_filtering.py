import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#As in one-dimensional signals, images also can be filtered with various low-pass filters(LPF), high-pass filters(HPF) etc. LPF helps in removing noises, blurring the images etc. HPF filters helps in finding edges in the images.
#OpenCV provides a function cv.filter2D() to convolve a kernel with an image

img = cv.imread("noisy2.jpeg")

#kernel of size 11x11 for smoothening the image
k = np.ones((11,11),np.float32)/121

#dst = cv.filter2D( src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]] )
conv = cv.filter2D(img,-1,k)

cv.imshow("org",img)
cv.imshow("convulation_2D",conv)

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
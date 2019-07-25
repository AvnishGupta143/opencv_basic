import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("orange.jpg")

#Normally, we used to work with an image of constant size. But in some occassions, we need to work with images of different resolution of the same image. For example, while searching for something in an image, like face, we are not sure at what size the object will be present in the image. In that case, we will need to create a set of images with different resolution and search for object in all the images. These set of images with different resolution are called Image Pyramids (because when they are kept in a stack with biggest image at bottom and smallest image at top look like a pyramid).
#There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids
#Higher level (Low resolution) in a Gaussian Pyramid is formed by removing consecutive rows and columns in Lower level (higher resolution) image. Then each pixel in higher level is formed by the contribution from 5 pixels in underlying level with gaussian weights. By doing so, a M×N image becomes M/2×N/2 image. So area reduces to one-fourth of original area. It is called an Octave. The same pattern continues as we go upper in pyramid (ie, resolution decreases). Similarly while expanding, area becomes 4 times in each level. We can find Gaussian pyramids using cv.pyrDown() and cv.pyrUp() functions. 

# dst = cv.pyrDown( src[, dst[, dstsize[, borderType]]])
#Blurs an image and downsamples it.
#By default, size of the output image is computed as Size((src.cols+1)/2, (src.rows+1)/2), but in any case, the following conditions should be satisfied: |dstsize.width∗2−src.cols|≤2 && |dstsize.height∗2−src.rows|≤2
#The function performs the downsampling step of the Gaussian pyramid construction. Then, it downsamples the image by rejecting even rows and columns.

lower_reso1 = cv.pyrDown(img)
lower_reso2 = cv.pyrDown(lower_reso1)
lower_reso3 = cv.pyrDown(lower_reso2)

cv.imshow("img",img)
cv.imshow("lower_reso1",lower_reso1)
cv.imshow("lower_reso2",lower_reso2)
cv.imshow("lower_reso3",lower_reso3)

# dst = cv.pyrUp( src[, dst[, dstsize[, borderType]]] )
#Upsamples an image and then blurs it.
#By default, size of the output image is computed as Size(src.cols\*2, (src.rows\*2), but in any case, the following conditions should be satisfied: |dstsize.width−src.cols∗2|≤(dstsize.widthmod2) && |dstsize.height−src.rows∗2|≤(dstsize.heightmod2)
#The function performs the upsampling step of the Gaussian pyramid construction, though it can actually be used to construct the Laplacian pyramid. First, it upsamples the source image by injecting even zero rows and columns and then convolves the result with the same kernel as in pyrDown multiplied by 4.

higher_reso1 = cv.pyrUp(lower_reso3)
#during downsampling the data is lost and it cannot be regained when Upsampling is done again.Compare between the higher_reso1 and lower_reso2
higher_reso2 = cv.pyrUp(higher_reso1)
higher_reso2_2 = cv.pyrUp(lower_reso2)

higher_reso4 = cv.pyrUp(img)

cv.imshow("higher_reso4",higher_reso4)
cv.imshow("higher_reso1",higher_reso1)
cv.imshow("higher_reso2",higher_reso2)
cv.imshow("higher_reso2_2",higher_reso2_2)

#Laplacian Pyramids are formed from the Gaussian Pyramids. There is no exclusive function for that. Laplacian pyramid images are like edge images only. Most of its elements are zeros. They are used in image compression. A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid

lapP2 = cv.subtract(lower_reso2,higher_reso1)
lapP1 = cv.subtract(lower_reso1,higher_reso2_2)

cv.imshow("lapP1",lapP1)
cv.imshow("lapP2",lapP2)
if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()

#plt.subplot(4,1,1), plt.imshow(lower_reso3),plt.title("lower_reso3"),plt.xticks([]),plt.yticks([])
#plt.subplot(4,1,2), plt.imshow(lower_reso2),plt.title("lower_reso2"),plt.xticks([]),plt.yticks([])
#plt.subplot(4,1,3), plt.imshow(lower_reso1),plt.title("lower_reso1"),plt.xticks([]),plt.yticks([])
#plt.subplot(4,1,4), plt.imshow(img),plt.title("img"),plt.xticks([]),plt.yticks([])
#plt.show()
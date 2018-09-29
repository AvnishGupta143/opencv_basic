import numpy as np
import cv2 as cv

#Scaling is just resizing of the image. OpenCV comes with a function cv.resize() for this purpose. The size of the image can be specified manually, or you can specify the scaling factor. Different interpolation methods are used. Preferable interpolation methods are cv.INTER_AREA for shrinking and cv.INTER_CUBIC (slow) & cv.INTER_LINEAR for zooming. By default, interpolation method used is cv.INTER_LINEAR for all resizing purposes

#The function resize resizes the image src down to or up to the specified size. Note that the initial dst type or size are not taken into account. Instead, the size and type are derived from the src,dsize,fx, and fy. If you want to resize src so that it fits the pre-created dst, you may call the function as follows:
#// explicitly specify dsize=dst.size(); fx and fy will be computed from that.
#resize(src, dst, dst.size(), 0, 0, interpolation);

#Usage:: dst = cv.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
#dsize	output image size; if it equals zero, it is computed as:   𝚍𝚜𝚒𝚣𝚎 = 𝚂𝚒𝚣𝚎(𝚛𝚘𝚞𝚗𝚍(𝚏𝚡*𝚜𝚛𝚌.𝚌𝚘𝚕𝚜), 𝚛𝚘𝚞𝚗𝚍(𝚏𝚢*𝚜𝚛𝚌.𝚛𝚘𝚠𝚜))
#Either dsize or both fx and fy must be non-zero.

img = cv.imread("apple.jpg")
zoom = cv.resize(img,(0,0),fx=2,fy=2,interpolation = cv.INTER_CUBIC)
cv.imshow("zoomed_image",zoom)

rows,cols = img.shape[:2]
shrinked = cv.resize(img,(int(cols*0.5),int(rows*0.5)),interpolation = cv.INTER_AREA)
cv.imshow("shrinked_image",shrinked)
cv.waitKey(0)

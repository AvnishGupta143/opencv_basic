import numpy as np
import cv2 as cv


img = cv.imread("wedge.jpg")
cv.imshow("img",img)
print(img.shape)

rows,cols,ch = img.shape
#In affine transformation, all parallel lines in the original image will still be parallel in the output image. To find the transformation matrix, we need three points from input image and their corresponding locations in output image. Then cv.getAffineTransform will create a 2x3 matrix which is to be passed to cv.warpAffine.
# retval = cv.getAffineTransform( src, dst )
# dst = cv.warpAffine( src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]] )

pts1 = np.float32([[137,6],[311,88],[24,31]])
pts2 = np.float32([[0,0],[cols-1,0],[0,rows-1]])

M = cv.getAffineTransform(pts1,pts2)

aff_T = cv.warpAffine(img,M,(cols,rows))
cv.imshow("Transform Affine",aff_T)

#For perspective transformation, you need a 3x3 transformation matrix. Straight lines will remain straight even after the transformation. To find this transformation matrix, you need 4 points on the input image and corresponding points on the output image. Among these 4 points, 3 of them should not be collinear. Then transformation matrix can be found by the function cv.getPerspectiveTransform. Then apply cv.warpPerspective with this 3x3 transformation matrix.
#retval	= cv.getPerspectiveTransform( src, dst ) :returns 3x3 perspective transformation for the corresponding 4 point pairs.
#dst = cv.warpPerspective( src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])

pts1 = np.float32([[137,6],[311,88],[21,42],[239,155]])
pts2 = np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])

M_pers = cv.getPerspectiveTransform(pts1,pts2)

pers_T = cv.warpPerspective(img,M_pers,(cols,rows))
cv.imshow("Transform Perspective",pers_T)

cv.waitKey(0)

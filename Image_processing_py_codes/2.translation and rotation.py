import numpy as np
import cv2 as cv

##OpenCV provides two transformation functions, cv.warpAffine and cv.warpPerspective, with which you can have all kinds of transformations. cv.warpAffine takes a 2x3 transformation matrix while cv.warpPerspective takes a 3x3 transformation matrix as input.

#Translation is the shifting of object's location. If you know the shift in (x,y) direction, let it be (tx,ty), you can create the transformation matrix M as follows:
#			M = [ 1  0  tx ]
#			    [ 0  1  ty ]
#You can take make it into a Numpy array of type np.float32 and pass it into cv.warpAffine() function
#  	dst = cv.warpAffine( src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
#Third argument of the cv.warpAffine() function is the size of the output image, which should be in the form of **(width, height)**. Remember width = number of columns, and height = number of rows.

img = cv.imread("apple.jpg")
rows,cols = img.shape[:2]
M_trans = np.float32([[1,0,50],[0,1,100]])
translation = cv.warpAffine(img,M_trans,(cols,rows))
cv.imshow("translation",translation)

#Rotation of an image for an angle θ is achieved by the transformation matrix of the form
#                   M=[  cosθ  sinθ  ]
#                     [  −sinθ cosθ  ]
#But OpenCV provides scaled rotation with adjustable center of rotation so that you can rotate at any location you prefer. Modified transformation matrix is given by   [  α   β  (1−α)⋅center.x−β⋅center.y ]
#				    [ -β   α  β⋅center.x+(1−α)⋅center.y ]
#                where: α=scale⋅cosθ,β=scale⋅sinθ
#To find this transformation matrix, OpenCV provides a function, cv.getRotationMatrix2D
#retval	= cv.getRotationMatrix2D( center, angle, scale )
 
M_Rot = cv.getRotationMatrix2D((cols/2,rows/2),90,0.5)
Rotation = cv.warpAffine(img,M_Rot,(cols,rows))
cv.imshow("Rotation",Rotation)

cv.waitKey(0)

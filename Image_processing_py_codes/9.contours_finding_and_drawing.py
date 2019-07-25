import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition. 
#For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
#In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

img = cv.imread("rect.jpeg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret , threshold = cv.threshold(gray,197,255,cv.THRESH_BINARY_INV)

#there are three arguments in cv.findContours() function, first one is source image, second is contour retrieval mode, third is contour approximation method. And it outputs a modified image, the contours and hierarchy. contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
#image, contours, hierarchy = cv.findContours( image, mode, method[, contours[, hierarchy[, offset]]] )

k = np.ones((3,3),np.uint8)
threshold = cv.dilate(threshold,k ,iterations = 1)
threshold = cv.erode(threshold,k,iterations = 1)
threshold =  cv.GaussianBlur(threshold,(3,3),0)
cv.imwrite("threshold.jpg",threshold)

img2 , contours , hierarchy = cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

#To draw the contours, cv.drawContours function is used. It can also be used to draw any shape provided you have its boundary points. Its first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours (useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness etc.
#image = cv.drawContours(image,contours,contourIdx,color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]])
#image - Destination image.
#contours - All the input contours. Each contour is stored as a point vector.
#contourIdx - Parameter indicating a contour to draw. If it is negative, all the contours are drawn.
#color - Color of the contours.
#thickness - Thickness of lines the contours are drawn with. If it is negative (for example, thickness=CV_FILLED ), the contour interiors are drawn. The function draws contour outlines in the image if thickness≥0 or fills the area bounded by the contours if thickness<0
#lineType - Line connectivity. See cv::LineTypes. 

#Contour Approximation Method = Above, we told that contours are the boundaries of a shape with same intensity. It stores the (x,y) coordinates of the boundary of a shape. But does it store all the coordinates ? That is specified by this contour approximation method.
#If you pass cv.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we need all the points? For eg, you found the contour of a straight line. Do you need all the points on the line to represent that line? No, we need just two end points of that line. This is what cv.CHAIN_APPROX_SIMPLE does. It removes all redundant points and compresses the contour, thereby saving memory.

cv.imshow("original",img)
cv.imshow("gray",gray)
cv.imshow("threshold",threshold)

image = cv.drawContours(img,contours,-1,(0,255,0),3)
cv.imshow("image",image)
print(len(contours))
if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
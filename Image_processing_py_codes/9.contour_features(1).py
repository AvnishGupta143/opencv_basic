import numpy as np
import cv2 as cv

img = cv.imread("rect.jpeg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret , threshold = cv.threshold(gray,197,255,cv.THRESH_BINARY_INV)
k = np.ones((3,3),np.uint8)
threshold = cv.dilate(threshold,k ,iterations = 1)
threshold = cv.erode(threshold,k,iterations = 1)
threshold =  cv.GaussianBlur(threshold,(3,3),0)
cv.imwrite("threshold.jpg",threshold)
img2 , contours , hierarchy = cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
image = cv.drawContours(img,contours,0,(0,255,0),1)
cv.imshow("image",image)
if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()

#----------1.Moments and centroid
#Image moments help you to calculate some features like center of mass of the object, area of the object etc
#The function cv.moments() gives a dictionary of all moment values calculated.
#The moments of a contour are defined in the same way but computed using the Green's formula (see http://en.wikipedia.org/wiki/Green_theorem). So, due to a limited raster resolution, the moments computed for a contour are slightly different from the moments computed for the same rasterized contour.
# retval = cv.moments( array[, binaryImage])
# array : Raster image (single-channel, 8-bit or floating-point 2D array) or an array ( 1×N or N×1 ) of 2D points (Point or Point2f ).
cnt = contours[0]
M = cv.moments(cnt)
print("M: ",M)
#spatial moments: starting from m
#central moments: starting from mu
#central normalised moments: starting from nu
#From this moments, you can extract useful data like area, centroid etc. Centroid is given by the relations, Cx=M10/M00 and Cy=M01/M00

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print("cx: ",cx,"cy: ",cy)

#-----------2.Contour Area                          
#Contour area is given by the function cv.contourArea() or from moments, M['m00']
#The function computes a contour area. Similarly to moments , the area is computed using the Green formula. Thus, the returned area and the number of non-zero pixels, if you draw the contour using drawContours or fillPoly , can be different. Also, the function will most certainly give a wrong results for contours with self-intersections.
#retval = cv.contourArea( contour[, oriented] )
#oriented: Oriented area flag. If it is true, the function returns a signed area value, depending on the contour orientation (clockwise or counter-clockwise). Using this feature you can determine orientation of a contour by taking the sign of an area. By default, the parameter is false, which means that the absolute value is returned. 
area = cv.contourArea(cnt)
print("Area of Contour: ",area)

#----------3.Contour Perimeter
#It is also called arc length. It can be found out using cv.arcLength() function. Second argument specify whether shape is a closed contour (if passed True), or just a curve. 
# retval = cv.arcLength(curve, closed)
#curve:	Input vector of 2D points, stored in std::vector or Mat.
#closed: Flag indicating whether the curve is closed or not. 
perimeter = cv.arcLength(cnt,True)
print("Perimeter: ",perimeter)
import numpy as np
import cv2 as cv

img = cv.imread('lightening.jpg')
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(img_gray,200,255,cv.THRESH_BINARY_INV)
img2,contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
cv.imshow("thresh",thresh)
img1 = img.copy()
img1 = cv.drawContours(img1,contours,0,(0,255,255),4)
cnt = contours[0]

#-----1. Aspect Ratio
# It is the ratio of width to height of bounding rect of the object.
# AspectRatio = Width/Height
x,y,w,h = cv.boundingRect(cnt)
aspect_ratio = float(w)/h
print("Aspect Ratio: ",aspect_ratio)

#-----2. Extent
# Extent is the ratio of contour area to bounding rectangle area.
# Extent = ObjectArea/BoundingRectangleArea
area = cv.contourArea(cnt)
x,y,w,h = cv.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area
print("Extent: ",extent)

#-----3. Solidity
# Solidity is the ratio of contour area to its convex hull area.
# Solidity = ContourArea/ConvexHullArea
area = cv.contourArea(cnt)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area)/hull_area
print("Solidity: ",solidity)

#-----4.Equivalent Diameter
# Equivalent Diameter is the diameter of the circle whose area is same as the contour area.
# EquivalentDiameter = sqrt((4×ContourArea)/π)
area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)
print("Equivalent Diameter: ",equi_diameter)

#-----5. Orientation
# Orientation is the angle at which object is directed. Following method also gives the Major Axis and Minor Axis lengths.
(x,y),(MA,ma),angle = cv.fitEllipse(cnt)
print("Orientation of contour: ",angle)

#-----6. Mask and Pixel Points
# If we need all the points which comprises that object. It can be done as follows:
mask = np.zeros(img_gray.shape,np.uint8)
cv.drawContours(mask,[cnt],0,255,-1)
cv.imshow("mask",mask)
pixelpoints = np.transpose(np.nonzero(mask))
# pixelpoints = cv.findNonZero(mask)

# Here, two methods, one using Numpy functions, next one using OpenCV function (last commented line) are given to do the same. Results are also same, but with a slight difference. Numpy gives coordinates in **(row, column)** format, while OpenCV gives coordinates in **(x,y)** format. So basically the answers will be interchanged. Note that, row = y and column = x.

#-----7. Maximum Value, Minimum Value and their locations
# We can find these parameters using a mask image.
# Finds the global minimum and maximum in an array.
# The function cv::minMaxLoc finds the minimum and maximum element values and their positions. The extremums are searched across the whole array or, if mask is not an empty array, in the specified array region.
# The function do not work with multi-channel arrays. If you need to find minimum or maximum elements across all the channels, use Mat::reshape first to reinterpret the array as single-channel. Or you may extract the particular channel using either extractImageCOI , or mixChannels , or split .
# minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc( src[, mask] )
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(img_gray,mask = mask)

#-----8.Mean Color or Mean Intensity
# Here, we can find the average color of an object. Or it can be average intensity of the object in grayscale mode. We again use the same mask to do it.
# retval = cv.mean( src[, mask] )  : Calculates an average (mean) of array elements.
#The function cv::mean calculates the mean value M of array elements, independently for each channel, and return it. When all the mask elements are 0's, the function returns Scalar::all(0) 
mean_val = cv.mean(img ,mask = mask)
print("Mean Color: ",mean_val)

#-----9.Extreme Points means topmost, bottommost, rightmost and leftmost points of the object.
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

purple = (255,0,255)
cv.circle(img1,leftmost , 5, purple , -1)
cv.circle(img1,rightmost , 5, purple , -1)
cv.circle(img1,topmost , 5, purple , -1)
cv.circle(img1,bottommost , 5, purple , -1)
cv.imshow("image_original_contour",img1)
print()

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
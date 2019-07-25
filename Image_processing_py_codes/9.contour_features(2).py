import numpy as np
import cv2 as cv

img = cv.imread('lightening.jpg')
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(img_gray,200,255,cv.THRESH_BINARY_INV)
img2,contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(len(contours))
cv.imshow("thresh",thresh)
img1 = img.copy()
img1 = cv.drawContours(img1,contours,-1,(0,0,255),2)
cv.imshow("image_original_contour",img1)
cnt = contours[0]

#----------4.Contour Approximation 
#It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify. It is an implementation of Douglas-Peucker algorithm.The function cv::approxPolyDP approximates a curve or a polygon with another curve/polygon with less vertices so that the distance between them is less or equal to the specified precision
#To understand this, suppose you are trying to find a square in an image, but due to some problems in the image, you didn't get a perfect square, but a "bad shape" (As shown in first image below). Now you can use this function to approximate the shape. In this, second argument is called epsilon, which is maximum distance from contour to approximated contour. It is an accuracy parameter. A wise selection of epsilon is needed to get the correct output.
# approxCurve = cv.approxPolyDP( curve, epsilon, closed[, approxCurve] )
#curve:	Input vector of a 2D point stored in std::vector or Mat
#approxCurve: Result of the approximation. The type should match the type of the input curve.
#epsilon: Parameter specifying the approximation accuracy. This is the maximum distance between the original curve and its approximation.
#closed: If true, the approximated curve is closed (its first and last vertices are connected). Otherwise, it is not closed. 

epsilon = 0.01 * cv.arcLength(cnt,True)
approxCurve = cv.approxPolyDP(cnt, epsilon, True)
img2 = img.copy()
img2 = cv.drawContours(img2,[approxCurve],-1,(0,255,0),3)
cv.imshow("image_approx_contour",img2)

#----------5.Convex Hull
#cv.convexHull() function checks a curve for convexity defects and corrects it. Generally speaking, convex curves are the curves which are always bulged out, or at-least flat. And if it is bulged inside, it is called convexity defects. For example, check the below image of hand. Red line shows the convex hull of hand. The double-sided arrow marks shows the convexity defects, which are the local maximum deviations of hull from contours.
#The function cv::convexHull finds the convex hull of a 2D point set using the Sklansky's algorithm [164] that has O(N logN) complexity in the current implementation.
# hull = cv.convexHull(points[, hull[, clockwise[, returnPoints]]
#points are the contours we pass into.
#hull is the output, normally we avoid it.
#clockwise : Orientation flag. If it is True, the output convex hull is oriented clockwise. Otherwise, it is oriented counter-clockwise.The assumed coordinate system has its X axis pointing to the right, and its Y axis pointing upwards. 
#returnPoints : Operation flag.By default, True. Then it returns the coordinates of the hull points. If False, it returns the indices of contour points corresponding to the hull points.When the output array is std::vector, the flag is ignored, and the output depends on the type of the vector.

hull_points = cv.convexHull(cnt,returnPoints = True)
hull_indices = cv.convexHull(cnt,returnPoints = False)
for i in range(len(hull_points)): 
	print("cnt[",hull_indices[i],"] :",hull_points[i])
hull = img.copy()
hull = cv.drawContours(hull,[hull_points],-1,(255,0,0),3)
cv.imshow("hull",hull)

#----------6.Checking Convexity
#There is a function to check if a curve is convex or not, cv.isContourConvex(). It just return whether True or False.
# retval = cv.isContourConvex( contour)
#The function tests whether the input contour is convex or not. The contour must be simple, that is, without self-intersections. Otherwise, the function output is undefined.

k = cv.isContourConvex(cnt)
print("contour is Convex:",k)

#----------7.(a).Straight Bounding Rectangle
#It is a straight rectangle, it doesn't consider the rotation of the object. So area of the bounding rectangle won't be minimum. It is found by the function cv.boundingRect().
# retval = cv.boundingRect( points )
#The function calculates and returns the minimal up-right bounding rectangle for the specified point set.
#retval is basically the topleft and bottom right corners of the rectangle
#Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height. 

img3 = img.copy()
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img3,(x,y),(x+w,y+h),(255,255,0),2)
cv.imshow("bound_rect",img3)

#----------7.(b).Rotated Bounding Rectangle
#Here, bounding rectangle is drawn with minimum area, so it considers the rotation also. The function used is cv.minAreaRect(). It returns a Box2D structure which contains following detals - ( center (x,y), (width, height), angle of rotation ).
#retval	= cv.minAreaRect(points)
#The function calculates and returns the minimum-area bounding rectangle (possibly rotated) for a specified point set. Developer should keep in mind that the returned RotatedRect can contain negative indices when data is close to the containing Mat element boundary.
# But to draw this rectangle, we need 4 corners of the rectangle. It is obtained by the function cv.boxPoints()
#points	= cv.boxPoints( box[, points] )
#Finds the four vertices of a rotated rect. Useful to draw the rotated rectangle. 
#box - The input rotated rectangle. 
img4 = img.copy()
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img4,[box],0,(0,0,255),2)
cv.imshow("rotated_bound_rect",img4)

#----------8.Minimum Enclosing Circle and Triangle
#we find the circumcircle of an object using the function cv.minEnclosingCircle(). It is a circle which completely covers the object with minimum area. The function finds the minimal enclosing circle of a 2D point set using an iterative algorithm.
# center, radius = cv.minEnclosingCircle( points )

#The function finds a triangle of minimum area enclosing the given set of 2D points and returns its area
#The implementation of the algorithm is based on O'Rourke's [139] and Klee and Laskowski's [94] papers. O'Rourke provides a θ(n) algorithm for finding the minimal enclosing triangle of a 2D convex polygon with n vertices. Since the minEnclosingTriangle function takes a 2D point set as input an additional preprocessing step of computing the convex hull of the 2D point set is required. The complexity of the convexHull function is O(nlog(n)) which is higher than θ(n). Thus the overall complexity of the function is O(nlog(n)).
# retval, triangle = cv.minEnclosingTriangle( points[, triangle] )
img5 = img.copy()
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img5,center,radius,(255,255,0),2)

retval, triangle = cv.minEnclosingTriangle(cnt)
triangle = np.int0(triangle)
cv.drawContours(img5,[triangle],0,(0,255,255),2)
cv.imshow("bounding_circle_and_triangle",img5)

#----------9. Fitting an Ellipse 
# Fits an ellipse around a set of 2D points. 
#The function calculates the ellipse that fits (in a least-squares sense) a set of 2D points best of all. It returns the rotated rectangle in which the ellipse is inscribed.Developer should keep in mind that it is possible that the returned ellipse/rotatedRect data contains negative indices, due to the data points being close to the border of the containing Mat element.
#Check also fitEllipseAMS() and fitEllipseDirect()
# retval = cv.fitEllipse( points )
# retval is ( center (x,y), (width, height), angle of rotation ) or box	Alternative ellipse representation via RotatedRect.
img6 = img.copy()
ellipse = cv.fitEllipse(cnt)
cv.ellipse(img6,ellipse,(255,0,255),2)
cv.imshow("bounding_ellipse",img6)

#----------10. Fitting A Line
#we can fit a line to a set of points. Below image contains a set of white points. We can approximate a straight line to it. 
# line = cv.fitLine( points, distType, param, reps, aeps[, line])
#points - Input vector of 2D or 3D points, stored in std::vector<> or Mat. 
#distType - Distance used by the M-estimator, see cv::DistanceTypes
#param - Numerical parameter ( C ) for some types of distances. If it is 0, an optimal value is chosen.
#reps - Sufficient accuracy for the radius (distance between the coordinate origin and the line).
#aeps - Sufficient accuracy for the angle. 0.01 would be a good default value for reps and aeps. 
#line	Output line parameters. In case of 2D fitting, it should be a vector of 4 elements (like Vec4f) - (vx, vy, x0, y0), where (vx, vy) is a normalized vector collinear to the line and (x0, y0) is a point on the line. In case of 3D fitting, it should be a vector of 6 elements (like Vec6f) - (vx, vy, vz, x0, y0, z0), where (vx, vy, vz) is a normalized vector collinear to the line and (x0, y0, z0) is a point on the line. 
#The algorithm is based on the M-estimator ( http://en.wikipedia.org/wiki/M-estimator ) technique that iteratively fits the line using the weighted least-squares algorithm. After each iteration the weights wi are adjusted to be inversely proportional to ρ(ri) 
img7 = img.copy()
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img7,(cols-1,righty),(0,lefty),(0,255,0),2)
cv.imshow("fitting_line",img7)

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
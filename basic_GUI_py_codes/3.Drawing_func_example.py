#img : The image where you want to draw the shapes
#color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
#thickness : Thickness of the line or circle etc. If **-1** is passed for closed figures like circles, it will fill the shape. default thickness = 1
#lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves.

import numpy as np
import cv2 as cv

img = np.zeros((512,512,3),dtype = np.uint8)

#drawing a line img = cv.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
cv.line(img,(0,0),(511,511),(255,0,0),5)

#drawing a ractangle img = cv.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
cv.rectangle(img,(384,0),(510,128),(0,0,255),-1)

#drawing circle img = cv.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
cv.circle(img,(447,64),64,(0,255,0),-1)

#drawing ellipse img = cv.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]])
cv.ellipse(img,(256,256),(100,50),30,0,300,(0,255,255),30)

#drawing polygon  img = cv.polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]] )
#To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices and it should be of type int32.
pts = np.array([[10,5],[80,100],[150,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,pts,True,(255,0,255),5,)	

#putting custom text  img = cv.putText(	img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]	)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Lucifer',(10,511), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow("image",img)
k = cv.waitKey(0) & 0xFF       #function usage is modified for 64 bit machine by adding "& 0xFF"

if k == ord("c"): cv.destroyAllWindows()

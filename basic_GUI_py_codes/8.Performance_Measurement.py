import cv2 as cv
import numpy as np

#cv.getTickCount function returns the number of clock-cycles after a reference event (like the moment machine was switched ON) to the moment this function is called. So if you call it before and after the function execution, you get number of clock-cycles used to execute a function.

#cv.getTickFrequency function returns the frequency of clock-cycles, or the number of clock-cycles per second

#You can use cv.useOptimized() to check if it is enabled/disabled and cv.setUseOptimized() to enable/disable it. 
e1 = cv.getTickCount()
cv.setUseOptimized(True)
img = cv.imread("apple.jpg")
img[0:256,0:256,0] = 255
img[256:511,256:511,1] = 255
cv.imshow("img",img) 
e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()
print(time)

#Sometimes you may need to compare the performance of two similar operations. IPython gives you a magic command timeit to perform this. It runs the code several times to get more accurate results. Once again, they are suitable to measure single line codes.

#Python scalar operations are faster than Numpy scalar operations. So for operations including one or two elements, Python scalar is better than Numpy arrays. Numpy takes advantage when size of array is a little bit bigger.



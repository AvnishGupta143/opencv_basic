import numpy as np
import cv2

#cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
#Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
 
img_clr_bgr  = cv2.imread("apple.jpg",1)
img_bw = cv2.imread("apple.jpg",0)

#There is a special case where you can already create a window and load image to it later. In that case, you can specify whether window is resizable or not. It is done with the function cv2.namedWindow(). By default, the flag is cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window. It will be helpful when image is too large in dimension and adding track bar to windows.
cv2.namedWindow('image_color_bgr', cv2.WINDOW_NORMAL)

cv2.imshow('image_color_bgr',img_clr_bgr)
cv2.imshow('image_black&white',img_bw)

#Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode. So color images will not be displayed correctly in Matplotlib if image is read with OpenCV
img_clr_rgb = cv2.cvtColor(img_clr_bgr,cv2.COLOR_BGR2RGB)
cv2.imshow('image_color_rgb',img_clr_rgb)

k = cv2.waitKey(0) & 0xFF       #function usage is modified for 64 bit machine by adding "& 0xFF"

if k == ord("c"):
	cv2.destroyAllWindows()
	print("closed all windows")
elif k == ord("s"):
	cv2.imwrite("applegray.jpg",img_bw)
	cv2.destroyAllWindows()
	print("closed all windows and saved applegray.jpg")



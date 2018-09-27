import numpy as np
import cv2

#To capture a video, you need to create a VideoCapture object. Its argument can be either the device index or the name of a video file. Device index is just the number to specify which camera.Normally one camera will be connected (as in my case). So I simply pass 0 (or -1). You can select the second camera by passing 1 and so on.

cap = cv2.VideoCapture(0)

#to save a video create a VideoWriter object. We should specify the output file name (eg: output.avi). Then we should specify the FourCC code.Then number of frames per second (fps) and frame size should be passed. And last one is isColor flag. If it is True, encoder expect color frame, otherwise it works with grayscale frame.
#FourCC is a 4-byte code used to specify the video codec.Following codecs works fine for me. In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video) .
#FourCC code is passed as `cv.VideoWriter_fourcc('M','J','P','G')or cv.VideoWriter_fourcc(*'MJPG')` for MJPG.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_gray = cv2.VideoWriter("gray.avi",fourcc,20.0,(640,480))
out_color = cv2.VideoWriter("color.avi",fourcc,20.0,(640,480),True)

#Sometimes, cap may not have initialized the capture. In that case, this code shows error. You can check whether it is initialized or not by the method cap.isOpened(). If it is True, OK. Otherwise open it using cap.open().

while(cap.isOpened()):

#cap.read() returns a bool (True/False). If frame is read correctly, it will be True. So you can check end of the video by checking this return value.
	ret,frame = cap.read()
	if ret == True:
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		flipped = cv2.flip(frame,0)		
		#cv2.line(frame,(0,0),(100,120),(0,0,0),10)
		cv2.imshow("gray video",gray)
		cv2.imshow("rgb video",rgb)
		cv2.imshow("bgr video",frame)
		cv2.imshow("flip video",flipped)
		out_color.write(frame)
		out_gray.write(gray)
#You can also access some of the features of this video using cap.get(propId) method where propId is a number from 0 to 18. Each number denotes a property of the video (if it is applicable to that video).
#Some of these values can be modified using cap.set(propId, value). Value is the new value you want.
#For example, I can check the frame width and height by cap.get(cv.CAP_PROP_FRAME_WIDTH) and cap.get(cv.CAP_PROP_FRAME_HEIGHT). It gives me 640x480 by default. But I want to modify it to 320x240. Just use ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320) and ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240).

		w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
		h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
		print(h,"x",w)

		if cv2.waitKey(1) & 0xFF == ord("c"): break
	else: break

cap.release()
out_color.release()
out_gray.release()
cv2.destroyAllWindows()

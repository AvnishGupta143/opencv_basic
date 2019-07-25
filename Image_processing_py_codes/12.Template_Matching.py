import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Template Matching is a method for searching and finding the location of a template image in a larger image. OpenCV comes with a function cv.matchTemplate() for this purpose. It simply slides the template image over the input image (as in 2D convolution) and compares the template and patch of input image under the template image.
# It returns a grayscale image, where each pixel denotes how much does the neighbourhood of that pixel match with template.
#The function slides through image , compares the overlapped patches of size w×h against templ using the specified method and stores the comparison results in result . Here are the formulae for the available comparison methods ( I denotes image, T template, R result ). The summation is done over template and/or the image patch: x′=0...w−1,y′=0...h−1
# After the function finishes the comparison, the best matches can be found as global minimums (when TM_SQDIFF was used) or maximums (when TM_CCORR or TM_CCOEFF was used) using the minMaxLoc function. In case of a color image, template summation in the numerator and each sum in the denominator is done over all of the channels and separate mean values are used for each channel. That is, the function can take a color template and a color image. The result will still be a single-channel image, which is easier to analyze.

# result = cv.matchTemplate( image, templ, method[, result[, mask]] )
# result - Map of comparison results. It must be single-channel 32-bit floating-point. If image is W×H and templ is w×h , then result is (W−w+1)×(H−h+1) .
# method - Parameter specifying the comparison method, see cv::TemplateMatchModes
# mask -Mask of searched template. It must have the same datatype and size with templ. It is not set by default. Currently, only the TM_SQDIFF and TM_CCORR_NORMED methods are supported. 

def MatchingTemplate(method):

	img2 = img.copy()
	print("This result is using method",methods[method])
	res = cv.matchTemplate(img2,template,method)
	print(res)

	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
	cv.normalize( res, res, 0, 1, cv.NORM_MINMAX, -1 )
	# if method is SQDIFF best match is Global minimum else it is global maximum
	if method in [cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED]: 
		top_left = min_loc
	else:
		top_left = max_loc

	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv.rectangle(img2,top_left, bottom_right, 0, 2)
	match = "match_using " + methods[method]
	cv.imshow( match,img2)
	cv.imshow('result',res)

if __name__ == '__main__':

	global img
	img = cv.imread('messi.jpg',0)
	global template
	template = cv.imread('template1.jpg',0)
	w, h = template.shape[::-1]
	cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
	cv.namedWindow('result',cv.WINDOW_AUTOSIZE)

	global methods
	methods = ['cv.TM_SQDIFF','cv.TM_SQDIFF_NORMED','cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED']
	
	trackbar_label = 'Method: \n 0: SQDIFF \n 1: SQDIFF NORMED \n 2: TM CCORR \n 3: TM CCORR NORMED \n 4: TM COEFF \n 5: TM COEFF NORMED'
	cv.createTrackbar(trackbar_label,'image',0,5,MatchingTemplate)
	cv.imshow('image',img)
	if cv.waitKey(0) == ord('c'): cv.destroyAllWindows()

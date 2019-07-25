import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Suppose you are searching for an object which has multiple occurrences, cv.minMaxLoc() won't give you all the locations. In that case, we will use thresholding. So in this example, we will use a screenshot of the famous game Mario and we will find the coins in it.

img_rgb = cv.imread('mario.jpeg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = img_gray[158:191,367:390]

#list[<start>:<stop>:<step>]
w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imshow('res.png',img_rgb)
cv.waitKey(0)
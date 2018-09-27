import cv2 as cv
import numpy as np

img = cv.imread("apple.jpg")

#setting only red pixels
img[:,:,2] = 150
#setting on blue pixels
img[:,:,0] = 50

print("enter the location of the pixel you want")
coordinate = list()
for i in input().split(' '): coordinate.append(int(i))
print(img.item(coordinate[0],coordinate[1],coordinate[2]))

print("enter the value you want to set for this pixel(0 to 255)")
coordinate.append(int(input()))
img.itemset((coordinate[0],coordinate[1],coordinate[2]),coordinate[3])

#The shape of an image is accessed by img.shape. It returns a tuple of number of rows, columns, and channels (if image is color):
#If an image is grayscale, the tuple returned contains only the number of rows and columns, so it is a good method to check whether the loaded image is grayscale or color.
print("image shape:",img.shape)

#Total number of pixels is accessed by img.size: 
print("image size:",img.size)

#Image datatype is obtained by `img.dtype`: 
print("image datatype:",img.dtype)

cv.imshow("image",img) 

#ROI is again obtained using Numpy indexing. Here I am selecting the ball and copying it to another region in the image: 
img2 = cv.imread("balloon.jpg") # 269x300x3
balloon = img2[135:,:150]
img2[:134,:150] = balloon
img2[:,:,0]=255
cv.imshow("balloon image",img2)
cv.imwrite("balloon2.jpg",img2)

#Sometimes you will need to work separately on B,G,R channels of image. In this case, you need to split the BGR images to single channels. In other cases, you may need to join these individual channels to a BGR image.
#cv.split() is a costly operation (in terms of time). So do it only if you need it. 
b,g,r = cv.split(img)
# OR b = img[:,:,0] , g = img[:,:,1] , r = img[:,:,2]
img = cv.merge((b,g,r)) #b , g , r should be off same length

if cv.waitKey(0) & 0xFF == 27:	cv.destroyAllWindows()

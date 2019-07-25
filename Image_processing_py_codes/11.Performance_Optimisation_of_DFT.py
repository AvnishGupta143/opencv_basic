import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi.jpg',0)
rows,cols = img.shape

#Performance of DFT calculation is better for some array size. It is fastest when array size is power of two. The arrays whose size is a product of 2’s, 3’s, and 5’s are also processed quite efficiently. So if you are worried about the performance of your code, you can modify the size of the array to any optimal size (by padding zeros) before finding DFT. For OpenCV, you have to manually pad zeros. But for Numpy, you specify the new size of FFT calculation, and it will automatically pad zeros for you.

### USING OPENCV
# OpenCV provides a function, cv.getOptimalDFTSize() for this. It is applicable to both cv.dft() and np.fft.fft2()
nrows = cv.getOptimalDFTSize(rows)
ncols = cv.getOptimalDFTSize(cols)
print("original size: ","{} {}".format(rows,cols))
print("optimal size: ","{} {}".format(nrows,ncols))

#Now let's pad it with zeros (for OpenCV) and find their DFT calculation performance. You can do it by creating a new big zero array and copy the data to it, or use cv.copyMakeBorder().
nimg = np.zeros((nrows,ncols))
nimg[:rows,:cols] = img
#OR
right = ncols - cols
bottom = nrows - rows
nimg = cv.copyMakeBorder(img,0,bottom,0,right,cv.BORDER_CONSTANT, value = 0)

dft1 = cv.dft(np.float32(nimg),flags=cv.DFT_COMPLEX_OUTPUT)
# it will take less time as compared to  dft1 = cv.dft(np.float32(img),flags=cv.DFT_COMPLEX_OUTPUT)

### USING NUMPY
fft2 = np.fft.fft2(img,[nrows,ncols])
# it will take less time as compared to fft1 = np.fft.fft2(img)
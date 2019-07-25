import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("messi.jpg",0)

#Fourier Transform is used to analyze the frequency characteristics of various filters. For images, 2D Discrete Fourier Transform (DFT) is used to find the frequency domain. A fast algorithm called Fast Fourier Transform (FFT) is used for calculation of DFT
#For a sinusoidal signal, x(t)=Asin(2πft), we can say f is the frequency of signal, and if its frequency domain is taken, we can see a spike at f. If signal is sampled to form a discrete signal, we get the same frequency domain, but is periodic in the range [−π,π] or [0,2π] (or [0,N] for N-point DFT). You can consider an image as a signal which is sampled in two directions. So taking fourier transform in both X and Y directions gives you the frequency representation of image.
#More intuitively, for the sinusoidal signal, if the amplitude varies so fast in short time, you can say it is a high frequency signal. If it varies slowly, it is a low frequency signal. You can extend the same idea to images. Where does the amplitude varies drastically in images ? At the edge points, or noises. So we can say, edges and noises are high frequency contents in an image. If there is no much changes in amplitude, it is a low frequency component.

###1.FOURIER TRANSFORM USING NUMPY
#---------------------------------
#Numpy has an FFT package to do this. np.fft.fft2() provides us the frequency transform which will be a complex array. Its first argument is the input image, which is grayscale. Second argument is optional which decides the size of output array. If it is greater than size of input image, input image is padded with zeros before calculation of FFT. If it is less than input image, input image will be cropped. If no arguments passed, Output array size will be same as input.
#Now once you got the result, zero frequency component (DC component) will be at top left corner. If you want to bring it to center, you need to shift the result by N2 in both the directions. This is simply done by the function, np.fft.fftshift(). 

f = np.fft.fft2(img)
f_shifted = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(f_shifted))


#do some operations in frequency domain, like high pass filtering and reconstruct the image, ie find inverse DFT. For that you simply remove the low frequencies by masking with a rectangular window of size 60x60. Then apply the inverse shift using np.fft.ifftshift() so that DC component again come at the top-left corner. Then find inverse FFT using np.ifft2() function. The result, again, will be a complex number. You can take its absolute value. 

rows,cols = img.shape
r = int(rows/2)
c = int(cols/2)

#applying high pass filter removing lower frequency
#High Pass Filtering is an edge detection operation. 
high_pass = f_shifted.copy()
high_pass[r-30:r+30,c-30:c+30] = 0
high_pass_i = np.fft.ifftshift(high_pass)
img_back_high_pass = np.fft.ifft2(high_pass_i)
img_back_high_pass = np.abs(img_back_high_pass)

#applying low pass filter removing high frequency
low_pass = f_shifted.copy()
low_pass[0:r-10,0:c-10] = 0
low_pass[r+10:rows,0:c-10] = 0
low_pass[0:r-10,c+10:cols] = 0
low_pass[r+10:rows,c+10:cols] = 0
low_pass_i = np.fft.ifftshift(low_pass)
img_back_low_pass = np.fft.ifft2(low_pass_i)
img_back_low_pass = np.abs(img_back_low_pass)

plt.subplot(151),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(152),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(153),plt.imshow(img_back_high_pass, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(154),plt.imshow(img_back_high_pass)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.subplot(155),plt.imshow(img_back_low_pass ,cmap = 'gray')
plt.title('Image after LPF'), plt.xticks([]), plt.yticks([])
plt.show()
#It shows some ripple like structures in the img_back_high_pass there, and it is called ringing effects. It is caused by the rectangular window we used for masking. This mask is converted to sinc shape which causes this problem. So rectangular windows is not used for filtering. Better option is Gaussian Windows.

###2.FOURIER TRANSFORM USING OPENCV
#---------------------------------
#OpenCV provides the functions cv.dft() and cv.idft() for this. It returns the same result as previous, but with two channels. First channel will have the real part of the result and second channel will have the imaginary part of the result. The input image should be converted to np.float32 first.
# dst = cv.dft( src[, dst[, flags[, nonzeroRows]]] )
# dst =	cv.idft( src[, dst[, flags[, nonzeroRows]]] )
# idft(src, dst, flags) is equivalent to dft(src, dst, flags | DFT_INVERSE)

dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

#You can also use cv.cartToPolar() which returns both magnitude and phase in a single shot
# magnitude, angle = cv.cartToPolar( x, y[, magnitude[, angle[, angleInDegrees]]] )
# x - array of x-coordinates; this must be a single-precision or double-precision floating-point array.
# y - array of y-coordinates, that must have the same size and same type as x.
# magnitude	- utput array of magnitudes of the same size and type as x.
# angle - output array of angles that has the same size and type as x; the angles are measured in radians (from 0 to 2*Pi) or in degrees (0 to 360 degrees). 
magnitude, angle = cv.cartToPolar(dft_shift[:,:,0],dft_shift[:,:,1]) 

#we have to do inverse DFT

# create a mask first, center square is 1, remaining all zeros

mask = np.zeros((rows,cols,2),np.uint8)
mask[r-30:r+30, c-30:c+30] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(141),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(142),plt.imshow(img_back, cmap = 'gray')
plt.title('img_back_low_pass'), plt.xticks([]), plt.yticks([])
plt.subplot(143),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(144),plt.imshow(angle, cmap = 'gray')
plt.title('angle Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

if cv.waitKey(0) & 0xFF == ord('c'): cv.destroyAllWindows()
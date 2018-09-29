#To get other flags, just run following commands in your Python terminal : 
import cv2 as cv

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )


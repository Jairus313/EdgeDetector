import cv2
import numpy as np

img = cv2.imread('abc.png',0)  # importing image as img
cv2.imshow("Gray",img)
cv2.waitKey(0)

ret,thresh = cv2.threshold(img,90,255,cv2.THRESH_TOZERO) # converting into binary format by thresholding
cv2.imshow('binary',thresh)
cv2.waitKey(0)

guass = cv2.GaussianBlur(thresh,(5,5),0)  # applying gaussian filter for 5x5 resolution
cv2.imshow('guass',guass)
cv2.waitKey(0)

blur = cv2.blur(guass,(1,1))  # blurring for 1x1 resolution
median = cv2.medianBlur(blur,5)  # applying medianBlur for 1x1 resolution
cv2.imshow('noisefree',median)
cv2.waitKey(0)

kernel = np.ones((1,1),np.float32)/100  # making kernel
er = cv2.erode(median,kernel,iterations=5)  # eroding the image for 5 times
open = cv2.morphologyEx(er,cv2.MORPH_CLOSE,kernel) # using morphological method for the kernel.
cv2.imshow('open',open)
cv2.waitKey(0)

canny = cv2.Canny(open,350,350)  # detecting the edge via canny edge detector
cv2.imshow('canny',canny)
cv2.waitKey(0)

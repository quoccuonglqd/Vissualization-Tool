from __future__ import absolute_import
import cv2 as cv
from imagecorruption import *

img = cv.imread('D:/CMND/final_image/12_easy_0005.jpg')
img = shift(img,20,30)
cv.imshow('image',img)
cv.waitKey(0)
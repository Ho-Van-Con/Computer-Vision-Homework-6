import cv2
import imutils
import numpy as np

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5),(-1,-1))
img = cv2.imread("image.jpg")
img = imutils.resize(img,width=400)
cv2.namedWindow("Original",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Original",img)
cv2.namedWindow("Dest",cv2.cv2.WINDOW_AUTOSIZE)
img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
_ , img_bin_1 = cv2.threshold(img_gray,0,255,cv2.THRESH_TOZERO)
_ , img_bin = cv2.threshold(img_bin_1,120,255,cv2.THRESH_BINARY)
cv2.imshow("Imange Binary",img_bin)
imdest=cv2.dilate(img_bin_1,kernel)
imdest=cv2.erode(imdest,kernel)
cv2.imshow("Dest", imdest)
cv2.waitKey()
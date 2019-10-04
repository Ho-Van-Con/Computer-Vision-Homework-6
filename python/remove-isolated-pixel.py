#REMOVE ISOLATED PIXEL
import cv2
import numpy as np
im=np.zeros((9,10),dtype=np.uint8)
im[4,4]=255
im[8,8]=255
im[3,8]=255
for i in range (2,7):
    im[2,i]=255
    im[6,i]=255
    im[i,2]=255
    im[i,6]=255
cv2.namedWindow( "org", cv2.WINDOW_NORMAL)
cv2.resizeWindow('org',300,300)
cv2.namedWindow( "morp", cv2.WINDOW_NORMAL)
cv2.resizeWindow('morp',300,300)
cv2.imshow('org',im)
kernel=np.array([[0,1,0],[1,0,1],[0,1,0]],np.uint8)
imdilate=cv2.dilate(im,kernel)
cv2.namedWindow( "dilated", cv2.WINDOW_NORMAL)
cv2.resizeWindow('dilated',300,300)
cv2.imshow("dilated",imdilate)
immorph=cv2.bitwise_and(im,imdilate)
cv2.imshow('morp',immorph)
cv2.waitKey(0)
cv2.destroyAllWindows()

#REMOVE ISOLATED PIXEL
import cv2
import numpy as np
im=cv2.imread('isolated.png')
cv2.imshow('org',im)
kernel=np.array([[0,1,0],[1,0,1],[0,1,0]],np.uint8)
imdilate=cv2.dilate(im,kernel)
immorph=cv2.bitwise_and(im,imdilate)
cv2.imshow('morp',immorph)
cv2.waitKey(0)
cv2.destroyAllWindows()

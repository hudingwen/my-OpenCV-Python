import cv2
import numpy as np

img = cv2.imread("./pic/math.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 自适应二值化
dst =cv2.adaptiveThreshold(img1,255
                               ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C
                               ,cv2.THRESH_BINARY,11,0)

print(dst.shape)



cv2.imshow("img",img)
cv2.imshow("img1",img1)
cv2.imshow("dst",dst)
cv2.waitKey(0)
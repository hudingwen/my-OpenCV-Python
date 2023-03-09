import cv2
import numpy as np

img = cv2.imread("./pic/pig.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化
# 阈值 160
ret,dst =cv2.threshold(img1,160,255,cv2.THRESH_BINARY)
# 反向
# ret,dst =cv2.threshold(img1,160,255,cv2.THRESH_BINARY_INV)
print(dst.shape)



cv2.imshow("img",img)
cv2.imshow("img1",img1)
cv2.imshow("dst",dst)
cv2.waitKey(0)
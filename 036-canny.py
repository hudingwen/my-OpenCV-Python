import cv2
import numpy as np

# 边缘检测
img = cv2.imread("./pic/mxd/5.png")
dst = cv2.Canny(img,50,200)


cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey(0)
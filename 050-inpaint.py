import cv2
import numpy as np

# 图像修复

# 需要被修复的图片
img = cv2.imread("./pic/mxd/test/sample/b1.jpg")

# 抠出要修复的图片
mask = cv2.imread("./pic/mxd/test/sample/b2.jpg",0)


dst = cv2.inpaint(img,mask,5,cv2.INPAINT_TELEA)

cv2.imshow("dst",dst)

cv2.waitKey()
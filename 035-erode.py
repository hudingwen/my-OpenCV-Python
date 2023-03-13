import cv2
import numpy as np

img = cv2.imread("./pic/fushi.png")
# kernal = np.ones((7,7),np.uint8)

# MORPH_RECT 全是1
# MORPH_ELLIPSE 椭圆
# MORPH_CROSS 十字架
kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
# 腐蚀
# dst = cv2.erode(img,kernal,iterations=2)
# 膨胀
# dst = cv2.dilate(img,kernal,iterations=2)
# 开运算 腐蚀+膨胀 (消除外边的噪点)
# dst = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)
# 闭运算 膨胀+腐蚀 (消除里边的噪点)
# dst = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)
# 梯度运算 (可实现边缘查找)
# kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# dst = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernal)
# 顶帽运算 寻找外面的噪点
# kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
# dst = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernal)
# 黑帽运算 寻找里面的噪点
img = cv2.imread("./pic/fushi2.png")
kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
dst = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernal)

# 顶帽变换用于凸显暗背景上的亮物体。（也可叫白帽）
# 底帽变换用于凸显亮背景上的暗物体。（也可叫黑帽）

cv2.imshow("img",img) 
cv2.imshow("dst",dst)
cv2.waitKey(0)
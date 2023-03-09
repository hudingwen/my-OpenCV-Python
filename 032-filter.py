import cv2
import numpy as np

img = cv2.imread("./pic/pig.jpg")
# 卷积滤波
# kernal = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernal)
# 均值滤波
# dst = cv2.blur(img,(5,5))
# 高斯滤波
# dst = cv2.GaussianBlur(img,(5,5),sigmaX=1)
# 中值滤波 - 椒盐噪声处理
# img = cv2.imread("./pic/hujiao.jpg")
# dst = cv2.medianBlur(img,3)
# 双边滤波 - 美颜处理
# img = cv2.imread("./pic/face.jpg")
# dst = cv2.bilateralFilter(img,3,20,50)
# 高通滤波-索贝尔算子y方向边缘
# img = cv2.imread("./pic/chess.jpg")
# dst =cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
# 高通滤波-索贝尔算子x方向边缘
# dst2 =cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
# dst3 = cv2.add(dst,dst2)
# 高通滤波-沙尔算子(和索菲尔算子类似,但是只能求x或者y)
# img = cv2.imread("./pic/chess.jpg")
# dst = cv2.Scharr(img,cv2.CV_64F,1,0)
# dst2 = cv2.Scharr(img,cv2.CV_64F,0,1)
# dst3 = cv2.add(dst,dst2)
# 高通滤波-拉普拉斯算子(同时检测两个方向的边缘 对噪声敏感 一般先去噪在用拉普拉斯)
img = cv2.imread("./pic/chess.jpg")
dst = cv2.Laplacian(img,cv2.CV_64F,ksize=5)



cv2.imshow("img",img)
cv2.imshow("dst",dst)
# cv2.imshow("dst2",dst2)
# cv2.imshow("dst3",dst3)
cv2.waitKey(0)
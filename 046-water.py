# 导入库
import cv2
import numpy as np

from matplotlib import pyplot as plt

# 图像分割

# 获取背景
# 1.通过二值法得到黑白图片
# 2.通过形态学获取背景

img  = cv2.imread("./pic/water.png")

# img  = cv2.imread("./pic/mxd/test/sample/b56.jpg")

# 灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 自适应二值法
ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel =np.ones((3,3),np.int8)
# 开运算
open1 = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=5)
# 膨胀
bg = cv2.dilate(open1,kernel,iterations=1)
 # 获取前景物体
dst = cv2.distanceTransform(open1,cv2.DIST_L2,5)


ret,fg =  cv2.threshold(dst,0.7*dst.max(),255,cv2.THRESH_BINARY)

# 梯度显示
# plt.imshow(dst,cmap='gray')
# plt.show()
# exit()

# 获取未知区域
fg = np.uint8(fg)
unknow = cv2.subtract(bg,fg)

# 创建连通域
ret,marker =cv2.connectedComponents(fg)
marker = marker+1
marker[unknow==255]=0

# 进行图像分割
result = cv2.watershed(img,marker)

img[result==-1] = [0,0,255]

cv2.imshow("img",img)

cv2.imshow("unknow",unknow)
cv2.imshow("fg",fg)
cv2.imshow("dst",dst)

cv2.imshow("open1",open1)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
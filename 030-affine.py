import cv2
import numpy as np

dog = cv2.imread("./pic/pig.jpg")
h,w,ch =  dog.shape
# 自定义平移量
# [1, 0, 100] 向右平移
# [0, 1, 150] 向下平移
# M = np.float32([[1, 0, 100], [0, 1, 150]])
# 使用cv提供的
# 参数1 中心点
# 参数2 旋转角度
# 参数3 缩放
# M = cv2.getRotationMatrix2D((100,100),15,0.3)
src = np.float32([[400,300],[800,300],[400,500]])
dst = np.float32([[200,400],[600,500],[150,600]])
M = cv2.getAffineTransform(src,dst)
# 仿射(平移,旋转,翻转等.)
# 变换矩阵
new = cv2.warpAffine(dog,M,(w,h))

cv2.imshow("dog",dog)
cv2.imshow("new",new)
cv2.waitKey(0)

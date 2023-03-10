import numpy as np
import cv2

# a = np.array([1,2,3])
# print(a)
# print("-------")
# b = np.array([[1,2,3],[4,5,6]])
# print(b)
# print("-------")
# c = np.zeros((8,8,3),np.uint8)
# print(c)
# print("-------")
# d = np.ones((8,8),np.uint8)
# print(d)
# print("-------")
# e = np.full((8,8),10,np.uint8)
# print(e)
# print("定义单位矩阵-斜对角都为1")
# f = np.identity(8)
# print(f)
# print("非正方形举证-末尾1是表示从第一行第几个开始")
# g = np.eye(5,7,1)
# print(g)

# 获取子矩阵
img = np.zeros((480,640,3),np.uint8)
roi = img[100:400,100:600]
roi[:,:] = [0,0,255]  #另一种写法roi[:] = [0,0,255]
roi[10:200,10:200] = [0,255,0]
cv2.imshow("img",roi)
key = cv2.waitKey(0)
if key & 0xff == ord("q"):
    cv2.destroyAllWindows()

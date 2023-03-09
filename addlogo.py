# 添加logo
# 1.引入一张图片
# 2.要有一张logo
# 3.计算图片在什么地方添加,在添加的地方变成黑色
# 利用add,将logo与图片叠加到一起
import cv2
import numpy as np
# 导入图片
dog = cv2.imread("./pic/pig.jpg")
print(dog.shape)
# 创建logo
logo = np.zeros((200,200,3),np.uint8)
mask = np.zeros((200,200),np.uint8)
# 绘制logo
logo[20:120,20:120] = [0,0,255]
logo[80:180,80:180] = [0,255,0]
# 绘制掩码
mask[20:120,20:120] = 255
mask[80:180,80:180] = 255
# 对mask按位求反
m = cv2.bitwise_not(mask)
# 选择logo添加到图片的位置
roi = dog[0:200,0:200]
# 与m做与操作
tmp = cv2.bitwise_and(roi,roi,mask=m)
# 叠加
dst = cv2.add(tmp,logo)
# 区域赋值
dog[0:200,0:200] = dst

cv2.imshow("dst",dst)
cv2.imshow("tmp",tmp)
cv2.imshow("m",m)
cv2.imshow("mask",mask)
cv2.imshow("logo",logo)
cv2.imshow("dog",dog)
cv2.waitKey(0)
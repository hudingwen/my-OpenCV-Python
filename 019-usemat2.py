import cv2
import numpy as np


img = cv2.imread("./pic/1.jpg")

#shape有三个属性高度,宽度,通道
print(img.shape)
#图像占用空间
#高度 * 宽度 * 通道
print(img.size)
#图像中每个元素的位深 uint8 无符号8位 取值0-255
print(img.dtype)
import cv2
import numpy as np

back = cv2.imread("./pic/1.jpg")
small = cv2.imread("./pic//1.jpg")

print(back.shape)
print(small.shape)
# 图像融合/溶合
# 参数
# 图像1
# 图像1权重
# 图像2
# 图象2权重
# 整体权重
result = cv2.addWeighted(small,0.7,back,0.3,0.5)
cv2.imshow("add2",result)
cv2.waitKey(0)
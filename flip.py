import cv2
import numpy as np

dog = cv2.imread("./pic/pig.jpg")
# 上下翻转
# new = cv2.flip(dog,0)
# 上下翻转
# new = cv2.flip(dog,1)
# 上下左右翻转
new = cv2.flip(dog,-1)



cv2.imshow("dog",dog)
cv2.imshow("new",new)
cv2.waitKey(0)
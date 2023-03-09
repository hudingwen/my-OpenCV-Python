import cv2
import numpy as np


dog = cv2.imread("./pic/pig.jpg")
# 90度旋转
# new = cv2.rotate(dog,cv2.ROTATE_90_CLOCKWISE)
# 180度旋转
new = cv2.rotate(dog,cv2.ROTATE_180)

cv2.imshow("dog",dog)
cv2.imshow("new",new)
cv2.waitKey(0)
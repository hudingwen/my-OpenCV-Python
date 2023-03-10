import cv2
import numpy as np

dog = cv2.imread("./pic/pig.jpg")
# 固定尺寸缩放
# 注意:这里size和shap的size是相反的
# new = cv2.resize(dog,(400,400))
# 按比例缩放
new = cv2.resize(dog,None,fy=0.3,fx=0.3)

cv2.imshow("dog",dog)
cv2.imshow("new",new)
cv2.waitKey(0)
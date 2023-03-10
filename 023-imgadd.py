import cv2
import numpy as np

dog = cv2.imread("./pic/1.jpg")

print(dog.shape)

img = np.ones((2500,4000,3),np.uint8)*50
cv2.imshow("orig",dog)
# 两张图相加时大小必须一致
result = cv2.add(dog,img)
cv2.imshow("result",result)
# 图像相减 result - img
orgi_1 = cv2.subtract(result,img)
cv2.imshow("orgi_1",orgi_1)
# 图像相乘
orgi_2 = cv2.multiply(result,img)
cv2.imshow("orgi_2",orgi_2)
# 图像相除
orgi_3 = cv2.divide(result,img)
cv2.imshow("orgi_3",orgi_3)

cv2.waitKey(0)
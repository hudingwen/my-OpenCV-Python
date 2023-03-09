import cv2
import numpy as np

img = cv2.imread("./pic/math.jpg")
# 透视变换
# 参数1 左上角
# 参数2 右上角
# 参数3 左下角
# 参数4 右下角
src = np.float32([[38,100],[440,100],[38,560],[440,560]])
# 需要放置的图像大小的四个位置
dst = np.float32([[0,0],[500,0],[0,600],[500,600]])
M = cv2.getPerspectiveTransform(src,dst)
new = cv2.warpPerspective(img,M,(500,600))

cv2.imshow("img",img)
cv2.imshow("new",new)
cv2.waitKey(0)

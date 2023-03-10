import cv2
import numpy as np

blockSize = 2
ksize = 3
k = 0.04

maxCrners = 1000
ql = 0.01
minDistance = 10
# 加载
img = cv2.imread("./pic/chess.jpg")
# 灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# harris角点检测
# dst = cv2.cornerHarris(gray,blockSize,ksize,k)
# harris角点展示
# img[dst>0.01*dst.max()] = [0,0,255]
# Shi-Tomasi绘制角点
corners = cv2.goodFeaturesToTrack(gray,maxCrners,ql,minDistance)
corners = np.int32(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(255,0,0),-1)

cv2.imshow("harris",img)
cv2.waitKey(0)

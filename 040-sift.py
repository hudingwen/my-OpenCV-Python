import cv2
import numpy as np

# 特征点匹配
# 加载
# img = cv2.imread("./pic/chess.jpg")
img1 = cv2.imread("./pic/mxd/1.png")
img2 = cv2.imread("./pic/mxd/b7.jpg")
 
# 灰度化
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
g1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
g2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.SIFT_create()
# 创建orb对象
# orb =cv2.ORB_create()

# 进行检测
# kp = sift.detect(gray,None)
# kp ,des = sift.detectAndCompute(gray,None)
# kp ,des = orb.detectAndCompute(gray,None)
kp1 ,des1 = sift.detectAndCompute(g1,None)
kp2 ,des2 = sift.detectAndCompute(g2,None)
# 暴力特征匹配
bf = cv2.BFMatcher(cv2.NORM_L1)
match = bf.match(des1,des2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,match,None)
cv2.imshow("img3",img3)

# 画出特征点
# cv2.drawKeypoints(gray,kp,img)

# cv2.imshow("img",img)
cv2.waitKey(0)
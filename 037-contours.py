import cv2
import numpy as np

# 定义画线函数
def drawShape(src,points):
    i = 0
    while i <len(points):
        if(i == len(points)-1):
            x,y = points[i][0]
            x1,y1 = points[0][0]
            cv2.line(src,(x,y),(x1,y1),(0,0,255),5)
        else:
            x,y = points[i][0]
            x1,y1 = points[i+1][0]
            cv2.line(src,(x,y),(x1,y1),(0,0,255),5)
        i = i+1

# 轮廓查找
# img = cv2.imread("./pic/outline.jpg")
# img = cv2.imread("./pic/hand.png")
img = cv2.imread("./pic/hello.jpg")

print(img.shape)
# 灰值化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)
# 二值化
ret,binary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
# 轮廓查找
# contours 轮廓
# hierarchy 层级
# RETR_EXTERNAL 外层
# RETR_TREE 树
contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
# 绘制轮廓
cv2.drawContours(img,contours,-1,(0,255,0),1)
# 轮廓面积计算
area = cv2.contourArea(contours[0])
print("area=%d"%(area))
# 轮廓周长计算
lenNum = cv2.arcLength(contours[0],True)
print("lenNum=%d"%(lenNum))

# 多边形逼近和凸包
# k = 0
# e = 20
# while k < len(contours):
#     # 逼近
#     approx = cv2.approxPolyDP(contours[k],e,True)
#     drawShape(img,approx)
#     # 凸包
#     approx = cv2.convexHull(contours[k])
#     drawShape(img,approx)
#     k = k+1

# 最小外接矩阵
r = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(r)
print(box)
box = np.int32(box)
cv2.drawContours(img,[box],0,(0,0,255),2)
# 最大外接矩阵
x,y,w,h = cv2.boundingRect(contours[1])
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


print(binary.shape)
cv2.imshow("binary",binary)
cv2.imshow("gray",gray)
cv2.imshow("img",img)
cv2.waitKey(0)
import cv2
import numpy as np

# flann特征点匹配
# 加载
img1 = cv2.imread("./pic/mxd/1.png")
img2 = cv2.imread("./pic/mxd/b7.jpg")

# 灰度化
g1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
g2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.SIFT_create()

# 计算描述子和特征点
kp1 ,des1 = sift.detectAndCompute(g1,None)
kp2 ,des2 = sift.detectAndCompute(g2,None)

# 创建匹配器
index_params = dict(algorithm=1,tress=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params,search_params)

# 描述子进行匹配计算
matchs = flann.knnMatch(des1,des2,k=2)
good = []
for i,(m,n) in enumerate(matchs):
    if m.distance < 0.7 * n.distance:
        good.append(m)

# 图像查找
if len(good) >= 4:
    srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    H,_ = cv2.findHomography(srcPts,dstPts,cv2.RANSAC,5.0)

    h,w = img1.shape[:2]
    pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,H)

    cv2.polylines(img2,[np.int32(dst)],True,(0,0,255))
else:
    print("not found")
    exit()

# 匹配绘制
ret = cv2.drawMatchesKnn(img1,kp1,img2,kp2,[good],None)


cv2.imshow("ret",ret)
cv2.waitKey(0)


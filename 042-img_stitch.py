import cv2
import numpy as np

def stitch_image(img1,img2,H):
    # 1.获得每张图片的四个角点
    # 2.对图片进行变换(单应性矩阵使图进行旋转,平移)
    # 3.创建一张大图,将两张图拼接到一起
    # 4.将结果输出
    h1,w1 = img1.shape[:2]  #拿到数组前两个属性
    h2,w2 = img2.shape[:2]  #拿到数组前两个属性
    img1_dims = np.float32([[0,0],[0,h1],[w1,h1],[w1,0]]).reshape(-1,1,2)
    img2_dims = np.float32([[0,0],[0,h2],[w2,h2],[w2,0]]).reshape(-1,1,2)
    img1_stransform = cv2.perspectiveTransform(img1_dims,H)
    result_dims =  np.concatenate((img2_dims,img1_stransform),axis=0)
    [x_min,y_min] = np.int32(result_dims.min(axis=0).ravel()-0.5)
    [x_max,y_max] = np.int32(result_dims.max(axis=0).ravel()+0.5)
    # 平移的距离
    transform_dist = [-x_min,-y_min]
    transform_array = np.array([[1,0,transform_dist[0]],[0,1,transform_dist[1]],[0,0,1]])
    result_img = cv2.warpPerspective(img1,transform_array.dot(H),(x_max-x_min,y_max-y_min))
    result_img[transform_dist[1]:transform_dist[1]+h2
               ,transform_dist[0]:transform_dist[0]+w2] = img2
    return result_img
def get_home(img1,img2):
    # 1.创建特征转换对象
    # 2.通过特征转换对象活得特征点和描述子
    # 3.创建特征匹配器
    # 4.进行特征匹配
    # 5.过滤特征并验证找出有效的特征匹配点
    sift =cv2.SIFT_create()
    g1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    k1 ,d1 = sift.detectAndCompute(g1,None)
    k2 ,d2 = sift.detectAndCompute(g2,None)
    # 创建特征匹配器
    bf = cv2.BFMatcher()
    maches = bf.knnMatch(d1,d2,k=2)

    verify_ratio = 0.8
    verify_matches = []
    for m1,m2 in maches:
        if m1.distance < verify_ratio * m2.distance:
            verify_matches.append(m1)
    min_matches = 8
    if len(verify_matches) > min_matches:
        img1_pts = []
        img2_pts = []
        for m in verify_matches:
            img1_pts.append(k1[m.queryIdx].pt)
            img2_pts.append(k2[m.trainIdx].pt)
        # [(x1,y1),(x2,y2),...]
        # [[x1,y1],[x2,y2],...]
        img1_pts = np.float32(img1_pts).reshape(-1,1,2)
        img2_pts = np.float32(img2_pts).reshape(-1,1,2)
        H,mask = cv2.findHomography(img1_pts,img2_pts,cv2.RANSAC,5.0)
        return H
    else:
        print("not enough matches")
        exit()
# 图像合并
# 第一步,读取文件,把图片设置一样大小
# 第二步,找特征点,描述子.计算单元性矩阵
# 第三步,根据单应性矩阵对图像进行变换,然后平移
# 第四步,拼接并输出最终结果

# 读取两张图片
img1 = cv2.imread("./pic/pin1.jpg")
img2 = cv2.imread("./pic/pin2.jpg")

# 将两张图片大小调成一致
img1 = cv2.resize(img1,(np.int32(1440/2),np.int32(1080/2)))
img2 = cv2.resize(img2,(np.int32(1440/2),np.int32(1080/2)))

inputs = np.hstack((img1,img2))
# 获得单应性矩阵
H = get_home(img1,img2)
# 
result_image = stitch_image(img1,img2,H)

cv2.imshow("result_image",result_image)
cv2.imshow("inputs",inputs)
cv2.waitKey(0)
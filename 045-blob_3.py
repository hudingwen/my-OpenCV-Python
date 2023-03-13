# 导入库
import cv2
import numpy as np
import sys

# 读取图像.
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b1.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b2.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b3.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b4.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b5.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b6.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b7.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b8.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b9.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b10.jpg" )
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b11.jpg" )
# img = cv2.imread("D:\\hudingwen\\github\\TestKeyBoard\\TestKeyboard\\bin\\x64\Debug\\pics\\20230311224520.jpg" )
# img = cv2.imread("D:\\hudingwen\\github\\TestKeyBoard\\TestKeyboard\\bin\\x64\Debug\\pics\\20230312133046.jpg" )

sample = sys.argv[1] 
sample2 = "{}".format(sample) 
img = cv2.imread(sample2)  


 

# 灰值化
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# 二值化
# ret,dst =cv2.threshold(img,170,255,cv2.THRESH_BINARY)
# 形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# 膨胀
dilate = cv2.dilate(dst,kernel,iterations=0)
# 腐蚀
dilate = cv2.erode(dilate,kernel)  
# cv2.imshow("dst",dilate)
# cv2.waitKey()
# exit()
# 膨胀
# dilate = cv2.dilate(dst,kernel,iterations=0)
# # 腐蚀
# dilate = cv2.erode(dilate,kernel)
# 灰值化
# dilate = cv2.cvtColor(dilate, cv2.COLOR_BGR2GRAY) 
# # 膨胀
# dilate = cv2.dilate(dst,kernel,iterations=0)
# # 腐蚀
# dilate = cv2.erode(dilate,kernel)
# # 灰值化
# dilate = cv2.cvtColor(dilate, cv2.COLOR_BGR2GRAY)  
dilate = 255 - dilate 
# dilate = cv2.dilate(dilate,kernel,iterations=0) 

ret,dilate =cv2.threshold(dilate,170,255,cv2.THRESH_BINARY)
# cv2.imshow("tmp", dst)
#寻找轮廓  
contours, hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE  )  
#矩形列表  
box_ji=[]  
#根据轮廓绘制矩形  
for i in range(len(contours)):  
    
    area = cv2.contourArea(contours[i])  
    x, y, w, h = cv2.boundingRect(contours[i])  
    # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  
    rect = cv2.minAreaRect(contours[i]) #提取矩形坐标  
    box = cv2.boxPoints(rect)  
    box = np.int32(box)  
    angle =abs(abs(rect[2])-45)  
    length = max(rect[1])  
    width = min(rect[1])  


    width = max(box, key=lambda x: x[0])[0] - min(box, key=lambda x: x[0])[0]
    height = max(box, key=lambda x: x[1])[1] - min(box, key=lambda x: x[1])[1]
    if width < 195 or width > 205:
        continue
    if height < 45 or height > 55:
        continue
    # print(width)
    # print(height)
    print("{'success':true,'msg':'图像识别成功'}")
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)  
    # box_ji.append(box)  
    # cv2.imshow("Keypoints", img)
    # cv2.waitKey(0)
    exit()
    break
print("{'success':false,'msg':'图像识别失败'}")
exit()
    
    
    
 
    

# dilate=cv2.adaptiveThreshold(dilate,200,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,5)


# # 用默认参数设置检测器
# ver = (cv2.__version__).split('.')
# if int(ver[0]) < 3:
#     detector = cv2.SimpleBlobDetector()
# else:
#     detector = cv2.SimpleBlobDetector_create()

# # 检测blobs
# keypoints = detector.detect(dilate)

# # 用红色圆圈画出检测到的blobs
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS 确保圆的大小对应于blob的大小
# im_with_keypoints = cv2.drawKeypoints(dilate, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 结果显示
# cv2.imshow("Keypoints", img)
# cv2.waitKey(0)

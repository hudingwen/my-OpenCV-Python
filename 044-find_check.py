import cv2
import numpy as np
 
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b1.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b2.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b3.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b4.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b5.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b6.jpg" )  # 出不来
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b7.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b8.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b9.jpg" )  
# img = cv2.imread("D:\\hudingwen\\github\\my-OpenCV-Python\\pic\\mxd\\test\\sample\\b10.jpg" )  
img = cv2.imread("D:\\hudingwen\\github\\TestKeyBoard\\TestKeyboard\\bin\\x64\Debug\\pics\\20230311224527.jpg" )  

 

# 灰值化
# gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY) 
# 二值化
ret,dst =cv2.threshold(img,160,255,cv2.THRESH_BINARY_INV)
# 形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

 # 膨胀
dilate = cv2.dilate(dst,kernel,iterations=0)

dilate = cv2.erode(dilate,kernel)
dilate = cv2.cvtColor(dilate, cv2.COLOR_BGR2GRAY) 
# dilate = cv2.dilate(dilate,kernel,iterations=0)
# dilate = cv2.erode(dilate,kernel) 
 
# 腐蚀 去掉图中小斑块
# 形态学
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# erode = cv2.erode(mask,kernel)
# # 膨胀 还原放大
# dilate = cv2.dilate(erode,kernel,iterations=2)
# # 闭操作 去掉物体内部小块
# close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
# close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
# # 查找轮廓
# cnts,h = cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

 
cv2.imshow("img_gray",dilate)


cv2.waitKey(0)
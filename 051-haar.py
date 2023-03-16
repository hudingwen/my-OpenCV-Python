import cv2
import numpy as np


# Haar人脸识别

# 第一步 创建Haar级联器

# 导入人脸数据
facer = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")
# 导入眼睛数据
eyer = cv2.CascadeClassifier("./haarcascades/haarcascade_eye.xml")
 




#第二步 导入人脸识别的图片并将其灰度化


img = cv2.imread("./pic/home.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 第三部 进行人脸识别
# [[x,y,w,h]]
faces = facer.detectMultiScale(gray,1.1,5)

i = 0
# 圈出人脸
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    # 取出
    roi_img = img[y:y+h,x:x+w]
    eyes = eyer.detectMultiScale(roi_img,1.1,5)
    # 圈出眼睛
    for(x,y,w,h) in eyes:
        cv2.rectangle(roi_img,(x,y),(x+w,y+h),(0,255,0),2)
    i+=1
    winname = "face"+str(i)
    cv2.imshow(winname,roi_img)
cv2.imshow("img",img)
cv2.waitKey()

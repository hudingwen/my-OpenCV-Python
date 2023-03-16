import cv2
import numpy as np

import pytesseract

# 车牌识别

# 第一步 创建Haar级联器

# 导入训练数据
plate = cv2.CascadeClassifier("./haarcascades/haarcascade_russian_plate_number.xml")
 

#第二步 导入车牌识别的图片并将其灰度化

img = cv2.imread("./pic/car.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 第三部 车牌定位
# [[x,y,w,h]]
plates = plate.detectMultiScale(gray,1.1,5)

i = 0
# 圈出人脸
for(x,y,w,h) in plates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
# 对获取到的车牌进行预处理
# 1 提取roi
roi = gray[y:y+h,x:x+w]
# 2 进行二值化
ret,roi_bin = cv2.threshold(roi,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# 代用tesseract识别
txt = pytesseract.image_to_string(roi,lang="chi_sim+eng",config="--psm 8 --oem 3")
print(txt)
cv2.imshow("roi_bin",roi_bin)
cv2.imshow("img",img)
cv2.waitKey()

import cv2
import numpy as np

# 读取图像，包括alpha通道 
img = cv2.imread("./pic\\mxd\\test\\sample\\b12.jpg" ,cv2.IMREAD_UNCHANGED)




alpha = img[:, :, 3]
mask = np.zeros_like(alpha)
mask[alpha > 0] = 255


contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

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
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)  
    box_ji.append(box)  
cv2.imshow("Keypoints", img)
cv2.waitKey(0)
    
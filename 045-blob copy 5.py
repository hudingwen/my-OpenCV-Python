# 导入库
import cv2
import numpy as np
import sys

 


 
 # 灰值化


# colorCount = 1
# while colorCount < 255:
#     colorCount+=2
#     # 二值化
    
#     dilate = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#     # ret,dilate =cv2.threshold(img,colorCount,255,cv2.THRESH_BINARY)
 

# #   cv2.imwrite("1.jpg", dilate)
#     cv2.imshow("dilate", dilate)
#     cv2.waitKey(0) 

colorCount = 1
while colorCount < 255:
    img = cv2.imread("./pic\\mxd\\test\\sampleOther\\{}.jpg".format(1))
    # 灰值化
    dilate = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   


    
    # 二值化
    ret,dilate =cv2.threshold(dilate,colorCount,255,cv2.THRESH_BINARY_INV) 
    
    cv2.imshow("dilate", dilate) 
    cv2.waitKey(0) 
    colorCount+=1
cv2.destroyAllWindows()
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
sample = sys.argv[1] 
sample2 = "{}".format(sample) 
img = cv2.imread(sample2)  


tempFlag = 1

countFind = 0
countNoFind = 0
# pid = 0
# while pid < 59:
pid = tempFlag - 1
while pid < tempFlag:
    fileId = pid + 1
    # 下一个
    pid+=1
    # img = cv2.imread("./pic\\mxd\\test\\sample\\b{}.jpg".format(fileId))
    isFind = False

    # arr = [1,10,30,60,90,95,100,105,110,115,120,150,180,210,240,254]
    # idx = 0
    # while idx < len(arr):
    #     colorCount = arr[idx]
    #     # 下一个
    #     idx+=1
    idx = 1
    while idx < 255:
        colorCount = idx
        # 下一个
        idx+=1
        # 二值化
        ret,dilate =cv2.threshold(img,colorCount,255,cv2.THRESH_BINARY_INV)
        # 形态学kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
        
        # # 膨胀
        dilate = cv2.dilate(dilate,kernel,iterations=0)
        # # 腐蚀
        dilate = cv2.erode(dilate,kernel)
        # cv2.imshow("img{}".format(colorCount),dilate) 
        # # # 膨胀
        # dilate = cv2.dilate(dilate,kernel,iterations=0)
        # # # 腐蚀
        # dilate = cv2.erode(dilate,kernel)

        # 灰值化
        dilate = cv2.cvtColor(dilate, cv2.COLOR_BGR2GRAY) 
        # 二值化
        ret,dilate =cv2.threshold(dilate,colorCount,255,cv2.THRESH_BINARY_INV) 



        #寻找轮廓  
        
        contours, hierarchy = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    
        #根据轮廓绘制矩形  
        
        for i in range(len(contours)):  
            
            area = cv2.contourArea(contours[i])  
            x, y, w, h = cv2.boundingRect(contours[i])  
            rect = cv2.minAreaRect(contours[i]) #提取矩形坐标  
            box = cv2.boxPoints(rect)  
            box = np.int32(box)  
            width = max(box, key=lambda x: x[0])[0] - min(box, key=lambda x: x[0])[0]
            height = max(box, key=lambda x: x[1])[1] - min(box, key=lambda x: x[1])[1]

            # if(fileId == tempFlag):
            #     cv2.drawContours(img, [box], 0, (0, 0, 255), 2)  
             

            
            # print("{}-{}".format(width,height))
            if (width == 201) and (height == 49) and box[0][1] == box[1][1] and box[2][1] == box[3][1]:
                # cv2.drawContours(img, [box], 0, (0, 0, 255), 2)  
                isFind = True 
                # print("{}找到了(小框):".format(fileId))
                print("{'success':true,'msg':'图像识别成功(小框)'}")
                # if(fileId == 22):
                # if(True):
                #     print("{}-{}".format(width,height))
                #     cv2.imshow("img",img) 
                #     cv2.waitKey()
                countFind+=1
                # print("{}-{}".format(width,height))
                break
            if (width == 239) and (height == 218) and box[0][1] == box[1][1] and box[2][1] == box[3][1]:
                # cv2.drawContours(img, [box], 0, (0, 0, 255), 2)  
                isFind = True 
                # print("{}找到了(大框):".format(fileId))
                print("{'success':true,'msg':'图像识别成功(大框)'}")
                # if(fileId == 22):
                # if(True):
                #     print("{}-{}".format(width,height))
                #     cv2.imshow("img",img) 
                #     cv2.waitKey()
                countFind+=1
                # print("{}-{}".format(width,height))
                break
        if isFind == True:
            break
        # if(fileId == tempFlag):
        #     print("{}-{}".format(width,height))
        #     print(colorCount)
        #     # cv2.imshow("dilate",dilate) 
        #     cv2.imshow("img",img) 
        #     cv2.waitKey()
    if(isFind == False):
        # print("{}没有找到".format(fileId))
        print("{'success':false,'msg':'未找到识别特征'}")
        countNoFind+=1
# success = countFind/(countFind+countNoFind)*100
# print("成功:{},失败:{}".format(countFind,countNoFind))
# percentage = (countFind / (countNoFind+countFind)) * 100
# print(f"成功比例:{percentage:.2f}%")
# cv2.imshow("img",img) 
cv2.waitKey()
cv2.destroyAllWindows()
import cv2
import numpy as np
# 车辆识别
min_w = 80
min_h = 80
# 检测线高度
line_high = 400
# 存放有效车辆数
cars = []
# 线的偏移
offset = 50
# 车的数量
carno = 0
def center(x,y,w,h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x+y1
    cy = y+y1
    return cx,cy
cap = cv2.VideoCapture("./video/cars.mp4")

bgsubmog = cv2.createBackgroundSubtractorMOG2()
bgsubmog2 = cv2.createBackgroundSubtractorMOG2()
# 形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
while True:
    ret,frame = cap.read()
    if(ret == True): 
        frame = cv2.resize(frame,None,fy=0.5,fx=0.5)
        # 灰度
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 高斯去燥
        blur = cv2.GaussianBlur(gray,(3,3),5)
        # 去背景
        mask = bgsubmog.apply(blur)
        # 腐蚀 去掉图中小斑块
        erode = cv2.erode(mask,kernel)
        # 膨胀 还原放大
        dilate = cv2.dilate(erode,kernel,iterations=2)
        # 闭操作 去掉物体内部小块
        close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
        close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
        # 查找轮廓
        cnts,h = cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        # 画线
        cv2.line(frame,(10,line_high),(960,line_high),(255,255,0),3)
        for(i ,c) in enumerate(cnts):
            (x,y,w,h) =cv2.boundingRect(c)
            # 对有效的车辆进行判断
            isValid = (w>=min_w) and (h>=min_h)
            if( not isValid):
                continue

            # 到这里都是有效的车
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cpoint = center(x,y,w,h)
            cars.append(cpoint)

            for(x,y) in cars:
                # 要有一条线
                # 有范围 20
                # 从数组中减去
                if((y > line_high-offset) and( y<line_high+offset)):
                    carno +=1
                    cars.remove((x,y))
                    print(carno)
                
           
        cv2.putText(frame,"cars count:"+str(carno),(450,60),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0),5)
        cv2.imshow("frame",frame) 
        # cv2.imshow("close",close) 
        # cv2.imshow("mask",mask) 

        # 没有降噪
        # mask2 = bgsubmog2.apply(frame)
        # cv2.imshow("mask2",mask2) 
    key = cv2.waitKey(40)
    if(key & 0xff == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
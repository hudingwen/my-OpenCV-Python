# 基本功能
# 可以通过鼠标进行基本绘制
# 1.画线 当用户按下l键 即选着了画线,此时滑动鼠标即可画线
# 1.画矩形 当用户按下r键 即选着了画矩形,此时滑动鼠标即可画矩形
# 1.画圆 当用户按下c键 即选着了画圆,此时滑动鼠标即可画圆

import cv2
import numpy as np

# 0-画线 1-画矩形 2-画圆
curshap = 0
startpos = (0,0)
# 显示窗口和背景
img = np.zeros((640,180,3),np.uint8)
# 鼠标回调函数
def mouse_callback(event,x,y,flags,userdata):
    global curshap,startpos
    # print(event,x,y,flags,userdata)
    if(event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        startpos = (x,y)
    elif(event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if curshap == 0:
            cv2.line(img,startpos,(x,y),(0,0,255))
        elif curshap == 1:
            cv2.rectangle(img,startpos,(x,y),(0,0,255))
        elif curshap == 2:
            a = (x - startpos[0])
            b = (y - startpos[1])
            r = int((a**2+b**2)**0.5)
            cv2.circle(img,startpos,r,(0,0,255))
        else:
            print("err:no shape")
# 创建窗口
cv2.namedWindow("drawshap",cv2.WINDOW_NORMAL)
# 设置鼠标回调函数
cv2.setMouseCallback("drawshap",mouse_callback)

while True:
    cv2.imshow("drawshap",img)
    key = cv2.waitKey(1) & 0xff
    if(key == ord('q')):
        break
    elif key == ord('l'):
        curshap = 0
    elif key == ord('r'):
        curshap = 1
    elif key == ord('c'):
        curshap = 2

cv2.destroyAllWindows()
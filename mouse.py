import cv2
import numpy as np
def mouse_callback(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)
# mouse_callback(1, 100, 100, 16, "666")

cv2.namedWindow("mouse",cv2.WINDOW_NORMAL)
#设置窗口大小
cv2.resizeWindow("mouse",640,480)

cv2.setMouseCallback("mouse",mouse_callback)

img = np.zeros((480,640,3),np.uint8)
while True:
    cv2.imshow("mouse",img)
    key = cv2.waitKey(1)
    if(key & 0xff == ord('q')):
        break
cv2.destroyAllWindows()
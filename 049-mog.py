import cv2
import numpy as np

# MOG去背景
cap =cv2.VideoCapture("./video/cars.mp4")

# mog = cv2.createBackgroundSubtractorMOG2()
mog = cv2.createBackgroundSubtractorKNN()
while(True):
    ret,frame = cap.read()
    fgmask = mog.apply(frame)
    cv2.imshow("fgmask",fgmask)
    k = cv2.waitKey(10)
    # 按esc键退出
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
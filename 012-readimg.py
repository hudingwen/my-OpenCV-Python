import cv2
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
img = cv2.imread("./pic/1.jpg")
cv2.imshow("img",img)
while True:
    
    key = cv2.waitKey(0)
    if(key & 0xff ==ord('q')):
        print("退出了")
        exit()
    if(key & 0xff ==ord('s')):
        cv2.imwrite("D:/360Downloads/desktop/python/my-OpenCV-Python/pic/5.jpg",img)
        print("保存了")
    else:
        print(key)
cv2.destroyAllWindows()
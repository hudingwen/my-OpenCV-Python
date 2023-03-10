import cv2
import time

# 获取当前时间戳
timestamp = time.time()
# 转换为结构化时间
struct_time = time.localtime(timestamp)
nowtime = time.strftime("%Y%m%d%H%M%S", struct_time)
path = './video/out_'+nowtime+'.mp4'
#创建多媒体写入工具
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#保存视频的尺寸要和摄像头尺寸一直否则无法保存
vw = cv2.VideoWriter(path,fourcc, 25,(640,480))


cv2.namedWindow("video",cv2.WINDOW_NORMAL)
#设置窗口大小
cv2.resizeWindow("video",640,480)
#读取摄像头
cap = cv2.VideoCapture(0)
#读取视频文件
#cap = cv2.VideoCapture("./video/索道1.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("video",frame)
        #写数据到多媒体文件
        vw.write(frame)
        key = cv2.waitKey(41)
        if(key & 0xff == ord('q')):
            break
    else:
        break
cap.release()
#释放多媒体写入工具
vw.release()
cv2.destroyAllWindows()
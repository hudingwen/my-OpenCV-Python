#coding=utf-8
import aircv as ac
import cv2
import sys
import numpy as np


def draw_box(img, pos, top_left, right_bottom, circle_radius,  color, line_width):
    # 圈出
    # if not pos:
    #     print("{'success':false,'msg':'图像识别失败'}")
    #     return
    # print("{'success':true,'msg':'图像识别成功'}")
    # 框出圆形
    # cv2.circle(img, pos, circle_radius, color, line_width)
    # 框出矩形
    cv2.rectangle(img, top_left, right_bottom, color, line_width)  # 左上，右下
    cv2.namedWindow("objDetect", 0)  # 创建窗口时候可以鼠标随意拖动窗口改变大小，CV_WINDOW_NORMAL就是0
    # cv2.resizeWindow("objDetect", 640, 480)  # 设置长宽大小为640*480
    # cv2.moveWindow("objDetect", 0, 0)  # 移动窗口到（0,0）坐标
    # cv2.imshow('objDetect', imsrc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def match_pic(img_source, img_target):
    # 匹配
    # imsrc = ac.imread(r"{}".format(img_source))
    # imobj = ac.imread(r"{}".format(img_target))
    imsrc = cv2.imdecode(np.fromfile(img_source,dtype=np.uint8),-1)
    imobj = cv2.imdecode(np.fromfile(img_target,dtype=np.uint8),-1)
     
    pos = ac.find_template(imsrc, imobj, rgb=True, bgremove=True)
    if not pos:
        print("{'success':false,'msg':'未找到识别特征'}", end="")
        return None, None, None
    top_left = pos['rectangle'][0]  # 左上
    right_bottom = pos['rectangle'][3]  # 右下
    circle_center_pos = pos['result']  # 中心点坐标
    circle_center_pos = tuple(map(int, circle_center_pos))
    # print('准确率:', pos['confidence'])
    # print(circle_center_pos)  # 坐标位置  
    if  float(pos['confidence']) >= float(0.7):
        print("{'success':true,'msg':'图像识别成功'}", end="")
    else:
        print("{'success':false,'msg':'未找到识别特征'}", end="")
    return circle_center_pos, top_left, right_bottom



t1 = sys.argv[1] 
img_target = "{}".format(t1) 

t2 = sys.argv[2] 
img_source = "{}".format(t2) 


# img_source = "D:\\hudingwen\\github\\TestKeyBoard\\TestKeyboard\\bin\\x64\\Debug\\pics\\20230315203328.jpg"
# img_source = "D:\\hudingwen\\github\\TestKeyBoard\\TestKeyboard\\bin\\x64\\Debug\\pics\\20230315201936.jpg"
# img_source = "./pic/mxd/test/sampleLun/20230315162142.png" 
# img_source = "./pic/mxd/test/sample/b11.jpg"
# img_target = "./pic/mxd/test/lun.png"

circle_center_pos, top_left, right_bottom = match_pic(img_source, img_target)
circle_radius = 40
color = (0, 0, 255)
line_width = 1
# draw circle
cv2.destroyAllWindows()
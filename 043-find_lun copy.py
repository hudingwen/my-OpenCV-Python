import aircv as ac
import cv2


def draw_box(img, pos, top_left, right_bottom, circle_radius,  color, line_width):
    # 圈出
    if not pos:
        print("{'success':false,'msg':'图像识别失败'}")
        return
    print("{'success':true,'msg':'图像识别成功'}")
    # 框出圆形
    # cv2.circle(img, pos, circle_radius, color, line_width)
    # 框出矩形
    cv2.rectangle(img, top_left, right_bottom, color, line_width)  # 左上，右下
    cv2.namedWindow("objDetect", 0)  # 创建窗口时候可以鼠标随意拖动窗口改变大小，CV_WINDOW_NORMAL就是0
    # cv2.resizeWindow("objDetect", 640, 480)  # 设置长宽大小为640*480
    # cv2.moveWindow("objDetect", 0, 0)  # 移动窗口到（0,0）坐标
    cv2.imshow('objDetect', imsrc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def match_pic(img_source, img_target):
    # 匹配
    imsrc = ac.imread(img_source)
    imobj = ac.imread(img_target)
    pos = ac.find_template(imsrc, imobj, rgb=True, bgremove=True)
    if not pos:
        return None, None, None
    top_left = pos['rectangle'][0]  # 左上
    right_bottom = pos['rectangle'][3]  # 右下
    circle_center_pos = pos['result']  # 中心点坐标
    circle_center_pos = tuple(map(int, circle_center_pos))
    print('准确率:', pos['confidence'])
    print(circle_center_pos)  # 坐标位置
    return circle_center_pos, top_left, right_bottom


# img_source = "./pic/mxd/test/sampleLun/20230315162142.png"
img_source = "./pic/mxd/test/sample/20230311163110.jpg"
img_target = "./pic/mxd/test/lun.png"
circle_center_pos, top_left, right_bottom = match_pic(img_source, img_target)
circle_radius = 40
color = (0, 0, 255)
line_width = 5
# draw circle
imsrc = ac.imread(img_source)
draw_box(imsrc, circle_center_pos, top_left, right_bottom, circle_radius, color, line_width)
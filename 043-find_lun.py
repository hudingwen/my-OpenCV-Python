import cv2
import numpy as np
import sys

# 传入参数
sample = sys.argv[1]
template = sys.argv[2] 
sample2 = "{}".format(sample)
template2 = "{}".format(template)
# sample2 = "D:/hudingwen/github/my-OpenCV-Python/pic/mxd/test/mogu.png"
# template2 = "D:\\hudingwen\\github\\TestKeyBoard\\TestKeyboard\\bin\\x64\\Debug\\pics\\20230311151936.jpg"
# 样本图
template = cv2.imread(sample2,0)
# 原图
img_rgb = cv2.imread(template2)
# 灰值化
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Store width and heigth of template in w and h
w, h = template.shape[::-1]
# Perform match operations.
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# Specify a threshold
# 这里的0.7表示匹配度
threshold = 0.7
# Store the coordinates of matched area in a numpy array
loc = np.where(res >= threshold)
x=loc[0]
y=loc[1]
# Draw a rectangle around the matched region.
if len(x) and len(y):
    for pt in zip(*loc[::-1]):
        # 这里会把匹配到的位置用矩形框给框选出来
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        # cv2.imwrite("f:/12.png", img_rgb)
        # cv2.imshow("test",img_rgb) 
        print("{'success':true,'msg':'图像识别成功'}")
        break
else:
    print("{'success':false,'msg':'图像识别失败'}")
exit()
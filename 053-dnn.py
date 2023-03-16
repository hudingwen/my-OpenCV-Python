from cv2 import dnn
import numpy as np
import cv2


# 深度学习网络

# 1 导入模型，创建神经网络
# 2 读图片，转成张量
# 3 将张量输入到网络中，并进行预测
# 4 得到结果，显示

# 参数描述
# 二进制模型
# -VGG_ILSVRC2016_SSD_300x300_iter_440000.caffemode
# 网络描述
# -ILSVRC2016/SSD_300x300/deploy.prototxt
# 分类信息
# -ILSVRC2016/SSD_300x300/labelmap..det.txt

# https://github.com/PINTO0309/MobileNet-SSD-RealSense/blob/master/caffemodel/MobileNetSSD/MobileNetSSD_deploy.caffemodel


#
# Caffe模型
# prototxt_path = r"C:/Python/Pycharm/docxprocess/face_detector/deploy.prototxt"
# model_path = r"C:/Python/Pycharm/docxprocess/face_detector/res10_300x300_ssd_iter_140000.caffemodel"
config = "./dnn/bvlc_googlenet/deploy.prototxt"
model = "./dnn/bvlc_googlenet/bvlc_googlenet.caffemodel"
net = dnn.readNetFromCaffe(config, model)
print("net")
print(net)
 
# tensorflow模型
# prototxt_path = r"C:/Python/Pycharm/docxprocess/face_detector/opencv_face_detector.pbtxt"
# model_path = r"C:/Python/Pycharm/docxprocess/face_detector/opencv_face_detector_uint8.pb"
# model=cv2.dnn.readNetFromTensorflow(model_path,prototxt_path)


# 读取图片 转换成张张量
img = cv2.imread("./pic/apple3.jpg")

blob = dnn.blobFromImage(img,
                  1.0, # 缩放因子
                  (224,224), # 要求尺寸
                  (104,117,123) #平均差值
                  )
# 将张量输入到网络中，并进行预测
net.setInput(blob)
r =net.forward()
classses = []
path = "./dnn/bvlc_googlenet//synset_words.txt"
with open(path,'rt') as f:
    classses = [x [x.find(" ")+1:] for x in f ]
order =  sorted(r[0],reverse=True)
z = list(range(3))
for i in range(0,3):
    z[i] = np.where(r[0] == order[i])[0][0]
    print("第",i+1,"项,匹配:",classses[z[i]],end='')
    print("类所在行:",z[i]+1," ","可能性:",order[i])
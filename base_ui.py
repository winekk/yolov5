import sys
import cv2
import torch
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from main_window_ui import Ui_MainWindow
from PySide6.QtCore import QTimer
# 格式化为QImage的图片

# 自定义方法 将
def convert2QImage(img):
    height, width, channel = img.shape
    return QImage(img, width, height, width * channel, QImage.Format.Format_RGB888)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.init_model()
        self.init_timer()
        self.setupUi(self)
        self.bind_slots()
        
    def init_timer(self):
        # 创建定时器对象
        self.timer = QTimer()
        # 100ms 间隔执行
        self.timer.setInterval(1)

    # 初始化model 一次加载永久使用
    # model 不设置 则为yolov5s.pt 这种类似的官方模型
    # source 设置为本地资源
    # path 模型地址
    # 首个参数 为项目本地参数 默认为"./"
    def init_model(self):
        self.model = torch.hub.load(
            "./", model="custom", path="runs/train/exp/weights/best.pt", source="local")

    def image_pred(self, file_path):
        results = self.model(file_path)
        # 元组 首位才为class 'numpy.ndarray' 的 多维数组
        image = results.render()[0]
        # 整体操作 image -> Qimage -> Qpixmap
        # 多维数组 -> Qimage
        return convert2QImage(image)

    def open_image(self):
        # 打开图片
        # filter参数为只能打开的文件类型参数 以 ; 分隔
        # 这里的dir  如果选择填入的话 会默认打开这个参数的文档位置 如果不填入 则会打开项目位置
        # 进行选择图片的上传操作
        # 1.可以这样直接选择图片然后通过这个方法把image图片转换为元组 元组[0] 就可以得到QImage的图片
        file_path = QFileDialog.getOpenFileName(
            self, dir="./datasets/images", filter="*.jpg;*.png")
        # ('D:/Dev/YOLOV5/yolov5/datasets/images/30.jpg', '*.jpg;*.png')
        # 很明显返回的是元组
        # 选择了的话 就肯定是有值的 那么我们选择file_path[0] 获取选择文件的路径
        if file_path[0]:
            file_path = file_path[0]
            # 通过自定义函数 通过file_path地址转为Qimage类型图片
            # 2.通过文件地址model进行转换 元组[0]的多维数组 再通过自定义方法 转换为Qimage图片
            qimage = self.image_pred(file_path)
            # 在展示的原图里面 展示刚才点击选择的图片
            # Qimage图片转换为 Qpixmap 前端QT进行展示
            self.input.setPixmap(QPixmap(file_path))
            self.output.setPixmap(QPixmap.fromImage(qimage))

    def open_video(self):
        file_path = QFileDialog.getOpenFileName(
             self, dir="./datasets", filter="*.mp4")
        if file_path[0]:
            file_path = file_path[0]
            self.video = cv2.VideoCapture(file_path)
            self.timer.start()
                
    def vedio_pred(self):
        ret, frame = self.video.read()
        if not ret:
            self.timer.stop()
        else:
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            self.input.setPixmap(QPixmap.fromImage(convert2QImage(frame)))
            results = self.model(frame)
            image = results.render()[0]
            self.output.setPixmap(QPixmap.fromImage(convert2QImage(image)))
        
   

    def bind_slots(self):
        # 这个det_img 是在生成的main_window_ui.py 中的属性函数
        # clicked 点击时间 connect 为连接 相当于 点击这个定位的连接执行open_image函数
        self.det_img.clicked.connect(self.open_image)
        self.pushButton_2.clicked.connect(self.open_video)
        # 绑定计时器逻辑
        self.timer.timeout.connect(self.vedio_pred)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

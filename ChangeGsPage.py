from PyQt5.QtWidgets import *
import cv2
import os

class ChangeGsPage():

    def __init__(self) :
        #定义初始值
        self.inputFilePath = ''
        self.savePath = ''
        self.type = ''
        self.outVideoType = {'mp4':False,'avi':False}
        self.outPicType = {'png':False,'jpg':False}

    def ChangeGsPageUI(self):
        # 功能页面
        self.main_frame = QWidget()

        ## 盒子布局
        self.changeTypeVideo = QLabel('视频')
        self.changeTypePic = QLabel('图片')
        self.file = QPushButton('输入文件')
        self.fileLoad = QPushButton('存储路径')
        self.outVideoLabel = QLabel('输出视频格式:')
        self.outPicLabel = QLabel('输出图片格式:')
        self.outVideoType1 = QLabel('mp4')
        self.outVideoType2 = QLabel('avi')
        self.outPicType1 = QLabel('png')
        self.outPicType2 = QLabel('jpg')
        self.outButton = QPushButton('确认输出')

        self.changeTypeVideoEdit = QRadioButton()
        self.changeTypePicEdit = QRadioButton()
        self.fileEdit = QLineEdit()
        self.fileLoadEdit = QLineEdit()
        self.outVideoType1Edit = QCheckBox()
        self.outVideoType2Edit = QCheckBox()
        self.outPicType1Edit = QCheckBox()
        self.outPicType2Edit = QCheckBox()

        grid_all = QVBoxLayout()
        grid_H1 = QHBoxLayout()
        grid_H2 = QHBoxLayout()
        grid_H4 = QHBoxLayout()
        grid_H3 = QVBoxLayout()

        grid_H3_1 = QHBoxLayout()
        grid_H3_2 = QHBoxLayout()



        grid_H1.addWidget(self.changeTypeVideo)
        grid_H1.addWidget(self.changeTypeVideoEdit)
        grid_H1.addWidget(self.changeTypePic)
        grid_H1.addWidget(self.changeTypePicEdit)
        grid_H2.addWidget(self.file)
        grid_H2.addWidget(self.fileEdit)
        grid_H3_1.addWidget(self.outVideoLabel)
        grid_H3_1.addWidget(self.outVideoType1)
        grid_H3_1.addWidget(self.outVideoType1Edit)
        grid_H3_1.addWidget(self.outVideoType2)
        grid_H3_1.addWidget(self.outVideoType2Edit)
        grid_H3_2.addWidget(self.outPicLabel)
        grid_H3_2.addWidget(self.outPicType1)
        grid_H3_2.addWidget(self.outPicType1Edit)
        grid_H3_2.addWidget(self.outPicType2)
        grid_H3_2.addWidget(self.outPicType2Edit)
        grid_H3.addLayout(grid_H3_1)
        grid_H3.addLayout(grid_H3_2)
        grid_H4.addWidget(self.fileLoad)
        grid_H4.addWidget(self.fileLoadEdit)

        grid_all.addLayout(grid_H1)
        grid_all.addLayout(grid_H2)
        grid_all.addLayout(grid_H4)
        grid_all.addLayout(grid_H3)
        grid_all.addWidget(self.outButton)

        # Qweight添加相关项目
        self.main_frame.setLayout(grid_all)

        self.file.clicked.connect(self.getInputFile)
        self.fileLoad.clicked.connect(self.setLoadPath)
        self.changeTypeVideoEdit.clicked.connect(lambda:self.changeType('video'))
        self.changeTypePicEdit.clicked.connect(lambda:self.changeType('pic'))
        self.outVideoType1Edit.clicked.connect(lambda:self.changeOutType('outVideoType1Edit','outVideoType','mp4'))
        self.outVideoType2Edit.clicked.connect(lambda:self.changeOutType('outVideoType2Edit','outVideoType','avi'))
        self.outPicType1Edit.clicked.connect(lambda:self.changeOutType('outPicType1Edit','outPicType','png'))
        self.outPicType2Edit.clicked.connect(lambda:self.changeOutType('outPicType2Edit','outPicType','jpg'))
        self.outButton.clicked.connect(self.changeGS)
        
        self.main_frame.setStatusTip('格式转换页')
        return self.main_frame
    
    def getInputFile(self):
        fileName,fileType=QFileDialog.getOpenFileName(None,"选取文件",os.getcwd(),"All Files(*);;Text Files(*.txt)")
        self.inputFilePath = fileName
        self.fileEdit.setText(fileName+'type:'+fileType)
    def setLoadPath(self):
        directory1 = QFileDialog.getExistingDirectory(None,"选取文件夹","./")  
        self.savePath = directory1
        self.fileLoadEdit.setText(directory1)
    def changeType(self,connect):
        self.type = connect
        print(self.type)
    def changeOutType(self,box,type,value):
        print(box,type,value)
        if getattr(self,box).isChecked():
            getattr(self,type)[value] = True
        else:
            getattr(self,type)[value] = False
        print(getattr(self,type))
    def changeGS(self):
        if self.type == 'video':
            cap = cv2.VideoCapture(self.inputFilePath)
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            # 获取视频图像宽、高
            size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            # 生成处理后的视频文件
            # 根据原视频，生成新视频文件，
            videoWriter = cv2.VideoWriter(self.savePath+'/'+ self.savePath.split('/')[-1].split('.')[0] +'.mp4', cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), fps, size)
            
            while cap.isOpened():
                # 逐帧读取
                ret, frame = cap.read()
                self.main_frame.setStatusTip('正在读取中')
                # 没有下一帧，关闭循环
                if not ret:
                    self.main_frame.setStatusTip('转存结束')
                    break
                # 转灰度图
                # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # 垂直反转  1水平翻转、0垂直翻转、-1水平垂直翻转
                # frame = cv2.flip(frame, 0)
                # 缩放图像(宽、高)
                # frame = cv2.resize(frame, size)
                # 写入一帧
                videoWriter.write(frame)
                cv2.imshow('frame', frame)
                # 按q退出
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            videoWriter.release()
            cv2.destroyAllWindows()

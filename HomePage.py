from PyQt5.QtWidgets import *
import time

class HomePage:

    def HomePageUI(self):
        # 功能页面
        self.main_frame = QWidget()

        # 设置提示框
        self.title = QLabel('Title')
        self.author = QLabel('Author')
        self.review = QLabel('Review')
        # 设置编辑器
        self.titleEdit = QLineEdit()
        self.authorEdit = QLineEdit()
        self.reviewEdit = QTextEdit()
        # 设置按钮
        self.button1 = QPushButton("开始查询1")
        self.button2 = QPushButton("开始查询2")
        self.button1.clicked.connect(lambda:self.test())
        self.button2.clicked.connect(self.test)

        grid = QGridLayout()
        # 设置间距
        grid.setSpacing(10)

        # grid.setRowStretch(0,1) == 将第0行拉伸一倍
        # grid.setColumnStretch(0,1) == 将第0列拉伸一倍
        # grid.addWidget(title, 1, 0) == title布置在第一行第一列
        # grid.addWidget(title, 3, 1, 5, 1) == title布置在第三行第一列，占据五行一列
        grid.addWidget(self.title, 1, 0)
        grid.addWidget(self.titleEdit, 1, 1)
        grid.addWidget(self.author, 2, 0)
        grid.addWidget(self.authorEdit, 2, 1)
        grid.addWidget(self.review, 3, 0)
        grid.addWidget(self.reviewEdit, 3, 1, 5, 1)
        grid.addWidget(self.button1,9,0,1,2)
        grid.addWidget(self.button2,10,0,1,2)
        # Qweight添加相关项目
        self.main_frame.setLayout(grid)

        self.main_frame.setStatusTip('主页面')
        return self.main_frame
    
    def test(self):
        print("1111")
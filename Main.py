import sys
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import *
import ChangeGsPage
import HomePage

# 创建一个类
class Ex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 提示栏初始信息
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("项目初始化")
        # 项目程序大小
        self.resize(400,600)
        # 项目屏幕居中显示
        self.center() 
        
        # 菜单栏相关
        #一级菜单栏
        menubar = self.menuBar()
        HomePageMenu = menubar.addAction('返回主页')
        settingMenu = menubar.addMenu('设置')
        changeGSMenu = menubar.addMenu('格式转换')
        option3Menu = menubar.addMenu('option3')
        #一级菜单栏事件绑定
        HomePageMenu.triggered.connect(self.toHomePage)

        #二级菜单栏
        # settingMenu 普通菜单栏
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)
        newAct = QAction('New', self)
        # ssettingMenu 勾选菜单栏
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')        # 用checkable选项创建一个能选中的菜单。
        viewStatAct.setChecked(True)        # 默认设置为选中状态
        viewStatAct.triggered.connect(self.toggleMenu)
        # settingMenu 添加菜单栏
        settingMenu.addAction(newAct)
        settingMenu.addMenu(impMenu)
        settingMenu.addAction(viewStatAct)
        
        # changeGSMenu 普通菜单栏
        tochangeGS =  QAction('切换到格式转化页面', self)
        tochangeGS.triggered.connect(self.toChangeGS)
        # changeGSMenu 添加菜单栏
        changeGSMenu.addAction(tochangeGS)

        # 功能页面
        self.toHomePage()

        # 设置标题 展示
        self.setWindowTitle('算价表')
        self.show()

    # 右键菜单
    def contextMenuEvent(self, event):
        print("##")
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()
        elif action == opnAct:
            print('打开就打开')
        elif action == newAct:
            print('新建就新建')
    
    # 项目居中函数
    def center(self):
        # 得到了主窗口大小
        qr = self.frameGeometry()
        # 获取显示器的分辨率,然后得到中间点的位置
        cp = QDesktopWidget().availableGeometry().center()
        # 然后把自己的窗口的中心点放到qr的中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    # 切换提示栏
    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide

    #切换changeGs界面
    def toChangeGS(self):
        self.setCentralWidget(ChangeGsPage.ChangeGsPage().ChangeGsPageUI())
    #回到主页面
    def toHomePage(self):
        self.setCentralWidget(HomePage.HomePage().HomePageUI())

app = QApplication(sys.argv)
demo1 = Ex()
sys.exit(app.exec_())

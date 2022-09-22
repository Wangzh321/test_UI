from PySide2 import QtCore
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QWidget, QMessageBox

from lib.baseDragButton import DraggableButton
from lib.share import Share


#主窗口
class MainWin(QMainWindow):

    def __init__(self):
        super(MainWin, self).__init__()
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('./static/UI/main2.ui')

        #设置默认页码
        self.ui.stackedWidget.setCurrentIndex(4)

        #切换界面
        self.ui.pushButton.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(0) or self.hideAllComponents())
        self.ui.pushButton_2.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(1) or self.hideAllComponents())
        self.ui.pushButton_3.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(2) or self.hideAllComponents())

        #总线事件绑定
        self.ui.pushButton_4.clicked.connect(self.openComponentWin)
        #创建可移动按钮
        self.hideAllComponents()
        self.creatcomponents()

        #self.close()

        # self.ui.pushButton_8.move(30, 20)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告', "系统将退出，是否确认?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def keyPressEvent(self, event):
        print("close")

    def openComponentWin(self):
       '''
       展示组件选择界面
       :return:
       '''
       Share.componentWin.ui.setWindowModality(QtCore.Qt.ApplicationModal)
       Share.componentWin.ui.show()

    def hideAllComponents(self):
        '''
        隐藏所有动态创建的组件
        :return:
        '''
        # 组件类型1
        self.ui.pushButton_8.hide()
        self.ui.pushButton_13.hide()
        self.ui.pushButton_11.hide()
        self.ui.pushButton_9.hide()
        self.ui.pushButton_10.hide()
        # 组件类型2
        self.ui.pushButton_5.hide()
        self.ui.pushButton_6.hide()
        self.ui.pushButton_7.hide()
        self.ui.pushButton_12.hide()
        self.ui.pushButton_14.hide()
    def creatcomponents(self):
        # 组件类型1
        self.ui.pushButton_8 = DraggableButton(QIcon("./static/images/cpu.png"),"1", self.ui)
        self.ui.pushButton_13 = DraggableButton(QIcon("./static/images/cpu.png"),"2", self.ui)
        # self.ui.pushButton_11 = DraggableButton("./static/images/cpu.png","组件1", self.ui)
        # self.ui.pushButton_9 = DraggableButton("./static/images/cpu.png","组件1", self.ui)
        # self.ui.pushButton_10 = DraggableButton("./static/images/cpu.png","组件1", self.ui)
        # # 组件类型2
        # self.ui.pushButton_5 = DraggableButton("./static/images/cpu.png","组件2", self.ui)
        # self.ui.pushButton_6 = DraggableButton("./static/images/cpu.png","组件2", self.ui)
        # self.ui.pushButton_7 = DraggableButton("./static/images/cpu.png","组件2", self.ui)
        # self.ui.pushButton_12 = DraggableButton("./static/images/cpu.png","组件2", self.ui)
        # self.ui.pushButton_14 = DraggableButton("./static/images/cpu.png","组件2", self.ui)


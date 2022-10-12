# 能拖动的按钮的基类
import time

from PyQt5.QtWidgets import QAbstractGraphicsShapeItem
from PySide2 import QtCore
from PySide2.QtCore import QPoint, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QPushButton
from lib.share import Share
from utils.operateJson import loadJsonFromFile


class DraggableButton(QPushButton):
    def __init__(self, icon,title, parent,type):
        super().__init__(icon,title, parent)

        self.setIconSize(QSize(100, 100))

        self.iniDragCor = [30, 20]
        # 初始位置和大小、名字
        self.move(150, 70)
        self.resize(120, 120)
        self.setObjectName(title)
        self.type=type
        self.setStyleSheet("border-style: dashed;border-width: 2px;border-color: #8B7355;")
        # 绑定点击事件
        # self.clicked.connect(self.openEditWin)

        # 隐藏
        self.hide()

    def mousePressEvent(self, e):
        # 左键按下
        if e.buttons() == QtCore.Qt.LeftButton:
            self.initDragLocation(e)
            # 右键按下
        elif e.buttons() == QtCore.Qt.RightButton:
            self.openDataWin()


    def mouseMoveEvent(self, e):
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]
        # pos=self.mapToParent(self.pos())
        # parentPos=self.mapToParent(Share.mainWin.frame_2.pos())
        # print("当前位置"+str(self.mapToParent(self.pos())))

        cor = QPoint(x, y)
        cor=self.mapToParent(cor)
        # if pos.x()<0 or pos.x()>Share.mainWin.width()+parentPos.x():
        #     print("x超出范围")
        #
        # if pos.y()<0 or pos.y()>Share.mainWin.height()+parentPos.y():
        #     print("y超出范围")
        self.move(cor)  # 需要maptoparent一下才可以的,否则只是相对位置。

    def mouseDoubleClickEvent(self, e):
        # 左键按下
        if e.buttons() == QtCore.Qt.LeftButton:
            self.openEditWin()
        if e.buttons() == QtCore.Qt.RightButton:
            self.deleteComponents(e)



    def openEditWin(self):
        '''
        打开属性编辑窗口
        :return:
        '''
        Share.editWin.ClearLastFill()
        Share.editWin.getComponentInfo(self.objectName(),self.type)
        Share.jsonFlie = loadJsonFromFile("./configuration/test.json")
        print( Share.jsonFlie)
        if  Share.jsonFlie and  Share.jsonFlie.get("component") and  Share.jsonFlie.get("component").get(self.objectName()):
            Share.editWin.loadCofig(Share.jsonFlie.get("component").get(self.objectName()))
        Share.editWin.ui.setWindowModality(QtCore.Qt.ApplicationModal)
        Share.editWin.ui.show()

    def openDataWin(self):
        '''
        打开数据监视窗口
        :return:
        '''
        Share.dataWin.ui.setWindowModality(QtCore.Qt.ApplicationModal)
        Share.dataWin.ui.show()

    def initDragLocation(self, e):
        '''
        左键按下 初始拖拽位置
        :param e:
        :return:
        '''
        self.iniDragCor[0] = e.x()
        self.iniDragCor[1] = e.y()

    def deleteComponents(self,e):
        '''
        删除组件
        :return:
        '''
        print(self.type)
        self.hide()


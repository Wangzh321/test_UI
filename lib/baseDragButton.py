# 能拖动的按钮的基类
import time

from PySide2 import QtCore
from PySide2.QtCore import QPoint, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QPushButton
from lib.share import Share


class DraggableButton(QPushButton):
    def __init__(self, icon,title, parent):
        super().__init__(icon,title, parent)

        self.setIconSize(QSize(100, 100))

        self.iniDragCor = [30, 20]
        # 初始位置和大小
        self.move(150, 70)
        self.resize(80, 80)
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

        cor = QPoint(x, y)
        self.move(self.mapToParent(cor))  # 需要maptoparent一下才可以的,否则只是相对位置。

    def mouseDoubleClickEvent(self, e):
        # 左键按下
        if e.buttons() == QtCore.Qt.LeftButton:
            self.openEditWin()


    def openEditWin(self):
        '''
        打开属性编辑窗口
        :return:
        '''
        Share.editWin.ui.setWindowModality(QtCore.Qt.ApplicationModal)
        Share.editWin.ui.show()

    def openDataWin(self):
        '''
        打开数据监视窗口
        :return:
        '''
        Share.dataWin.ui.show()

    def saveInfoToJson(self, info):
        '''
        保存json格式文件
        :param info:
        :return:
        '''
        # TODO 保存Json格式文件

    def initDragLocation(self, e):
        '''
        左键按下 初始拖拽位置
        :param e:
        :return:
        '''
        self.iniDragCor[0] = e.x()
        self.iniDragCor[1] = e.y()

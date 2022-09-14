#能拖动的按钮的基类
import time

from PySide2.QtCore import QPoint
from PySide2.QtWidgets import QPushButton
from lib.share import Share


class DraggableButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.iniDragCor = [30, 20]
        #初始位置和大小
        self.move(150,70)
        self.resize(150,150)
        #绑定点击事件
        #self.clicked.connect(self.openEditWin)

        #隐藏
        self.hide()

    def mousePressEvent(self, e):
        self.iniDragCor[0] = e.x()
        self.iniDragCor[1] = e.y()
        Share.editWin.ui.show()

    def mouseMoveEvent(self, e):
        Share.editWin.ui.hide()
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]

        cor = QPoint(x, y)
        self.move(self.mapToParent(cor))  # 需要maptoparent一下才可以的,否则只是相对位置。

    def openEditWin(self):
        '''
        打开属性编辑窗口
        :return:
        '''
        print("here")
        Share.editWin.ui.show()

    def saveInfoToJson(self,info):
        '''
        保存json格式文件
        :param info:
        :return:
        '''
        # TODO 保存Json格式文件





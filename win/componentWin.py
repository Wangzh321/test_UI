from PySide2.QtCore import QRect
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox, QPushButton

from lib.baseDragButton import DraggableButton
from lib.share import Share


# 组件选择窗口
class ComponentWin:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('./static/UI/component.ui')
        # 默认组件界面关闭
        self.ui.hide()

        # 选择组件
        self.ui.pushButton.clicked.connect(lambda :self.selectComponent(1))
        self.ui.pushButton_2.clicked.connect(lambda :self.selectComponent(2))
        self.ui.pushButton_3.clicked.connect(lambda :self.selectComponent(3))
        # self.ui.pushButton_8.clicked.connect(self.selectComponent)
        # self.ui.pushButton_7.clicked.connect(self.selectComponent)

    def selectComponent(self,clickButtonOrder):
        '''
        选择组件1
        :return:
        '''

        # 显示组件
        if(clickButtonOrder==1):
            Share.componentCount1 += 1
            button= DraggableButton(QIcon("./static/images/cpu.png"),"组件1-%d"%(Share.componentCount1), Share.mainWin.frame_2,1)
        elif(clickButtonOrder==2):
            Share.componentCount2+=1
            button = DraggableButton(QIcon("./static/images/road.png"), "组件2-%d" % (Share.componentCount2),Share.mainWin.frame_2, 2)
        elif(clickButtonOrder==3):
            Share.componentCount3+=1
            button = DraggableButton(QIcon("./static/images/road1.png"), "组件3-%d" % (Share.componentCount3),Share.mainWin.frame_2, 3)

        button.show()
        self.ui.hide()



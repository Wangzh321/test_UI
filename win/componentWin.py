from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox

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
        self.ui.pushButton.clicked.connect(self.selectComponent1)
        self.ui.pushButton_2.clicked.connect(self.selectComponent2)
        # self.ui.pushButton_3.clicked.connect(self.selectComponent)
        # self.ui.pushButton_8.clicked.connect(self.selectComponent)
        # self.ui.pushButton_7.clicked.connect(self.selectComponent)

    def selectComponent1(self):
        '''
        选择组件1
        :return:
        '''

        # 显示组件

        if (Share.componentCount1 == 0):
            Share.mainWin.pushButton_8.show()
        elif (Share.componentCount1 == 1):
            Share.mainWin.pushButton_13.show()
        elif (Share.componentCount1 == 2):
            Share.mainWin.pushButton_11.show()
        elif (Share.componentCount1 == 3):
            Share.mainWin.pushButton_9.show()
        elif (Share.componentCount1 == 4):
            Share.mainWin.pushButton_10.show()
        # 限制每类组件5个
        else:
            QMessageBox.information(
                self.ui,
                '提示',
                '每类组件最多5个！')
        Share.componentCount1 += 1
        # 关闭组件选择窗口
        self.ui.hide()

    def selectComponent2(self):
        '''
        选择组件2
        :return:
        '''
        # 显示组件
        if (Share.componentCount2 == 0):
            Share.mainWin.pushButton_5.show()
        elif (Share.componentCount2 == 1):
            Share.mainWin.pushButton_6.show()
        elif (Share.componentCount2 == 2):
            Share.mainWin.pushButton_7.show()
        elif (Share.componentCount2 == 3):
            Share.mainWin.pushButton_12.show()
        elif (Share.componentCount2 == 4):
            Share.mainWin.pushButton_14.show()
        # 限制每类组件5个
        else:
            QMessageBox.information(
                self.ui,
                '提示',
                '每类组件最多5个！')
        Share.componentCount2 += 1
        # 关闭组件选择窗口
        self.ui.hide()



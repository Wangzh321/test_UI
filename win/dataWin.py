#数据监视窗口
from PySide2.QtUiTools import QUiLoader


class DataWin:
    '''
    属性编辑窗口
    '''
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('./static/UI/data.ui')
        #默认组件界面关闭
        self.ui.hide()
        #绑定重置文本按钮
        self.ui.pushButton_2.clicked.connect(self.resetText)
        #绑定确定按钮
        self.ui.pushButton.clicked.connect(self.confirm)

    def resetText(self):
        '''
        重置文本框
        :return:
        '''
        self.ui.lineEdit.setText("重置文本成功")
        self.ui.lineEdit_2.setText("重置文本成功")
        self.ui.lineEdit_3.setText("重置文本成功")

    def confirm(self):
        '''
        确定按钮
        :return:
        '''
        # TODO 调用动态组件保存json文件的方法
        self.ui.hide()
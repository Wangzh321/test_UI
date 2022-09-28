from PySide2.QtUiTools import QUiLoader

#属性编辑窗口
from lib.share import Share
from utils.operateJson import saveFileByJson, loadJsonFromFile


class EditWin:
    '''
    属性编辑窗口
    '''
    def __init__(self):
        self.buttonName=''
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('./static/UI/edit.ui')
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
        self.ui.lineEdit_3.setText("重置文本成功")
        self.ui.lineEdit_4.setText("重置文本成功")
        self.ui.lineEdit_9.setText("重置文本成功")
        self.ui.lineEdit_10.setText("重置文本成功")
        self.ui.lineEdit_8.setText("重置文本成功")

    def confirm(self):
        '''
        确定按钮
        :return:
        '''
        componentConfigJson={
        self.buttonName: {
        "属性1":self.ui.lineEdit.text(),
        "属性2":self.ui.lineEdit_3.text(),
        "属性3": self.ui.lineEdit_4.text(),
        "属性4":self.ui.lineEdit_9.text(),
        "属性5": self.ui.lineEdit_10.text(),
        "属性6": self.ui.lineEdit_8.text(),
         }
         }
        Share.configJson.update(componentConfigJson)
        saveFileByJson(Share.configJson,"test.json")
        self.ui.hide()

    def loadCofig(self,configInfo):
        self.ui.lineEdit.setText(configInfo.get("属性1"))
        self.ui.lineEdit_3.setText(configInfo.get("属性2"))
        self.ui.lineEdit_4.setText(configInfo.get("属性3"))
        self.ui.lineEdit_9.setText(configInfo.get("属性4"))
        self.ui.lineEdit_10.setText(configInfo.get("属性5"))
        self.ui.lineEdit_8.setText(configInfo.get("属性6"))

    def setButtonName(self,name):
        self.buttonName=name

    def ClearLastFill(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_10.clear()
        self.ui.lineEdit_8.clear()


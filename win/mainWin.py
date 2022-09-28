from PySide2 import QtCore
from PySide2.QtCore import QSize, QCoreApplication, QMetaObject, QRect
from PySide2.QtGui import QIcon, Qt, QFont
from PySide2.QtWidgets import *

from lib.baseDragButton import DraggableButton
from lib.share import Share


#主窗口
class MainWin(QMainWindow):

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi()
    #     # 从文件中加载UI定义
    #
    #     # 从 UI 定义中动态 创建一个相应的窗口对象
    #     # 注意：里面的控件对象也成为窗口对象的属性了
    #     # 比如 self.button , self.textEdit
    #     self = QUiLoader().load('./static/UI/main2')
    #
    #     # 设置默认页码
        self.stackedWidget.setCurrentIndex(4)
    #
    #     # 切换界面
        self.pushButton.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(0) or self.hideAllComponents())
        self.pushButton_2.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(1) or self.hideAllComponents())
        self.pushButton_3.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(2) or self.hideAllComponents())

        #总线事件绑定
        self.pushButton_4.clicked.connect(self.openComponentWin)
        #创建可移动按钮
        self.hideAllComponents()
        self.creatcomponents()

        #self.close()

        # self.pushButton_8.move(30, 20)

    def setupUi(self):
        self.setObjectName(u"smartUI")
        self.resize(1078, 785)
        self.setMinimumSize(QSize(1078, 785))
        self.setMaximumSize(QSize(1078, 785))
        icon = QIcon()
        icon.addFile(u"static/images/s.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.action1 = QAction(self)
        self.action1.setObjectName(u"action1")
        self.action1.setCheckable(False)
        icon1 = QIcon()
        icon1.addFile(u"static/images/\u65b0\u5efa\u7a97\u53e3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action1.setIcon(icon1)
        self.action2 = QAction(self)
        self.action2.setObjectName(u"action2")
        icon2 = QIcon()
        icon2.addFile(u"static/images/\u5de5\u5177.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action2.setIcon(icon2)
        self.action3 = QAction(self)
        self.action3.setObjectName(u"action3")
        icon3 = QIcon()
        icon3.addFile(u"static/images/\u5de5\u5177(1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.action3.setIcon(icon3)
        self.action4 = QAction(self)
        self.action4.setObjectName(u"action4")
        icon4 = QIcon()
        icon4.addFile(u"static/images/\u76f4\u64ad\u95f4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action4.setIcon(icon4)
        self.action5 = QAction(self)
        self.action5.setObjectName(u"action5")
        icon5 = QIcon()
        icon5.addFile(u"static/images/\u6253\u5f00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action5.setIcon(icon5)
        self.action6 = QAction(self)
        self.action6.setObjectName(u"action6")
        icon6 = QIcon()
        icon6.addFile(u"static/images/\u4fdd\u5b58.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action6.setIcon(icon6)
        self.action7 = QAction(self)
        self.action7.setObjectName(u"action7")
        icon7 = QIcon()
        icon7.addFile(u"static/images/\u64a4\u9500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action7.setIcon(icon7)
        self.action8 = QAction(self)
        self.action8.setObjectName(u"action8")
        icon8 = QIcon()
        icon8.addFile(u"static/images/\u56de\u9000.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action8.setIcon(icon8)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 141, 691))
        self.frame.setStyleSheet(u"#frame{\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "border:1px solid rgb(149, 149, 149);\n"
                                 "border-radius:20px\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 10, 141, 51))
        font = QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"/*#frame QPushButton{\n"
                                      "border: 2px solid rgb(112, 112, 112);\n"
                                      "border-radius: 25px;\n"
                                      "}*/")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 80, 141, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"/*#frame QPushButton{\n"
                                        "border: 2px solid rgb(112, 112, 112);\n"
                                        "border-radius: 25px;\n"
                                        "}*/")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 150, 141, 51))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"/*#frame QPushButton{\n"
                                        "border: 2px solid rgb(112, 112, 112);\n"
                                        "border-radius: 25px;\n"
                                        "}*/")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(140, 0, 921, 691))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 0, 921, 691))
        self.frame_2.setStyleSheet(u"#frame_2{background-color:rgb(255, 255, 255);}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(460, 0, 20, 691))
        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(0, 0, 16, 21))
        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(0, 100, 16, 21))
        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(50, 90, 16, 21))
        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(60, 30, 16, 21))
        self.pushButton_13 = QPushButton(self.frame_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(10, 50, 16, 21))
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(30, 170, 93, 28))
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(40, 220, 93, 28))
        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(30, 260, 93, 28))
        self.pushButton_12 = QPushButton(self.frame_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(40, 300, 93, 28))
        self.pushButton_14 = QPushButton(self.frame_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(50, 340, 93, 28))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 0, 921, 681))
        self.frame_3.setStyleSheet(u"#frame_3{background-color:rgb(255, 255, 255);}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.plainTextEdit = QPlainTextEdit(self.frame_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(360, 280, 104, 87))
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.lineEdit_2 = QLineEdit(self.page_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(350, 230, 113, 21))
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.lineEdit = QLineEdit(self.page_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(370, 250, 113, 21))
        self.stackedWidget.addWidget(self.page_3)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(self)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.TopToolBarArea)
        self.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action5)
        self.menu.addAction(self.action6)
        self.menu_2.addAction(self.action2)
        self.menu_2.addAction(self.action3)
        self.menu_3.addAction(self.action4)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action7)
        self.menu_3.addAction(self.action8)
        self.toolBar.addAction(self.action1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action5)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action6)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action7)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action8)
        self.toolBar.addAction(self.action3)
        self.toolBar.addAction(self.action4)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()

        self.retranslateUi(self)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(self)
        # setupUi

    def retranslateUi(self, smartUI):
        smartUI.setWindowTitle(QCoreApplication.translate("smartUI", u"smartUI", None))
        self.action1.setText(QCoreApplication.translate("smartUI", u"\u65b0\u5efa", None))
        self.action1.setIconText(QCoreApplication.translate("smartUI", u"\u5de5\u5177", None))
        self.action2.setText(QCoreApplication.translate("smartUI", u"gongju", None))
        self.action3.setText(QCoreApplication.translate("smartUI", u"gongju", None))
        self.action4.setText(QCoreApplication.translate("smartUI", u"sadas", None))
        self.action5.setText(QCoreApplication.translate("smartUI", u"\u6253\u5f00", None))
        self.action6.setText(QCoreApplication.translate("smartUI", u"\u4fdd\u5b58", None))
        self.action7.setText(QCoreApplication.translate("smartUI", u"\u64a4\u9500", None))
        self.action8.setText(QCoreApplication.translate("smartUI", u"\u56de\u9000", None))
        self.pushButton.setText(QCoreApplication.translate("smartUI", u"platform", None))
        self.pushButton_2.setText(QCoreApplication.translate("smartUI", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("smartUI", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("smartUI", u"\u603b\u7ebf", None))
        self.pushButton_8.setText(QCoreApplication.translate("smartUI", u"\u7ec4\u4ef61", None))
        self.pushButton_9.setText(QCoreApplication.translate("smartUI", u"\u7ec4\u4ef61", None))
        self.pushButton_10.setText(QCoreApplication.translate("smartUI", u"\u7ec4\u4ef61", None))
        self.pushButton_11.setText(QCoreApplication.translate("smartUI", u"\u7ec4\u4ef61", None))
        self.pushButton_13.setText(QCoreApplication.translate("smartUI", u"\u7ec4\u4ef61", None))
        self.pushButton_5.setText(QCoreApplication.translate("smartUI", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("smartUI", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("smartUI", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("smartUI", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("smartUI", u"PushButton", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("smartUI", u"\u9875\u97622\n"
                                                                              "", None))
        self.lineEdit_2.setText(QCoreApplication.translate("smartUI", u"\u7a7a\u767d\u9875\u6d4b\u8bd5", None))
        self.lineEdit.setText(QCoreApplication.translate("smartUI", u"\u9875\u97623", None))
        self.menu.setTitle(QCoreApplication.translate("smartUI", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("smartUI", u"\u83dc\u5355", None))
        self.menu_3.setTitle(QCoreApplication.translate("smartUI", u"\u83dc\u5355", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("smartUI", u"toolBar", None))

    # retranslateUi

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
        self.pushButton_8.hide()
        self.pushButton_13.hide()
        self.pushButton_11.hide()
        self.pushButton_9.hide()
        self.pushButton_10.hide()
        # 组件类型2
        self.pushButton_5.hide()
        self.pushButton_6.hide()
        self.pushButton_7.hide()
        self.pushButton_12.hide()
        self.pushButton_14.hide()
    def creatcomponents(self):
        # 组件类型1
        self.pushButton_8 = DraggableButton(QIcon("./static/images/cpu.png"),"1", self,'组件1')
        self.pushButton_13 = DraggableButton(QIcon("./static/images/cpu.png"),"2", self,'组件2')
        # self.pushButton_11 = DraggableButton("./static/images/cpu.png","组件1", self)
        # self.pushButton_9 = DraggableButton("./static/images/cpu.png","组件1", self)
        # self.pushButton_10 = DraggableButton("./static/images/cpu.png","组件1", self)
        # # 组件类型2
        # self.pushButton_5 = DraggableButton("./static/images/cpu.png","组件2", self)
        # self.pushButton_6 = DraggableButton("./static/images/cpu.png","组件2", self)
        # self.pushButton_7 = DraggableButton("./static/images/cpu.png","组件2", self)
        # self.pushButton_12 = DraggableButton("./static/images/cpu.png","组件2", self)
        # self.pushButton_14 = DraggableButton("./static/images/cpu.png","组件2", self)
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告', "系统将退出，是否确认?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
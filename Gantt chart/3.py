
# 动态甘特图

import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from window import Ui_MainWindow as aui
import sys


#参数初始化，加以随时间推进的甘特图


def draw(path):
    execute_time = [50,60]
    trans_time = [10]

    # print(execute_time,trans_time)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots()
    ax.cla()

    x = ['PE_execute1', 'trans_1to2', 'PE_execute2']
    y = [execute_time[0], trans_time[0], execute_time[1]]
    y.reverse()
    x.reverse()
    Y=[]
    for i in range(0,len(y)):
        l = []
        for j in range(1,y[i]+1):
            l.append(j)
        Y.append(l)


    plt.xlabel("时间")
    plt.ylabel("进程")
    speed=0.2
    for i in range(2,-1,-1):#每一段

        for j in range(0,len(Y[i])):
            if i == 0:
                plt.barh(x[0], Y[i][j], color=(0, 0, 1), height=0.5, left=y[1] + y[2])
                plt.barh(x[1],0)
                plt.barh(x[2],0)
                plt.xlim([y[1]+y[2],y[0]+y[1]+y[2]])
                plt.pause(speed)
            elif i == 1:
                plt.barh(x[i], Y[i][j], color=(0, 0, 1), height=0.5, left=y[2])
                plt.barh(x[0], 0)
                plt.barh(x[2], 0)
                plt.xlim([y[2], y[1] + y[2]])
                plt.pause(speed)
            elif i == 2:
                plt.barh(x[0], 0)
                plt.barh(x[1], 0)
                plt.barh(x[i], Y[i][j], color=(0, 0, 1), height=0.5, left=0)
                plt.xlim([0,y[2]])
                plt.pause(speed)



        #plt.xlim([0 ,300])
        # plt.tick_params(axis='x',width=4)
        # plt.show()
        #plt.pause(1)


class AUi(QtWidgets.QMainWindow, aui):
    def __init__(self):
        super(AUi, self).__init__()
        self.setupUi(self)
    def pic(self):
        path =self.lineEdit.text()
        a.close()
        draw(path)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a=AUi( )
    a.show()

    a.pushButton.clicked.connect(a.pic)

    sys.exit(app.exec_())



#动态甘特图


#功能说明：参数文件未给定，但传参了，后续可加。自动输出动态甘特图




import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from window import Ui_MainWindow as aui
import sys

def draw(path):
    execute_time = []
    trans_time = []

    for i in range(100,-1,-1):
        execute_time.append([i,i])
        trans_time.append([101-i])
    #[100, 100],[0]

    #print(execute_time,trans_time)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots()
    for k in range(0, len(execute_time)):
        ax.cla()
        x = ['PE_execute1', 'trans_1to2', 'PE_execute2']
        y = [execute_time[k][0], trans_time[k][0], execute_time[k][1]]
        y.reverse()
        x.reverse()

        for i in range(0, 2 * len(execute_time) - 1):
            if i == 0:
                plt.barh(x[i], y[i], color=(0, 0, 1), height=0.5, left=y[1] + y[2])
            elif i == 1:
                plt.barh(x[i], y[i], color=(0, 0, 1), height=0.5, left=y[2])
            elif i == 2:
                plt.barh(x[i], y[i], color=(0, 0, 1), height=0.5, left=0)
        plt.xlabel("时间")
        plt.ylabel("进程")
        plt.xlim([0,300])
        #plt.tick_params(axis='x',width=4)
        #plt.show()
        plt.pause(1)


class AUi(QtWidgets.QMainWindow, aui):
    def __init__(self):
        super(AUi, self).__init__()
        self.setupUi(self)
    def pic(self):
        path=self.lineEdit.text()
        a.close()
        draw(path)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a=AUi()
    a.show()

    a.pushButton.clicked.connect(a.pic)

    sys.exit(app.exec_())
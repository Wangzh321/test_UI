from PySide2.QtWidgets import QApplication

from lib.share import Share
from win.componentWin import ComponentWin
from win.dataWin import DataWin
from win.editWin import EditWin
from win.mainWin import MainWin


if __name__ == '__main__':
    app = QApplication([])
    Share.mainWin = MainWin()
    Share.mainWin.ui.show()
    compomentWin = ComponentWin()

    Share.componentWin = compomentWin
    Share.editWin = EditWin()
    Share.dataWin = DataWin()

    app.exec_()
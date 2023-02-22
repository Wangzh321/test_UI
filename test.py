import sys

import PyQt5
from PyQt5.QtCore import Qt, QRect, QPointF, QRectF, pyqtSignal, QObject
from PyQt5.QtGui import QBrush, QPainter, QPen, QPolygonF, QColor, QFont
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsEllipseItem,
    QGraphicsItem,
    QGraphicsRectItem,
    QGraphicsPolygonItem,
    QGraphicsTextItem,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
    QGraphicsSceneHoverEvent,
    QGraphicsSceneMouseEvent
)

width = 800
height = 1000


class Bus(QGraphicsPolygonItem, QObject):
    state: int
    cx: float
    cy: float
    w: float
    w1: float
    l: float
    l1: float
    points = []
    polygon = []

    def __init__(self):
        super(Bus, self).__init__()
        self.polygon = QPolygonF()
        self.cx = width / 2
        self.cy = height / 2
        self.w = 50
        self.w1 = 100
        self.l = 350
        self.l1 = 250
        self.setAcceptHoverEvents(True)
        self.rect_top = QRectF(self.cx - 15, 135, 30, 30)
        self.rect_bottom = QRectF(self.cx - 15, 835, 30, 30)

    def bus_paint(self):
        self.points = [[self.cx - self.w, self.cy - self.l1], [self.cx - self.w1, self.cy - self.l1],
                       [self.cx, self.cy - self.l], [self.cx + self.w1, self.cy - self.l1],
                       [self.cx + self.w, self.cy - self.l1], [self.cx + self.w, self.cy + self.l1],
                       [self.cx + self.w1, self.cy + self.l1], [self.cx, self.cy + self.l],
                       [self.cx - self.w1, self.cy + self.l1], [self.cx - self.w, self.cy + self.l1]]
        self.polygon.clear()
        for i in range(10):
            self.polygon.append(QPointF(self.points[i][0], self.points[i][1]))
        self.setPolygon(self.polygon)

    def hoverMoveEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        pos: QPointF() = event.pos()
        if self.rect_top.contains(pos):
            self.setCursor(Qt.SizeVerCursor)
            self.state = 1
        elif self.rect_bottom.contains(pos):
            self.setCursor(Qt.SizeVerCursor)
            self.state = 2
        else:
            self.setCursor(Qt.ArrowCursor)
            self.state = 0

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton:
            pass

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.prepareGeometryChange()
        if self.state == 1:
            pos: QPointF = event.pos()
            x = self.points[2][1]
            for i in range(5):
                self.points[i][1] += (pos.y() - x)
            self.polygon.clear()
            for i in range(10):
                self.polygon.append(QPointF(self.points[i][0], self.points[i][1]))
            self.setPolygon(self.polygon)
        elif self.state == 2:
            pos: QPointF = event.pos()
            x = self.points[7][1]
            for i in range(5, 10):
                self.points[i][1] += (pos.y() - x)
            self.polygon.clear()
            for i in range(10):
                self.polygon.append(QPointF(self.points[i][0], self.points[i][1]))
            self.setPolygon(self.polygon)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.state == 1:
            pos: QPointF = event.pos()
            self.rect_top.setRect(self.cx - 15, pos.y() - 15, 30, 30)
        elif self.state == 2:
            pos: QPointF = event.pos()
            self.rect_bottom.setRect(self.cx - 15, pos.y() - 15, 30, 30)


class test(QWidget):
    pass


class PE(QGraphicsRectItem):

    def __init__(self, P: test, pos: QPointF()):
        super(PE, self).__init__()
        rect_m = QRectF(0, 0, 50, 50)
        self.setRect(rect_m)
        self.setPos(pos.x(), pos.y())
        self.bus = Bus()
        self.bus.setBrush(QColor("#54FF9F"))
        self.bus.w = 10
        self.bus.w1 = 20
        self.left = P.bus.cx - P.bus.w
        self.right = P.bus.cx + P.bus.w
        if pos.x() < self.left:
            self.bus.cx = (pos.x() + self.boundingRect().right() + self.left) / 2
            self.bus.cy = self.pos().y() + 25
            self.bus.l = (self.left - self.boundingRect().right() - pos.x()) / 2
            self.bus.l1 = self.bus.l - 20
            self.bus.bus_paint()
            self.bus.setTransformOriginPoint(self.bus.cx, self.bus.cy)
            self.bus.setRotation(90)
        elif pos.x() > (self.right):
            self.bus.cx = (pos.x() + self.right) / 2
            self.bus.cy = self.pos().y() + 25
            self.bus.l = (pos.x() - self.right) / 2
            self.bus.l1 = self.bus.l - 20
            self.bus.bus_paint()
            self.bus.setTransformOriginPoint(self.bus.cx, self.bus.cy)
            self.bus.setRotation(90)


    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton:
            pass

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        pos = event.scenePos()
        self.setPos(pos.x(), pos.y())

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        pos = event.scenePos()
        if pos.x() < self.left:
            self.bus.cx = (self.pos().x() + self.boundingRect().right() + self.left) / 2
            self.bus.cy = self.pos().y() + 25
            self.bus.l = (self.left - self.boundingRect().right() - self.pos().x()) / 2
            self.bus.l1 = self.bus.l - 20
            self.bus.bus_paint()
            self.bus.setTransformOriginPoint(self.bus.cx, self.bus.cy)
            self.bus.setRotation(90)
        elif pos.x() > (self.right):
            self.bus.cx = (self.pos().x() + self.right) / 2
            self.bus.cy = self.pos().y() + 25
            self.bus.l = (self.pos().x() - self.right) / 2
            self.bus.l1 = self.bus.l - 20
            self.bus.bus_paint()
            self.bus.setTransformOriginPoint(self.bus.cx, self.bus.cy)
            self.bus.setRotation(90)



class test(QWidget):
    bus: Bus()

    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(0, 0, width, height)
        self.bus = Bus()
        self.bus.setBrush(QColor("#98F5FF"))
        self.bus.bus_paint()
        text = QGraphicsTextItem("cross bus")
        text.setFont(QFont("宋体",20))
        text.setPos(QPointF(self.bus.cx - text.boundingRect().width() / 2, self.bus.cy - text.boundingRect().height() / 2))
        text.setTransformOriginPoint(text.boundingRect().width() / 2, text.boundingRect().height() / 2)
        text.setRotation(90)
        self.bus.childItems().append(text)
        self.scene.addItem(self.bus)
        self.scene.addItem(text)

        view = QGraphicsView(self.scene)
        view.setRenderHint(QPainter.Antialiasing)

        hbox = QHBoxLayout(self)
        hbox.addWidget(view)

        self.setLayout(hbox)

    def mousePressEvent(self, event) -> None:
        if event.buttons() == Qt.LeftButton:
            pos: QPointF() = event.pos()
            pe = PE(self, pos)
            self.scene.addItem(pe)
            self.scene.addItem(pe.bus)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = test()
    w.show()

    app.exec()

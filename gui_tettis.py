# -*- config: utf-8 -*-

import sys
import numpy as np
import random
from color_tetoris import my_color
import tetris
from PyQt5 import QtGui, QtWidgets, QtCore


class Mainwindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.scale = 30
        self.intrval = 500
        self.st = tetris.Stage()
        self.color = my_color()
        self.margin = (4, 4)
        self.init_windos('My Tetris')
        self.set_font()

    def set_font(self):
        self.font = QtGui.QFont('stencil', 30)

    def init_windos(self, title):
        self.setWindowTitle(title)
        self.setFixedSize(self.scale * (self.st.field[0] + 2 * self.margin[0]),
                          self.scale * (self.st.field[1] + 2 * self.margin[1]))
        self.timerId = self.startTimer(self.intrval)
        self.timerId_effect = self.startTimer(0.1*self.intrval)
        self.show()

    def paintEvent(self, event):
        '''
        Override paintEvent
        '''
        qp = QtGui.QPainter()
        # draw
        qp.begin(self)
        self.draw(event, qp)
        qp.end()

    def draw(self, event, qp):
        self.put_colored_block(qp)

    def put_colored_block(self, qp):
        for row in range(self.st.field[1]):
            for col in range(self.st.field[0]):
                color_num = int(self.st.board[row][col]) + 1
                self.draw_squar(qp, self.color.list[color_num], col, row)

    def timerEvent(self, event):
        '''
        Override timerEvent
        '''
        if event.timerId() == self.timerId:
            self.update()

    def keyPressEvent(self, event):
        key = event.key()

    def draw_squar(self, qp, color, col, row):
        x = self.scale * (col + self.margin[0])
        y = self.scale * (row + self.margin[1])
        unit = self.scale - 2
        qp.fillRect(x, y, unit, unit, color)

        qp.setPen(color.lighter())
        qp.drawLine(x, y, x + unit, y)
        qp.drawLine(x, y, x, y + unit)

        qp.setPen(color.darker(300))
        qp.drawLine(x + unit, y + unit, x + unit, y)
        qp.drawLine(x + unit, y + unit, x, y + unit)

    def draw_text(self, event, qp, text):
        qp.setPen(self.color.list[9])
        qp.setFont(self.font)
        self.text = text
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Mainwindow()
    painter = QtGui.QPainter()
    app.exec_()

if __name__ == '__main__':
    main()

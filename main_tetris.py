import sys
import numpy as np
import random
from gui_tettis import Mainwindow
import tetris
from PyQt5 import QtGui, QtWidgets, QtCore


class Mainwindow_tetoris(Mainwindow):
    def __init__(self):
        super().__init__()

        self.pause = True
        self.st.next_block = self.st.select_block(random.randint(0, 6))

    def timerEvent(self, event):
        '''
        Override timerEvent
        '''
        if self.pause is False and self.st.over is False:
            '''
            if flag_move is True, it means that a block is falling
            if flag_move is note , it means that a block just stops
            when the block stops, another block is generated.
            '''
            if event.timerId() == self.timerId:
                if self.st.flag_move is False:
                    self.st.moving_block = self.st.next_block
                    self.st.next_block = \
                        self.st.select_block(random.randint(0, 6))
                    self.st.init_posture()
                    self.st.flag_move = True

                if self.st.check_movable(self.st.moving_block,
                                         self.st.position,
                                         next_y=1) is True and \
                        self.st.flag_move is True:
                    self.st.position[1] += 1
                    self.st.move_block(self.st.position[0],
                                       self.st.position[1])
                else:
                    self.st.flag_move = False
                    self.st.over = self.st.judge_gameover()
                    self.st.save_board()
                    self.st.remove_lined_blocks()
                self.update()
        else:
            self.update()


    def keyPressEvent(self, event):
        key = event.key()
        can_move = False

        if key == QtCore.Qt.Key_P:
            self.pause = not(self.pause)
        if self.pause is False:
            if key == QtCore.Qt.Key_Left:
                if self.st.check_movable(self.st.moving_block,
                                         self.st.position, next_x=-1) is True:
                    self.st.position[0] -= 1
                    can_move = True
            elif key == QtCore.Qt.Key_Right:
                if self.st.check_movable(self.st.moving_block,
                                         self.st.position, next_x=1) is True:
                    self.st.position[0] += 1
                    can_move = True
            elif key == QtCore.Qt.Key_Down:
                if self.st.check_movable(self.st.moving_block,
                                         self.st.position, next_y=1) is True:
                    self.st.position[1] += 1
                    can_move = True
            elif key == QtCore.Qt.Key_W:
                if self.st.check_movable(self.st.moving_block,
                                         self.st.position, next_rot=1) is True:
                    self.st.rotation = 1
            elif key == QtCore.Qt.Key_E:
                if self.st.check_movable(self.st.moving_block,
                                         self.st.position, next_rot=1) is True:
                    self.st.rotation = 3


        if can_move is True:
            self.st.move_block(self.st.position[0], self.st.position[1])
            can_move = False
            self.update()

        if self.st.rotation != 0:
            self.st.moving_block = self.st.rotate(self.st.moving_block,
                                                  self.st.rotation)
            self.st.move_block(self.st.position[0], self.st.position[1])
            self.st.rotation = 0
            self.update()

    def draw(self, event, qp):
        self.put_colored_block(qp)
        self.next_block(qp)
        if self.st.over is True:
            self.draw_text(event, qp, u'gameover')
        elif self.pause is True:
            self.draw_text(event, qp, u'PAUSE')

    def next_block(self, qp):
        for row in range(4):
            for col in range(4):
                color_num = int(self.st.next_block[row][col]) + 1
                if self.st.next_block[row][col] > 0:
                    self.draw_squar(qp, self.color.list[color_num],
                                    col + 4, row - 4)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Mainwindow_tetoris()
    painter = QtGui.QPainter()
    app.exec_()

if __name__ == '__main__':
    main()

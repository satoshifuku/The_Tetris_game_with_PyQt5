# -*- config: utf-8 -*-

import sys
from PyQt5 import QtGui


class my_color(object):
    def __init__(self):
        self.list = []
        self.list.append(QtGui.QColor('gray'))
        self.list.append(QtGui.QColor(235, 235, 235))
        self.list.append(QtGui.QColor('Cyan'))
        self.list.append(QtGui.QColor('darkblue'))
        self.list.append(QtGui.QColor('darkred'))
        self.list.append(QtGui.QColor('Magenta'))
        self.list.append(QtGui.QColor('darkgreen'))
        self.list.append(QtGui.QColor('Yellow'))
        self.list.append(QtGui.QColor(250, 90, 30))
        self.list.append(QtGui.QColor('red'))

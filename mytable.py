from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys


class MyTable(QTableWidget):
    ITEMDOUBLECLICK = QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(MyTable, self).__init__(parent)
        
    def mouseDoubleClickEvent(self, ev):
        row = self.currentRow()
        item = self.item(row,0).text()
        self.ITEMDOUBLECLICK.emit(item)
        return super(MyTable, self).mouseDoubleClickEvent(ev)
        

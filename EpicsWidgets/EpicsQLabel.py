from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSlot, pyqtProperty
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


import numpy as np

from Auxillary.cs_epics import WrappedPV
from Constants.font_sizes import WIDGETS_SIZE


class EpicsFloatLabel(QLabel):
    def __init__(self, cname, count=1):
        super().__init__()
        self._suffix = ""
        self._decimal = 3

        self.val = 0.000

        self.setText(f'{float():.{self._decimal}f} {self._suffix}')
        self.setAlignment(Qt.AlignCenter)

        self.chan = WrappedPV(cname, count=count)
        self.chan.valueMeasured.connect(self.cs_update)

        self.setFont(QFont("Arial", WIDGETS_SIZE, QFont.Bold))
        self.setStyleSheet("""
                            QLabel {
                                color: black;
                                background-color: #ecf0f1;
                                padding: 5px 10px;
                                border-radius: 4px;
                                border: 1px solid #bdc3c7;
                                min-width: 80px;
                            }
                        """)
        self.setAlignment(Qt.AlignCenter)

    @pyqtSlot(str)
    def setSuffix(self, suffix):
        self._suffix = suffix
        self.setText(f'{self.val} {self._suffix}')

    def getSuffix(self):
        return self._suffix

    suffix = pyqtProperty(str, getSuffix, setSuffix)

    @pyqtSlot(int)
    def setDecimal(self, decimal):
        self._decimal = decimal
        self.setText(f'{float(self.val):.{self._decimal}f} {self._suffix}')

    def getDecimal(self):
        return self._decimal

    decimal = pyqtProperty(int, getDecimal, setDecimal)

    def cs_update(self, chan):
        self.val = round(float(chan.val), self._decimal)
        self.setText(f'{float(self.val):.{self._decimal}f} {self._suffix}')

    def make_disconnect(self):
        self.chan.dis()


class PoiEpicsFloatLabel(EpicsFloatLabel):
    def __init__(self, cname):
        super().__init__(cname, 10000)

    def cs_update(self, chan):
        # print(chan.val)
        val = np.mean(chan.val)
        self.val = round(float(val), self._decimal)
        self.setText(f'{float(self.val):.{self._decimal}f} {self._suffix}')


class EpicsIntLabel(QLabel):
    def __init__(self, cname):
        super().__init__()
        self.setText(f'{0}')
        self.setAlignment(Qt.AlignCenter)

        self.val = 0

        self.chan = WrappedPV(cname)
        self.chan.valueMeasured.connect(self.cs_update)

        self._suffix = ""

        self.setFont(QFont("Arial", 18, QFont.Bold))
        self.setStyleSheet("""
                                    QLabel {
                                        color: black;
                                        background-color: #ecf0f1;
                                        padding: 5px 10px;
                                        border-radius: 4px;
                                        border: 1px solid #bdc3c7;
                                        min-width: 80px;
                                    }
                                """)
        self.setAlignment(Qt.AlignCenter)

    @pyqtSlot(str)
    def setSuffix(self, suffix):
        self._suffix = suffix
        self.setText(f'{self.val} {self._suffix}')

    def getSuffix(self):
        return self._suffix

    suffix = pyqtProperty(str, getSuffix, setSuffix)

    def cs_update(self, chan):
        self.val = int(chan.val)
        self.setText(f'{self.val} {self._suffix}')

    def make_disconnect(self):
        self.chan.dis()

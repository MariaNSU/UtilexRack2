from PyQt5.QtCore import pyqtSignal, QObject
from epics import PV
from PyQt5.QtWidgets import QApplication
import numpy as np


class WrappedPV(QObject):
    valueMeasured = pyqtSignal(object)

    def __init__(self, cname, count=1, **kwargs):
        super().__init__()
        self.pv = PV(cname, callback=self.cs_update, count=count, auto_monitor=True)
        self.val = 0.0 if count==1 else np.zeros((count, ))
        self.name: str = cname
        self.size: int = count
        self.mlen = 0.0

    def cs_update(self, pvname, value, **kwargs):
        self.val = value
        self.mlen = kwargs.get('count', None)
        self.valueMeasured.emit(self)

    def set_value(self, val):
        self.pv.put(val)

    def __del__(self):
        self.pv.disconnect()

class POIWrappedPV(WrappedPV):
    def __init__(self, cname, count=1, **kwargs):
        super().__init__(cname, count=1, **kwargs)

    def cs_update(self, pvname, value, **kwargs):
        self.val = np.mean(value)
        self.mlen = kwargs.get('count', None)
        self.valueMeasured.emit(self)


if __name__ == "__main__":
    app = QApplication(['bpm_cross_section'])
    pv = WrappedPV('BI-LA5:PK7-fastAvY:Mea')
    app.exec()

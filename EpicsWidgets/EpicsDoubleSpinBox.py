from PyQt5.QtWidgets import QDoubleSpinBox
from PyQt5.QtGui import QFont

from Auxillary.cs_epics import WrappedPV


class EpicsDoubleSpinBox(QDoubleSpinBox):
    def __init__(self, cname, ps_restr):
        super().__init__()
        self.editingFinished.connect(self.ps_send)
        self.setMaximum(ps_restr[1])
        self.setMinimum(ps_restr[0])
        self.setSingleStep(0.1)
        self.setDecimals(2)

        self.setFont(QFont("Arial", 18))
        self.setStyleSheet("""
                    QDoubleSpinBox {
                        color: black;
                        background-color: #e8f8f5;
                        border: 2px solid #7dcea0;
                        border-radius: 4px;
                        padding: 5px;
                        min-width: 100px;
                    }
                    QDoubleSpinBox:hover {
                        border: 2px solid #52be80;
                    }
                """)

        self.chan = WrappedPV(cname)
        self.chan.valueMeasured.connect(self.cs_update)

    def cs_update(self, chan):
        v = chan.val
        if v is not None:
            if v != self.value():
                self.setValue(v)

    def ps_send(self):
        value = self.value()
        self.chan.set_value(value)

    def make_disconnect(self):
        self.chan.disconnect()
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtGui import QFont

from Auxillary.cs_epics import WrappedPV


class EpicsSpinBox(QSpinBox):
    def __init__(self, cname, ps_restr):
        super().__init__()
        self.editingFinished.connect(self.ps_send)
        self.setRange(ps_restr[0], ps_restr[1])
        self.setFont(QFont("Arial", 10))
        self.setStyleSheet("""
                    QSpinBox {
                        background-color: #e8f6f3;
                        border: 2px solid #76d7c4;
                        border-radius: 4px;
                        padding: 5px;
                        min-width: 100px;
                    }
                    QSpinBox:hover {
                        border: 2px solid #48c9b0;
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
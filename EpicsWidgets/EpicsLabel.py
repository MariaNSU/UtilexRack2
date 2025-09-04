from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Auxillary.cs_epics import WrappedPV
from Constants.font_sizes import WIDGETS_SIZE


class EpicsLabel(QLabel):
    def __init__(self, cname):
        super().__init__()
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

        self.chan = WrappedPV(cname)
        self.chan.valueMeasured.connect(self.cs_update)

    def cs_update(self, chan):
        v = chan.val
        if v is not None:
            if str(v) != self.text():
                self.setText(str(v))

    def make_disconnect(self):
        self.chan.disconnect()
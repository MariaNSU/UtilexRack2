from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtGui import QFont
from Holding.HoldingRegisterWidget import HoldingRegisterWidget


class IntHoldingWidget(HoldingRegisterWidget):
    def __init__(self, name, address, restr_ar=None, parent=None):
        super().__init__(name, address, "int16", parent)
        if restr_ar is None:
            restr_ar = [-1000, 1000]
        self.create_spinbox(restr_ar)

    def create_spinbox(self, restr_ar=None):
        if restr_ar is None:
            restr_ar = [-1000, 1000]

        self.spinbox = QSpinBox()
        self.spinbox.setRange(restr_ar[0], restr_ar[1])
        self.spinbox.setFont(QFont("Arial", 10))
        self.spinbox.setStyleSheet("""
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

        self.layout.addWidget(self.spinbox)

    def get_value(self):
        return self.spinbox.value() if self.spinbox else 0

    def set_value(self, value):
        if self.spinbox:
            self.spinbox.setValue(int(value))


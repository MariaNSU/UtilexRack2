from PyQt5.QtWidgets import QDoubleSpinBox
from PyQt5.QtGui import QFont
from Holding.HoldingRegisterWidget import HoldingRegisterWidget
from EpicsWidgets.EpicsDoubleSpinBox import EpicsDoubleSpinBox

class FloatHoldingWidget(HoldingRegisterWidget):
    def __init__(self, name, address, restr_ar=None, parent=None):
        super().__init__(name, address, "float", parent)
        if restr_ar is None:
            restr_ar = [-1000, 1000]
        self.create_double_spinbox(restr_ar)

    def create_double_spinbox(self, restr_ar=None):
        if restr_ar is None:
            restr_ar = [-1000, 1000]

        self.spinbox = EpicsDoubleSpinBox(self.name, restr_ar)


        self.layout.addWidget(self.spinbox)

    def get_value(self):
        return self.spinbox.value() if self.spinbox else 0.0

    def set_value(self, value):
        if self.spinbox:
            self.spinbox.setValue(float(value))
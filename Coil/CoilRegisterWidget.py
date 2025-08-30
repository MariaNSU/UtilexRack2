from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QFont
from Coil.CoilButton import CoilButton


class CoilRegisterWidget(QWidget):

    def __init__(self, name, address, parent=None):
        super().__init__(parent)
        self.name = name
        self.address = address

        self.setup_ui()

    def setup_ui(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 5, 10, 5)

        self.name_label = QLabel(self.name)
        self.name_label.setFont(QFont("Arial", 10))
        self.name_label.setStyleSheet("color: #2c3e50;")
        self.name_label.setMinimumWidth(200)

        self.info_label = QLabel(f"Адрес: {self.address} | Тип: bool")
        self.info_label.setFont(QFont("Arial", 8))
        self.info_label.setStyleSheet("color: #7f8c8d;")
        self.info_label.setFixedWidth(160)

        self.button = CoilButton()

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.info_label)
        self.layout.addStretch()
        self.layout.addWidget(self.button)

    def get_state(self):
        return self.button.isChecked() if self.button else False

    def set_state(self, state):
        if self.button:
            self.button.setChecked(state)
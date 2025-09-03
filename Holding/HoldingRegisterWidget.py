from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QFont


class HoldingRegisterWidget(QWidget):
    def __init__(self, base_name, description, address, data_type, parent=None):
        super().__init__(parent)
        self.base_name = base_name
        self.description = description
        self.address = address
        self.data_type = data_type
        self.spinbox = None

        self.setup_ui()

    def setup_ui(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 5, 10, 5)

        self.name_label = QLabel(self.description)
        self.name_label.setFont(QFont("Arial", 18))
        self.name_label.setStyleSheet("color: #2c3e50;")
        self.name_label.setFixedWidth(450)

        self.info_label = QLabel(f"Адрес: {self.address} | Тип: {self.data_type}")
        self.info_label.setFont(QFont("Arial", 16))
        self.info_label.setStyleSheet("color: #7f8c8d;")
        self.info_label.setFixedWidth(250)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.info_label)
        self.layout.addStretch()

    def get_value(self):
        pass

    def set_value(self, value):
        pass
55
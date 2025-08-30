from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QScrollArea, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Input.UpdateButton import UpdateButton
from Holding.SaveButton import SaveButton
class BaseHoldingTab(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.title = title
        self.registers = {}
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.title_label = QLabel(self.title)
        self.title_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("QScrollArea { border: none; }")

        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setSpacing(8)

        self.scroll.setWidget(self.container)

        self.update_button = UpdateButton()
        self.update_button.clicked.connect(self.on_update_data)

        self.save_button = SaveButton()
        self.save_button.clicked.connect(self.on_save_data)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.save_button)

        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.scroll)
        self.main_layout.addLayout(self.button_layout)

    def on_update_data(self):
        pass

    def on_save_data(self):
        pass

    def get_all_values(self):
        return {address: widget.get_value() for address, widget in self.registers.items()}

    def set_all_values(self, values_dict):
        for address, value in values_dict.items():
            if address in self.registers:
                self.registers[address].set_value(value)


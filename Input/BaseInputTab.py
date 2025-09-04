from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Input.IntInputRegisterWidget import IntInputRegisterWidget
from Input.FloatInputRegisterWidget import FloatInputRegisterWidget
from Constants.font_sizes import TITLE_LABEL_SIZE


class BaseInputTab(QWidget):

    def __init__(self, rack_name, title, parent=None):
        super().__init__(parent)
        self.title = title
        self.rack_name = rack_name
        self.registers = {}
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.title_label = QLabel(self.title)
        self.title_label.setFont(QFont("Arial", TITLE_LABEL_SIZE, QFont.Bold))
        self.title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("QScrollArea { border: none; }")

        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setSpacing(5)

        self.scroll.setWidget(self.container)

        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.scroll)

    def add_int_register(self, base_name, description, address, data_type):
        register_widget = IntInputRegisterWidget(base_name, description, address, data_type)
        self.registers[address] = register_widget
        self.container_layout.addWidget(register_widget)


    def add_float_register(self, base_name, description, address, data_type):
        register_widget = FloatInputRegisterWidget(base_name, description, address, data_type)
        self.registers[address] = register_widget
        self.container_layout.addWidget(register_widget)

    def update_register(self, address, value):
        if address in self.registers:
            self.registers[address].set_value(value)

    def renew_data(self):
        print("Base Tab Class!")
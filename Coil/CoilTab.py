from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Coil.CoilRegisterWidget import CoilRegisterWidget


class CoilTab(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.registers = {}
        self.setup_ui()
        self.create_coil_registers()

    def setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.title_label = QLabel("Coil Регистры")
        self.title_label.setFont(QFont("Arial", 16, QFont.Bold))
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

    def create_coil_registers(self):
        coil_registers = [
            ("Состояние кондиционера", 201)
        ]

        for name, address in coil_registers:
            self.add_register(name, address)

        if len(self.registers) == 1:
            self.container_layout.addStretch()

    def add_register(self, name, address):
        register_widget = CoilRegisterWidget(name, address)
        self.registers[address] = register_widget
        self.container_layout.addWidget(register_widget)


    def update_register(self, address, value):
        if address in self.registers:
            self.registers[address].set_state(bool(value))
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Coil.CoilRegisterWidget import CoilRegisterWidget
from Auxillary.json_parsing import get_config_by_type

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
        coil_registers = get_config_by_type('coil', 'Rack1')

        for register_info in coil_registers:
            base_name = register_info['base_name']
            description = register_info['description']
            address = register_info['address']
            self.add_register(base_name, description, address)

        if len(self.registers) == 1:
            self.container_layout.addStretch()

    def add_register(self, base_name, description, address):
        register_widget = CoilRegisterWidget(base_name, description, address)
        self.registers[address] = register_widget
        self.container_layout.addWidget(register_widget)


    def update_register(self, address, value):
        if address in self.registers:
            self.registers[address].set_state(bool(value))
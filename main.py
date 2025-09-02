import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTabWidget, QApplication)
from PyQt5.QtGui import QFont

from Coil.CoilTab import CoilTab
from Input.IntInputTab import IntInputTab
from Input.FloatInputTab import FloatInputTab
from Holding.IntHoldingTab import IntHoldingTab
from Holding.FloatHoldingTab import FloatHoldingTab

class UtilexMainWindow(QMainWindow):
    def __init__(self, rack_name):
        super().__init__()

        self.rack_name = rack_name

        self.setWindowTitle("Utilex Control Panel")
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.tab_widget = QTabWidget()
        self.tab_widget.setFont(QFont("Arial", 14, QFont.Bold))
        self.main_layout.addWidget(self.tab_widget)

        self.coil_tab = CoilTab(self.rack_name)
        self.tab_widget.addTab(self.coil_tab, "Coil Регистры")

        self.int_input_tab = IntInputTab(self.rack_name)
        self.tab_widget.addTab(self.int_input_tab, "Int Input Регистры")

        self.float_input_tab = FloatInputTab(self.rack_name)
        self.tab_widget.addTab(self.float_input_tab, "Float Input Регистры")

        self.holding_tab = IntHoldingTab(self.rack_name)
        self.tab_widget.addTab(self.holding_tab, "Int Holding Регистры")

        self.holding_tab = FloatHoldingTab(self.rack_name)
        self.tab_widget.addTab(self.holding_tab, "Float Holding Регистры")

    def load_test_data(self):
        self.int_input_tab.update_register(1, 1)
        self.int_input_tab.update_register(6, 1500)
        self.int_input_tab.update_register(15, 30)

        self.float_input_tab.update_register(2, 22.5)
        self.float_input_tab.update_register(4, 18.3)
        self.float_input_tab.update_register(7, 75.8)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #f0f0f0;
            }
            QTabWidget::pane {
                border: 1px solid #c0c0c0;
                background: white;
            }
            QTabBar::tab {
                background: #e0e0e0;
                color: #333333;
                padding: 8px 16px;
                margin: 2px;
                border-radius: 4px;
            }
            QTabBar::tab:selected {
                background: #4ca3e0;
                color: white;
            }
            QTabBar::tab:hover {
                background: #d0d0d0;
            }
        """)
    if len(sys.argv) > 1:
        rack_name = sys.argv[1]
    else:
        rack_name = "Rack1"
    window = UtilexMainWindow(rack_name)
    window.show()
    sys.exit(app.exec_())
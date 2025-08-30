from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont


class CoilButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__("ВЫКЛ", parent)
        self.setCheckable(True)
        self.setFixedSize(120, 40)
        self.setFont(QFont("Arial", 10, QFont.Bold))
        self.update_style()

        self.toggled.connect(self.update_style)
        self.toggled.connect(self.print_state)

    def update_style(self):
        if self.isChecked():
            self.setStyleSheet("""
                QPushButton {
                    background-color: #27ae60;
                    color: white;
                    border: 2px solid #219a52;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #2ecc71;
                }
            """)
            self.setText("ВКЛ")
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border: 2px solid #c0392b;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #ff6b6b;
                }
            """)
            self.setText("ВЫКЛ")

    def print_state(self):
        print("Coil button is", self.isChecked())

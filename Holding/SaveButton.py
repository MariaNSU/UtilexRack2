from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class SaveButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Сохранить все значения", parent)
        self.setup_style()

    def setup_style(self):
        self.setFont(QFont("Arial", 12, QFont.Bold))
        self.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet("""
                    QPushButton {
                        background-color: #27ae60;
                        color: white;
                        border: 2px solid #219a52;
                        border-radius: 8px;
                        padding: 10px 20px;
                        margin: 10px 15px;
                    }
                    QPushButton:hover {
                        background-color: #2ecc71;
                        border: 2px solid #27ae60;
                    }
                    QPushButton:pressed {
                        background-color: #219a52;
                    }
                """)


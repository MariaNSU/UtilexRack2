from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont


class UpdateButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__("Обновить данные для всех регистров!", parent)
        self.setup_style()

    def setup_style(self):
        self.setFont(QFont("Arial", 12, QFont.Bold))
        self.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: 2px solid #2980b9;
                border-radius: 8px;
                padding: 10px 20px;
                margin: 15px;
            }
            QPushButton:hover {
                background-color: #5dade2;
                border: 2px solid #3498db;
            }
            QPushButton:pressed {
                background-color: #2c81ba;
                border: 2px solid #2471a3;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
                border: 2px solid #95a5a6;
                color: #7f8c8d;
            }
        """)

        self.clicked.connect(self.on_click)

    def on_click(self):
        print("Need new data...")


class UpdateButtonAdvanced(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Обновить данные для всех регистров", parent)
        self.normal_text = "Обновить данные для всех регистров"
        self.loading_text = "Обновление..."
        self.is_loading = False

        self.setup_style()
        self.clicked.connect(self.start_loading)

    def setup_style(self):
        self.setFont(QFont("Arial", 12, QFont.Bold))
        self.setCursor(Qt.PointingHandCursor)

        self.update_style()

    def update_style(self):
        if self.is_loading:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #f39c12;
                    color: white;
                    border: 2px solid #e67e22;
                    border-radius: 8px;
                    padding: 10px 20px;
                    margin: 15px;
                }
            """)
            self.setText(self.loading_text)
            self.setEnabled(False)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: 2px solid #2980b9;
                    border-radius: 8px;
                    padding: 10px 20px;
                    margin: 15px;
                }
                QPushButton:hover {
                    background-color: #5dade2;
                    border: 2px solid #3498db;
                }
                QPushButton:pressed {
                    background-color: #2c81ba;
                    border: 2px solid #2471a3;
                }
            """)
            self.setText(self.normal_text)
            self.setEnabled(True)

    def start_loading(self):
        self.is_loading = True
        self.update_style()

        QTimer.singleShot(2000, self.stop_loading)

    def stop_loading(self):
        self.is_loading = False
        self.update_style()
        print("Данные успешно обновлены!")
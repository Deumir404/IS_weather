from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt


class ErrorDialog(QDialog):
    def __init__(self, error_message, parent=None):
        """
        Инициализация диалогового окна для отображения ошибок.

        :param error_message: Текст ошибки, который будет отображен.
        :param parent: Родительский виджет (опционально).
        """
        super().__init__(parent)
        self.setWindowTitle("Ошибка")
        self.setModal(True)
        self.setFixedSize(300, 150)

        # Основной макет
        layout = QVBoxLayout()

        # Сообщение об ошибке
        self.label = QLabel(error_message)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        # Кнопка "ОК"
        self.ok_button = QPushButton("ОК")
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Установка макета
        self.setLayout(layout)
        self.exec()



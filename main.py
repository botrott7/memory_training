from PyQt5.QtWidgets import (QApplication, QInputDialog, QLineEdit,
                             QWidget, QGridLayout, QPushButton, QMessageBox)
from PyQt5.QtCore import QTimer, Qt
import random
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_size = None  # Размер сетки не определен по умолчанию
        self.init_ui()

    def init_ui(self):
        size, ok = QInputDialog.getInt(self, 'Выбор размера', 'Введите размер таблицы (напр., 5 для 5x5):', 5, 2, 10)
        if ok:
            self.grid_size = size
        else:
            sys.exit()  # Выход, если не был выбран размер

        self.total_numbers = self.grid_size ** 2
        self.numbers = list(range(1, self.total_numbers + 1))
        random.shuffle(self.numbers)

        self.setWindowTitle('Таблица Шульте')

        self.grid = QGridLayout()
        self.inputs = []

        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                number = self.numbers[i * self.grid_size + j]
                line_edit = QLineEdit(str(number))
                line_edit.setReadOnly(True)  # Сделать поле только для чтения
                line_edit.setAlignment(Qt.AlignCenter)
                row.append(line_edit)
                self.grid.addWidget(line_edit, i, j)
            self.inputs.append(row)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.enable_editing)
        self.timer.start(30000)  # 30 секунд на запоминание

        self.check_button = QPushButton('Проверить', self)
        self.check_button.clicked.connect(self.check_results)
        self.check_button.setEnabled(False)  # Кнопка не будет доступна до завершения времени
        self.grid.addWidget(self.check_button, self.grid_size, 0, 1, self.grid_size)  # Разместить кнопку под сеткой

        self.setLayout(self.grid)
        self.show()

    def enable_editing(self):
        for row in self.inputs:
            for line_edit in row:
                line_edit.setReadOnly(False)  # Разрешить редактирование
                line_edit.setText('')  # Очистить поле
        self.check_button.setEnabled(True)

    def check_results(self):
        correct = 0
        for i, row in enumerate(self.inputs):
            for j, line_edit in enumerate(row):
                number = int(line_edit.text())
                if number == self.numbers[i * self.grid_size + j]:
                    correct += 1

        if correct == self.total_numbers:
            QMessageBox.information(self, 'Результат', 'Поздравляем! Вы правильно запомнили все числа.')
        else:
            QMessageBox.warning(self, 'Результат', 'К сожалению, есть ошибки. Попробуйте ещё раз.')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())
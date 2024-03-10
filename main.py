import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from functools import partial

from modules.SchulteTable import Schulte


class MemoryTrainingAppSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Выберите приложение для тренировки памяти')
        self.setGeometry(100, 100, 400, 300)

        grid_button = QPushButton('Сетка чисел для запоминания', self)
        grid_button.clicked.connect(self.open_grid_numbers_app)
        grid_button.setGeometry(100, 50, 200, 30)

        test2_button = QPushButton('Тест 2', self)
        test2_button.clicked.connect(partial(self.open_test_app, 'Тест 2'))
        test2_button.setGeometry(100, 100, 200, 30)

        test3_button = QPushButton('Тест 3', self)
        test3_button.clicked.connect(partial(self.open_test_app, 'Тест 3'))
        test3_button.setGeometry(100, 150, 200, 30)

        test4_button = QPushButton('Тест 4', self)
        test4_button.clicked.connect(partial(self.open_test_app, 'Тест 4'))
        test4_button.setGeometry(100, 200, 200, 30)

        self.show()

    def open_grid_numbers_app(self):
        try:
            self.hide()
            self.Schulte = Schulte(self)
            self.Schulte.show()
        except Exception as e:
            print("Ошибка при запуске приложения:", e)

    def open_test_app(self, test_name):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    selector = MemoryTrainingAppSelector()
    ex = MemoryTrainingAppSelector()
    try:
        sys.exit(app.exec_())
    except Exception as e:
        print("Unhandled exception:", e)

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
        test2_button.clicked.connect(partial(self.open_test_app1, 'Тест 2'))
        test2_button.setGeometry(100, 100, 200, 30)

        test3_button = QPushButton('Тест 3', self)
        test3_button.clicked.connect(partial(self.open_test_app2, 'Тест 3'))
        test3_button.setGeometry(100, 150, 200, 30)

        test4_button = QPushButton('Тест 4', self)
        test4_button.clicked.connect(partial(self.open_test_app3, 'Тест 4'))
        test4_button.setGeometry(100, 200, 200, 30)

        self.show()

    def open_grid_numbers_app(self):
        self.hide()
        self.device_availability_window = Schulte(self)
        self.device_availability_window.show()

    def open_test_app1(self, test_name):
        pass

    def open_test_app2(self, test_name):
        pass

    def open_test_app3(self, test_name):
        pass

    def closeEvent(self, event):
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # QFontDatabase.addApplicationFont("fonts/Montserrat-Regular.ttf")
    ex = MemoryTrainingAppSelector()
    try:
        sys.exit(app.exec_())
    except Exception as e:
        print("Unhandled exception:", e)

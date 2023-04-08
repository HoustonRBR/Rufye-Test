from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QFont

class RufieTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест Руф'є")
        self.setGeometry(100, 100, 900, 675)
        
        self.name_label = QLabel('Введіть П.І.Б:', self)
        self.name_label.move(50, 50)
        self.name_input = QLineEdit(self)
        self.name_input.move(200, 50)
        
        self.age_label = QLabel('Повних років:', self)
        self.age_label.move(50, 100)
        self.age_input = QLineEdit(self)
        self.age_input.move(200, 100)
        
        self.first_test_label = QLabel('Лягте на спину, заміряйте пульс на 15 секунд. Натисніть кнопку "Почати перший тест", щоб запустити таймер', self)
        self.first_test_label.setGeometry(50, 150, 1000, 32)
        self.start_first_test_button = QPushButton('Почати перший тест', self)
        self.start_first_test_button.setGeometry(50, 200, 200, 32)
        self.first_test_input = QLineEdit(self)
        self.first_test_input.move(300, 200)
        
        self.second_test_label = QLabel('Виконайте 30 присідань', self)
        self.second_test_label.setGeometry(50, 250, 1000, 32)
        self.start_second_test_button = QPushButton('Почати робити присідання', self)
        self.start_second_test_button.setGeometry(50, 300, 220, 32)
        
        self.third_test_label = QLabel('Лягти на спину', self)
        self.third_test_label.setGeometry(50, 350, 900, 32)
        self.start_third_test_button = QPushButton('Почати фінальний тест', self)
        self.start_third_test_button.setGeometry(50, 400, 200, 32)
        self.third_test_input1 = QLineEdit(self)
        self.third_test_input1.move(50, 450)
        self.third_test_input2 = QLineEdit(self)
        self.third_test_input2.move(50, 500)
        
        self.send_result_button = QPushButton('Надіслати результат', self)
        self.send_result_button.setGeometry(370, 600, 190, 32)
        
        self.time_label = QLabel('00:00:15', self)
        self.time_label.move(700, 300)

app = QApplication([])
ruf = RufieTest()
ruf.show()
app.exec_()
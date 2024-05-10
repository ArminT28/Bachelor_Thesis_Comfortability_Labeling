import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from functools import partial
from datetime import datetime
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.last_pressed_button = None
        self.recording = False
        self.recorded_data = {}

    def initUI(self):
        self.setWindowTitle('Button Logger')
        self.setGeometry(100, 100, 1000, 500)

        layout = QVBoxLayout()

        self.start_recording_button = QPushButton(f'Start Recording', self)
        self.start_recording_button.setStyleSheet("background-color: purple;height: 50px")
        self.start_recording_button.clicked.connect(partial(self.start_recording, self.start_recording_button))
        layout.addWidget(self.start_recording_button)

        self.excellent_button = QPushButton(f'Excellent', self)
        self.excellent_button.setStyleSheet("height: 50px")
        self.excellent_button.clicked.connect(partial(self.log_text, self.excellent_button))
        layout.addWidget(self.excellent_button)

        self.acceptable_button = QPushButton(f'Acceptable', self)
        self.acceptable_button.setStyleSheet("height: 50px")
        self.acceptable_button.clicked.connect(partial(self.log_text, self.acceptable_button))
        layout.addWidget(self.acceptable_button)

        self.so_and_so_button = QPushButton(f'So and So', self)
        self.so_and_so_button.setStyleSheet("height: 50px")
        self.so_and_so_button.clicked.connect(partial(self.log_text, self.so_and_so_button))
        layout.addWidget(self.so_and_so_button)

        self.uncomfortable_button = QPushButton(f'Uncomfortable', self)
        self.uncomfortable_button.setStyleSheet("height: 50px")
        self.uncomfortable_button.clicked.connect(partial(self.log_text, self.uncomfortable_button))
        layout.addWidget(self.uncomfortable_button)

        self.no_attention_button = QPushButton(f'Not paying attention', self)
        self.no_attention_button.setStyleSheet("height: 50px")
        self.no_attention_button.clicked.connect(partial(self.log_text, self.no_attention_button))
        layout.addWidget(self.no_attention_button)

        self.stop_recording_button = QPushButton(f'Stop Recording', self)
        self.stop_recording_button.setStyleSheet("background-color: purple;height: 50px")
        self.stop_recording_button.clicked.connect(partial(self.stop_recording, self.stop_recording_button))
        layout.addWidget(self.stop_recording_button)

        self.save_data_button = QPushButton(f'Save Data', self)
        self.save_data_button.setStyleSheet("background-color: green;height: 50px")
        self.save_data_button.clicked.connect(partial(self.save_data, self.save_data_button))
        layout.addWidget(self.save_data_button)

        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.log_text(self.excellent_button)
        elif event.key() == Qt.Key_2:
            self.log_text(self.acceptable_button)
        elif event.key() == Qt.Key_3:
            self.log_text(self.so_and_so_button)
        elif event.key() == Qt.Key_4:
            self.log_text(self.uncomfortable_button)
        elif event.key() == Qt.Key_5:
            self.log_text(self.no_attention_button)

    def log_text(self, button):
        if self.recording:
            current_datetime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S.%f')
            self.recorded_data[current_datetime] = button.text()
        if self.last_pressed_button:
            self.last_pressed_button.setStyleSheet("height: 50px")
        if button.text() == "Excellent":
            button.setStyleSheet("background-color: green;height: 50px")
        elif button.text() == "Acceptable":
            button.setStyleSheet("background-color: yellow;height: 50px")
        elif button.text() == "So and So":
            button.setStyleSheet("background-color: orange;height: 50px")
        elif button.text() == "Uncomfortable":
            button.setStyleSheet("background-color: red;height: 50px")
        elif button.text() == "Not paying attention":
            button.setStyleSheet("background-color: red;height: 50px")
        else:
            button.setStyleSheet("background-color: purple;height: 50px")
        self.last_pressed_button = button
        print(f'Button {button.text()} pressed.')

    def start_recording(self, button):
        if self.recording:
            print("Already recording")
            return
        print("Started recording")
        self.recording = True

    def stop_recording(self, button):
        if not self.recording:
            print("Not recording")
            return
        print("Stopped recording")
        self.recording = False

    def save_data(self, button):
        if not self.recording:
            with open('Labeled_Data/CJ77TAL 2024-05-10 16-44.CSV', 'w') as file:
                file.write('Timestamp,Label\n')
                for key, value in self.recorded_data.items():
                    file.write(f'{key},{value}\n')
            print('Data saved to file')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

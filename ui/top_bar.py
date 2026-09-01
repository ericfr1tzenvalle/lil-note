from PySide6.QtWidgets import QWidget, QGridLayout,QLabel, QPushButton
from PySide6.QtCore import QDateTime, QTimer, Qt

class TopBar(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout(self)
        self.label = QLabel('lilnote')
        self.label.setObjectName('label-lilnote')
        self.date = QDateTime().currentDateTime().toString('dd-mm-yyyy hh:mm:ss')
        self.data_label = QLabel(self.date)
        self.data_label.setObjectName('label-data')
        self.theme_button = QPushButton("☼")
        self.theme_button.setObjectName("theme_button")
        self.theme_button.setFixedSize(32,32)
        self.main_layout.addWidget(self.theme_button, 0, 0, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.label, 0, 1, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.data_label, 0, 2, alignment=Qt.AlignRight)

        self.main_layout.setColumnStretch(0,1)
        self.main_layout.setColumnStretch(1,1)
        self.main_layout.setColumnStretch(2,1)

        self.timer_date = QTimer(self)
        self.timer_date.timeout.connect(self.update_date)
        self.timer_date.start(1000) 

    def update_date(self):
        self.date = QDateTime().currentDateTime().toString('dd-mm-yyyy hh:mm:ss')
        self.data_label.setText(self.date)

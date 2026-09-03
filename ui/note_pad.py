from PySide6.QtWidgets import QVBoxLayout,QWidget, QPlainTextEdit
from ui.top_bar import TopBar
class NotePad(QWidget):

    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.note_pad = QPlainTextEdit()
        self.top_bar = TopBar()
        self.main_layout.setContentsMargins(8, 3, 8, 10)
        self.main_layout.addWidget(self.top_bar)
        self.main_layout.addWidget(self.note_pad)

    

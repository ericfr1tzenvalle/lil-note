from pathlib import Path

from PySide6.QtWidgets import QHBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

ICONS_DIR = Path(__file__).resolve().parent.parent / "assets" / "icons"
FILE_TEXT_ICON_FOR_DARK_THEME = ICONS_DIR / "file-text.svg"
FILE_TEXT_ICON_FOR_LIGHT_THEME = ICONS_DIR / "file-text-dark.svg"


class StatusBar(QWidget):
    def __init__(self, file_path=None, parent=None):
        super().__init__(parent)
        self.setObjectName("status_bar")
        self.status_layout = QHBoxLayout(self)

        filename = Path(file_path).stem if file_path else "untitled.txt"
        self.filename_label = QLabel(filename)
        self.file_icon_label = QLabel()
        self.status_layout.setContentsMargins(8, 0, 8, 6)
       
        self.status_layout.addWidget(self.file_icon_label, alignment=Qt.AlignLeft)
        self.status_layout.addWidget(self.filename_label, alignment=Qt.AlignLeft)

        self.set_theme(is_dark_theme=True)

    def set_file(self, file_path=None):
        filename = Path(file_path).stem if file_path else "untitled.txt"
        self.filename_label.setText(filename)

    def set_theme(self, is_dark_theme):
        icon_path = FILE_TEXT_ICON_FOR_DARK_THEME if is_dark_theme else FILE_TEXT_ICON_FOR_LIGHT_THEME
        self.file_icon_label.setPixmap(QIcon(str(icon_path)).pixmap(12, 12))

        



        

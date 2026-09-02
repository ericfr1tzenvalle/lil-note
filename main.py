import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from styles.theme import DARK_THEME, LIGHT_THEME

app = QApplication(sys.argv)
app.setStyleSheet(DARK_THEME)
window = MainWindow()

dark_mode = True


def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    app.setStyleSheet(DARK_THEME if dark_mode else LIGHT_THEME)
    window.note.top_bar.theme_button.setText("☼" if dark_mode else "☾")
    window.status_bar.set_theme(dark_mode)


window.note.top_bar.theme_button.clicked.connect(toggle_theme)

window.show()
sys.exit(app.exec())

from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from ui.note_pad import NotePad
from PySide6.QtGui import QAction
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent
DIR = PATH / 'notes'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("lilnote")
        self.resize(600, 400)
        self.note = NotePad()
        self.setCentralWidget(self.note)
        self.current_file = None
        DIR.mkdir(parents=True, exist_ok=True)

        # actions/hotkeys   
        self.new_note_action = QAction("New Note", self)
        self.open_note_action = QAction("Open Note", self)
        self.save_note_action = QAction("Save Note", self)
        self.save_as_note_action = QAction("Save Note As", self)
        self.help_action = QAction("Help", self)

        self.new_note_action.setShortcut("Ctrl+N")
        self.new_note_action.triggered.connect(self.new_file)
        self.open_note_action.setShortcut("Ctrl+O")
        self.open_note_action.triggered.connect(self.open_file)
        self.save_note_action.setShortcut("Ctrl+S")
        self.save_note_action.triggered.connect(self.save_file)
        self.save_as_note_action.setShortcut("Ctrl+Shift+S")
        self.save_as_note_action.triggered.connect(self.save_file_as)
        self.help_action.setShortcut("Ctrl+H")
        self.help_action.triggered.connect(self.show_help)

        self.addActions([self.new_note_action, self.open_note_action, self.save_note_action, self.save_as_note_action, self.help_action])


    def get_note_content(self):
        return self.note.note_pad.toPlainText()

    def set_current_file(self, file_path):
        self.current_file = Path(file_path)
        self.setWindowTitle(f"lilnote - {self.current_file.stem}")

    def save_to_file(self, file_path):
        try:
            Path(file_path).write_text(self.get_note_content(), encoding="utf-8")
        except OSError as error:
            QMessageBox.critical(self, "Save Error", f"Could not save the note.\n{error}")
            return False

        self.set_current_file(file_path)
        return True

    def new_file(self):
        message = QMessageBox.question(self, "New Note", "Are you sure you want to create a new note? Unsaved changes will be lost.", QMessageBox.Yes | QMessageBox.No)
        if message == QMessageBox.Yes:
            self.note.note_pad.clear()
            self.current_file = None
            self.setWindowTitle("lilnote")

    def save_file(self):
        content = self.get_note_content()
        if not content.strip():
            QMessageBox.warning(self, "Empty Note", "Cannot save an empty note.")
            return

        if self.current_file is None:
            self.save_file_as()
            return

        if self.save_to_file(self.current_file):
            QMessageBox.information(self, "Note Saved", f"Note saved to {self.current_file}")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Note", str(DIR), "Text Files (*.txt);;All Files (*)")
        if not file_path:
            return

        try:
            content = Path(file_path).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            QMessageBox.critical(self, "Open Error", f"Could not open the note.\n{error}")
            return

        self.note.note_pad.setPlainText(content)
        self.set_current_file(file_path)

    def save_file_as(self):
        content = self.get_note_content()
        if not content.strip():
            QMessageBox.warning(self, "Empty Note", "Cannot save an empty note.")
            return

        default_path = str(DIR / "untitled.txt")
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Note As", default_path, "Text Files (*.txt);;All Files (*)")
        if not file_path:
            return

        path = Path(file_path)

        if self.save_to_file(path):
            QMessageBox.information(self, "Note Saved", f"Note saved to {path}")

    def closeEvent(self, event):
        message = QMessageBox.question(self, "Quit", "Are you sure you want to quit? Unsaved changes will be lost.", QMessageBox.Yes | QMessageBox.No)
        if message == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def show_help(self):
        help_text = (
            "<lilnote help>\n\n"
            "Hotkeys:\n"
            "Ctrl+N: New Note\n"
            "Ctrl+O: Open Note\n"
            "Ctrl+S: Save Note\n"
            "Ctrl+Shift+S: Save Note As\n"
            "Ctrl+H: Show Help\n\n"
            "Use the buttons in the top bar to toggle themes."
        )
        QMessageBox.information(self, "Help", help_text)

    


import sys

from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from ui.note_pad import NotePad
from PySide6.QtGui import QAction
from pathlib import Path

from ui.status_bar import StatusBar

PATH = Path(__file__).resolve().parent.parent
DIR = PATH / 'notes'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("lilnote")
        self.resize(800, 600)
        self.note = NotePad()
        self.setCentralWidget(self.note)
        self.current_file = None
        DIR.mkdir(parents=True, exist_ok=True)

        self.last_content = self.get_note_content()
        self.note.note_pad.textChanged.connect(self.on_content_changed)
       
        self.statusBar().setContentsMargins(0, 0, 0, 0)
        self.statusBar().layout().setContentsMargins(0, 0, 0, 0)

        self.status_bar = StatusBar(self.current_file)
        self.statusBar().addWidget(self.status_bar)

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
        self.help_shortcut = "Ctrl+Shift+H" if sys.platform == "darwin" else "Ctrl+H"
        self.help_action.setShortcut(self.help_shortcut)
        self.help_action.triggered.connect(self.show_help)

        self.addActions([self.new_note_action, self.open_note_action, self.save_note_action, self.save_as_note_action, self.help_action])

    def on_content_changed(self):
        content_now = self.get_note_content()
        is_modified = content_now != self.last_content
        filename = self.current_file.stem if self.current_file else 'untitled.txt'
        status = '●' if is_modified else ''

        self.status_bar.filename_label.setText(f'{status} {filename}')

    def get_note_content(self):
        return self.note.note_pad.toPlainText()

    def set_current_file(self, file_path):
        self.current_file = Path(file_path)
        self.setWindowTitle(f"lilnote - {self.current_file.stem}")
        self.status_bar.set_file(self.current_file)

    def mark_as_saved(self):
        self.last_content = self.get_note_content()
        self.on_content_changed()

    def save_to_file(self, file_path):
        try:
            Path(file_path).write_text(self.get_note_content(), encoding="utf-8")
        except OSError as error:
            QMessageBox.critical(self, "Save Error", f"Could not save the note.\n{error}")
            return False

        self.set_current_file(file_path)
        self.mark_as_saved()
        return True

    def new_file(self):
        if not self.confirm_save_changes("creating a new note"):
            return

        self.note.note_pad.clear()
        self.current_file = None
        self.setWindowTitle("lilnote - untitled.txt")
        self.status_bar.set_file()
        self.mark_as_saved()

    def has_unsaved_changes(self):
        return self.get_note_content() != self.last_content

    def confirm_save_changes(self, action):
        if not self.has_unsaved_changes():
            return True

        message = QMessageBox.warning(
            self,
            "Unsaved Changes",
            f"Do you want to save your changes before {action}?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
            QMessageBox.Save,
        )

        if message == QMessageBox.Save:
            return self.save_file()

        return message == QMessageBox.Discard
    
    def save_file(self):
        content = self.get_note_content()
        if not content.strip():
            QMessageBox.warning(self, "Empty Note", "Cannot save an empty note.")
            return False

        if self.current_file is None:
            return self.save_file_as()

        if self.save_to_file(self.current_file):
            QMessageBox.information(self, "Note Saved", f"Note saved to {self.current_file}")
            return True

        return False

    def open_file(self):
        if not self.confirm_save_changes("opening another note"):
            return

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
        self.mark_as_saved()

    def save_file_as(self):
        content = self.get_note_content()
        if not content.strip():
            QMessageBox.warning(self, "Empty Note", "Cannot save an empty note.")
            return False

        default_path = str(DIR / "untitled.txt")
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Note As", default_path, "Text Files (*.txt);;All Files (*)")
        if not file_path:
            return False

        path = Path(file_path)

        if self.save_to_file(path):
            QMessageBox.information(self, "Note Saved", f"Note saved to {path}")
            return True

        return False

    def closeEvent(self, event):
        if self.confirm_save_changes("quitting"):
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
            f"{self.help_shortcut}: Show Help\n\n"
            "Use the buttons in the top bar to toggle themes."
        )
        QMessageBox.information(self, "Help", help_text)

    

import sys

if sys.platform == "darwin":
    FONT_FAMILY = "Menlo"
    SYMBOL_FONT_FAMILY = "Apple Symbols"
elif sys.platform == "win32":
    FONT_FAMILY = "Consolas"
    SYMBOL_FONT_FAMILY = "Segoe UI Symbol"
else:
    FONT_FAMILY = "DejaVu Sans Mono"
    SYMBOL_FONT_FAMILY = "Sans Serif"

DARK_THEME = f"""
QMainWindow {{ background-color: #121212; }}
QInputDialog, QMessageBox {{ background-color: #1d1d1d; color: #f0f0f0; }}
QInputDialog QLabel, QMessageBox QLabel {{ color: #f0f0f0; }}
QLineEdit {{ background-color: #121212; color: #f0f0f0; border: 1px solid #3a3a3a; border-radius: 6px; padding: 7px; }}
QPushButton {{ background-color: #303030; color: #f0f0f0; border: none; border-radius: 6px; padding: 7px 14px; }}
QPushButton:hover {{ background-color: #404040; }}
QPlainTextEdit {{ background-color: #1d1d1d; color: #f0f0f0; border: none; border-radius: 14px; padding: 12px 10px; font-size: 22px; font-family: "{FONT_FAMILY}"; }}
QLabel#label-lilnote {{ color: #ffffff; font-family: "{FONT_FAMILY}"; font-size: 14px; }}
QLabel#label-data {{ color: #ffffff; font-family: "{FONT_FAMILY}"; font-size: 10px; }}
QWidget#status_bar QLabel {{ color: #f0f0f0; font-family: "{FONT_FAMILY}"; font-size: 11px; }}
QPushButton#theme_button {{ background: transparent; color: #f0f0f0; border: none; border-radius: 13px; padding: 0; font-family: "{SYMBOL_FONT_FAMILY}"; font-size: 20px; }}
QPushButton#theme_button:hover {{ background-color: #303030; border-radius: 13px; }}
QPushButton#theme_button:pressed {{ background-color: #404040; border-radius: 13px; }}
"""


LIGHT_THEME = f"""
QMainWindow {{ background-color: #f4f4f4; }}
QInputDialog, QMessageBox {{ background-color: #ffffff; color: #202020; }}
QInputDialog QLabel, QMessageBox QLabel {{ color: #202020; }}
QLineEdit {{ background-color: #ffffff; color: #202020; border: 1px solid #c5c5c5; border-radius: 6px; padding: 7px; }}
QPushButton {{ background-color: #e0e0e0; color: #202020; border: none; border-radius: 6px; padding: 7px 14px; }}
QPushButton:hover {{ background-color: #d0d0d0; }}
QPlainTextEdit {{ background-color: #ffffff; color: #202020; border: none; border-radius: 14px; padding: 12px 10px; font-size: 22px; font-family: "{FONT_FAMILY}"; }}
QLabel#label-lilnote {{ color: #202020; font-family: "{FONT_FAMILY}"; font-size: 14px; }}
QLabel#label-data {{ color: #555555; font-family: "{FONT_FAMILY}"; font-size: 10px; }}
QWidget#status_bar QLabel {{ color: #202020; font-family: "{FONT_FAMILY}"; font-size: 11px; }}
QPushButton#theme_button {{ background: transparent; color: #202020; border: none; border-radius: 13px; padding: 0; font-family: "{SYMBOL_FONT_FAMILY}"; font-size: 20px; }}
QPushButton#theme_button:hover {{ background-color: #dedede; border-radius: 13px; }}
QPushButton#theme_button:pressed {{ background-color: #cccccc; border-radius: 13px; }}
"""

# lilnote

> just a lil place to write things down

A simple, lightweight notepad built with Python + PySide6. No distractions, no bloated menus — open, write, save.

Sibling project of [lil-code](https://github.com/ericfr1tzenvalle/lil-code), same philosophy: minimal interfaces, built from scratch.

## Features

- Create, open, save, and save as (`Ctrl+N`, `Ctrl+O`, `Ctrl+S`, `Ctrl+Shift+S`)
- Light/dark theme toggle
- Live clock in the top bar
- Confirmation before discarding unsaved changes (new note / closing the app)
- Quick shortcuts help (`Ctrl+H`)

## Getting Started

```bash
pip install -r requirements.txt
python main.py
```

Notes are saved by default in the `notes/` folder (created automatically on first run).

## Structure

```
lilnote/
├── main.py
├── styles/
│   └── theme.py       # light and dark themes
└── ui/
    ├── main_window.py # main window, file actions, shortcuts
    ├── note_pad.py     # editing area
    └── top_bar.py      # top bar (theme, title, clock)
```
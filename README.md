# CTk-quiz
A class-based Python quiz app with a CustomTkinter interface, randomized questions, score tracking, and a leaderboard. Questions can be edited in the "Perguntas" folder.

## Requirements

- **Python 3.9 or newer** (Python 3.11 is recommended). The source uses annotations such as `list[str]`, which require Python 3.9 or newer as written.
- **Tkinter**, which is included with the standard Python installer on Windows. On Debian/Ubuntu Linux, install it with `sudo apt install python3-tk` if it is missing.
- **CustomTkinter**, installed from `requirements.txt` below.

The project imports `tkinter`, `messagebox`, `random`, and `os` from Python's standard library. The only direct third-party package used by the project is `customtkinter`; pip installs its required dependencies automatically.

## Installation on Windows 11

Run these commands in PowerShell from the project folder (the folder containing `QUESTIONÁRIO.py` and `requirements.txt`):

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Then launch the quiz:

```powershell
.\.venv\Scripts\python.exe "QUESTIONÁRIO.py"
```

These commands use the virtual environment's Python directly, so activation is optional.

## Installation on macOS or Linux

From the project folder:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python "QUESTIONÁRIO.py"
```

On Debian/Ubuntu, if Tkinter is missing, install the system package first:

```bash
sudo apt install python3-tk
```

## Changelog

Updates to this document will be described here.

### 0.1.0 (Dec 2023)

Initial version.

### 0.1.1 (15 Oct 2026)

Replaced Desktop-specific file paths and names with project-relative references.

## Credits and licensing

Copyright (c) 2025 Pedro Lourenço. All rights reserved.

This program is licensed under the MIT License. See the `LICENSE` file for the full license text.


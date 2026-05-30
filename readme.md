# Utility Scripts Collection

This repository contains a collection of utility scripts designed to make daily tasks easier. It includes a couple of Python scripts for PDF manipulation and directory tree generation, as well as an AutoHotkey script for quick text deletion.

---

## 🛠 Prerequisites and Setup

Before using the scripts, make sure you have the required software installed on your system.

### 1. Python Environment
The Python scripts require **Python 3** to be installed on your system.
You will also need to install the required Python packages. Open your terminal or command prompt in this directory and run:

```cmd
pip install -r requirements.txt
```
*(This installs `pypdf` for the PDF extractor and `pyperclip` for the tree generator).*

### 2. AutoHotkey Environment
The `.ahk` script requires **AutoHotkey v2**. You can download and install it from the [official AutoHotkey website](https://www.autohotkey.com/).

---

## 📜 Script Details

### 1. `pdfpage.py` (PDF Page Extractor)
A command-line Python script that extracts specific pages or page ranges from an existing PDF file and saves them into a new PDF document.

**What it does:**
- Extracts individual pages (e.g., `1, 2, 8`).
- Extracts ranges of pages (e.g., `4-6`, `10-12`).
- Saves the extracted pages into a new PDF file. If you don't specify an output file name, it automatically generates one based on the original file name and the pages requested (e.g., `document_pages_1_2_4-6.pdf`).

**How to use it:**
Run the script from the command line, providing the input PDF and the pages you want to extract:
```cmd
python pdfpage.py input.pdf "1,2,4-6,8" [output.pdf]
```
*(Note: Page numbers are 1-indexed. Ensure you put the page range string in quotes).*

### 2. `tree.py` (Directory Tree Generator)
A command-line Python script that generates a visual, Windows-style directory tree of any given folder and instantly copies the output to your clipboard.

**What it does:**
- Recursively scans a folder and prints its structure (directories and files).
- Formats the output perfectly using box-drawing characters (`├──`, `└──`, `│`).
- Automatically copies the resulting text tree to your clipboard so you can paste it anywhere immediately.
- Handles Permission Denied errors gracefully without crashing.

**How to use it:**
Run the script with the path to the folder you want to visualize:
```cmd
python tree.py "C:\Your\Folder\Path"
```
Once it finishes, just press `Ctrl+V` wherever you need the tree!

### 3. `home_end_del.ahk` (Line Deletion Shortcuts)
An AutoHotkey v2 script that provides two very handy keyboard shortcuts for quickly deleting text on your current line without having to reach for the mouse.

**What it does:**
It sets up global hotkeys that select text from your cursor to either the beginning or the end of the line, and instantly deletes it.

**Hotkeys:**
- <kbd>Ctrl</kbd> + <kbd>Win</kbd> + <kbd>Home</kbd> : Deletes everything from your current cursor position to the **beginning** of the line.
- <kbd>Ctrl</kbd> + <kbd>Win</kbd> + <kbd>End</kbd> : Deletes everything from your current cursor position to the **end** of the line.

**How to use it:**
1. Ensure AutoHotkey v2 is installed.
2. Double-click `home_end_del.ahk` to run it. It will run in the background (you can see it in your system tray).
3. Place your cursor anywhere in a text field and use the shortcuts above!

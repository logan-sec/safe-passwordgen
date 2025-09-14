# Local Password Generator 🔑

A simple, secure password generator written in Python.  
Unlike online generators, this runs entirely on **your own device**, so your passwords never leave your computer.

## ✨ Features
- Cryptographically secure randomness (`secrets` module).
- Adjustable password length with `--length`.
- Includes uppercase, lowercase, digits, and symbols.
- Local-only — **no internet usage**.
- Lightweight and beginner-friendly (under 30 lines of code).

---

## 📦 Requirements
- Python 3.6 or higher  
- Works on Linux, macOS, and Windows

---

## 🚀 Usage

Clone the repo and run:

```bash
# Default: 36-character password
python3 passwordgen.py

# Custom length (e.g., 24)
python3 passwordgen.py --length 24

⚠️ Notes

Minimum length is 8 characters. If you enter less, the program will exit with an error.

Passwords are printed to the terminal — they are not saved anywhere.

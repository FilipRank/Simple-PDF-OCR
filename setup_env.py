import os
import sys
import shutil
from tkinter import messagebox

def setup_bundled_tools():
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))

    tesseract = os.path.join(base, "bin", "tesseract")
    ghostscript = os.path.join(base, "bin", "ghostscript", "bin")

    os.environ["PATH"] = os.pathsep.join([
        tesseract,
        ghostscript,
        os.environ.get("PATH", "")
    ])

    print(f"Added {tesseract} (tesseract) to PATH")
    print(f"Added {ghostscript} (ghostscript) to PATH")

    os.environ["TESSDATA_PREFIX"] = os.path.join(tesseract, "tessdata")

    if not check_tools():
        return

def check_tools():
    missing = []

    if not shutil.which("tesseract"):
        missing.append(f"Tesseract OCR")

    if not (shutil.which("gswin64c") or shutil.which("gs")):
        missing.append("Ghostscript")

    if missing:
        messagebox.showerror(
            "Missing components",
            "Missing:\n" + "\n".join(missing)
        )
        return False

    return True
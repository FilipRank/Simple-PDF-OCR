Simple PDF OCR provides a user-friendly interface for performing OCR on multiple PDFs with the click of a few buttons. It uses OCRMyPDF in the background.

To download the application for your operating system, click on the latest release, which you can find in the release tab on the right-hand side of the Github interface.

The application supports doing OCR on multiple PDFs at simultaneously.

# Running from source

This project uses Python 3.12.10.

1. Create a python virtual environment and activate it:

    On GNU/Linux, and OSX:

    `python3 -m venv .venv`

    `source .venv/bin/activate`

    On Windows:

    `python -m venv .venv`

    `.venv\Scripts\Activate.ps1`

2. Install dependencies

    `pip install -r requirements.txt`

3. To run:

    `python main.py`

4. To build using PyInstaller:

    `pip install pyinstaller`

    `pyinstaller --onefile --name Simple-PDF-OCR main.py`    
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading
import ocrmypdf
from ocrmypdf._options import OcrOptions, ProcessingMode

def worker(input_files, output_dir):
    success_count = 0

    for pdf in input_files:
        filename = os.path.basename(pdf)
        output_pdf = os.path.join(
            output_dir,
            filename
        )

        try:
            status_label.config(
                text=f"Processing: {filename}"
            )


            options = OcrOptions(
                input_file=pdf,
                output_file=output_pdf,
                mode=ProcessingMode.force,
                skip_big=True
            )
            ocrmypdf.ocr(options)

            success_count += 1
        except Exception as e:
            print(f"Failed on file: {filename}")
            print(e)
        
    status_label.config(
        text=f"Finished {success_count}/{len(input_files)} files"
    )

    messagebox.showinfo(
        "Complete",
        f"Processed {success_count} of {len(input_files)} files."
    )


def run_ocr():
    input_files = filedialog.askopenfilenames(
        title="Select PDFs",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not input_files:
        return
    
    output_dir = filedialog.askdirectory(
        title="Select output folder"
    )

    if not output_dir:
        return
    
    threading.Thread(
        target=worker,
        args=(input_files, output_dir),
        daemon=True
    ).start()

root = tk.Tk()
root.title("Simple PDF OCR")
root.geometry("400x200")

tk.Button(
    root,
    text="Select PDF and OCR",
    command=run_ocr
).pack(pady=40)

status_label = tk.Label(
    root,
    text="Ready"
)
status_label.pack()


root.mainloop()
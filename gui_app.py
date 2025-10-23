import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image, ImageTk
from pathlib import Path
import io

def remove_background(input_path: str, output_path: str):
    """Removes background from image and saves output."""
    try:
        input_file = Path(input_path)
        output_file = Path(output_path)

        if not input_file.exists():
            messagebox.showerror("Error", "Input file not found.")
            return
        
        img = Image.open(input_file)
        result = remove(img)
        result.save(output_file)
        messagebox.showinfo("Success", f"Saved output to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_input_file():
    filename = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp *.bmp")]
    )

    if filename:
        input_path.set(filename)
        preview_image(filename)

def select_output_file():
    filename = filedialog.asksaveasfilename(
        title="Save Output As",
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )
    if filename:
        output_path.set(filename)

def preview_image(path):
    img = Image.open(path)
    img.thumbnail((250, 250))
    img_tk = ImageTk.PhotoImage(img)
    preview_label.config(image=img_tk)
    preview_label.image = img_tk

def start_process():
    if not input_path.get() or not output_path.get():
        messagebox.showwarning("Warning", "Please select input and output files.")
        return
    remove_background(input_path.get(), output_path.get())

root = tk.Tk()
root.title("Background Remover (Tkinter GUI)")
root.geometry("400x500")

input_path = tk.StringVar()
output_path = tk.StringVar()

tk.Label(root, text="Input Image:").pack(pady=5)    
tk.Entry(root, textvariable=input_path, width=40).pack()
tk.Button(root, text="Browse", command=select_input_file).pack(pady=5)

tk.Label(root, text="Output Image:").pack(pady=5)
tk.Entry(root, textvariable=output_path, width=40).pack()
tk.Button(root, text="Save As", command=select_output_file).pack(pady=5)

tk.Button(root, text="Remove Background", command=start_process, bg="#4CAF50", fg="white").pack(pady=15)

preview_label = tk.Label(root)
preview_label.pack(pady=10)

tk.Label(root, text="© 2025 Background Remover by Janak").pack(side="bottom", pady=10)


root.mainloop()
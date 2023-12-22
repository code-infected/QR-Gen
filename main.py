import pyqrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox


def generate_qr():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    qr = pyqrcode.create(url)
    qr.png("temp.png", scale=8)

    # Load and display the QR code image on the canvas
    img = Image.open("temp.png")
    img = img.resize((250, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    canvas.image = img
    canvas.create_image(0, 0, anchor=tk.NW, image=img)


def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr = pyqrcode.create(entry_url.get())
        qr.png(file_path, scale=8)
        messagebox.showinfo("Success", f"QR code saved as {file_path}")


# Create the main window
root = tk.Tk()
root.title("QR Gen")

# Entry widget for URL input
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=20)

# Button to generate QR code
btn_generate = tk.Button(root, text="Generate QR Code", command=generate_qr)
btn_generate.pack(pady=10)

# Canvas to display QR code
canvas = tk.Canvas(root, width=250, height=250)
canvas.pack(pady=20)

# Button to save QR code
btn_save = tk.Button(root, text="Save QR Code", command=save_qr)
btn_save.pack(pady=10)

root.mainloop()

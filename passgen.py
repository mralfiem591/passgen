import tkinter as tk
from tkinter import ttk, messagebox
import string
import random

def generate_password():
    length = length_var.get()
    chars = ""
    if use_upper.get():
        chars += string.ascii_uppercase
    if use_lower.get():
        chars += string.ascii_lowercase
    if use_digits.get():
        chars += string.digits
    if use_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("No character sets", "Please select at least one character set!")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x200")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use('clam')

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Password display
password_var = tk.StringVar()
password_entry = ttk.Entry(main_frame, textvariable=password_var, font=("Segoe UI", 14), state="readonly", width=30)
password_entry.grid(row=0, column=0, columnspan=3, pady=(0, 15))

# Options
length_var = tk.IntVar(value=12)
ttk.Label(main_frame, text="Length:").grid(row=1, column=0, sticky="w")
length_spin = ttk.Spinbox(main_frame, from_=6, to=32, textvariable=length_var, width=5)
length_spin.grid(row=1, column=1, sticky="w")

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

ttk.Checkbutton(main_frame, text="Uppercase", variable=use_upper).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(main_frame, text="Lowercase", variable=use_lower).grid(row=2, column=1, sticky="w")
ttk.Checkbutton(main_frame, text="Numbers", variable=use_digits).grid(row=3, column=0, sticky="w")
ttk.Checkbutton(main_frame, text="Symbols", variable=use_symbols).grid(row=3, column=1, sticky="w")

# Buttons
generate_btn = ttk.Button(main_frame, text="Generate", command=generate_password)
generate_btn.grid(row=4, column=0, pady=20, sticky="ew", columnspan=2)

copy_btn = ttk.Button(main_frame, text="Copy", command=copy_to_clipboard)
copy_btn.grid(row=4, column=2, pady=20, sticky="ew")

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
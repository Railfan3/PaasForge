import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------- Password Generator Logic ----------
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4 characters.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    if not any([use_upper.get(), use_lower.get(), use_digits.get(), use_special.get()]):
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    char_pool = ""
    password_chars = []

    if use_upper.get():
        char_pool += string.ascii_uppercase
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_lower.get():
        char_pool += string.ascii_lowercase
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_digits.get():
        char_pool += string.digits
        password_chars.append(random.choice(string.digits))
    if use_special.get():
        char_pool += string.punctuation
        password_chars.append(random.choice(string.punctuation))

    while len(password_chars) < length:
        password_chars.append(random.choice(char_pool))

    random.shuffle(password_chars)
    password = ''.join(password_chars)
    password_output.config(state='normal')
    password_output.delete(0, tk.END)
    password_output.insert(0, password)
    password_output.config(state='readonly')


# ---------- Custom Black-Spot Checkbox ----------
def add_black_spot_checkbox(parent, text, variable):
    frame = tk.Frame(parent, bg="#3E0066")
    frame.pack(anchor="w", pady=3)

    canvas = tk.Canvas(frame, width=20, height=20, bg="white", highlightthickness=1, highlightbackground="black")
    canvas.pack(side="left", padx=10)
    circle = canvas.create_oval(5, 5, 15, 15, fill="", outline="")

    def toggle():
        if variable.get():
            variable.set(False)
            canvas.itemconfig(circle, fill="", outline="")
        else:
            variable.set(True)
            canvas.itemconfig(circle, fill="black", outline="black")

    canvas.bind("<Button-1>", lambda e: toggle())

    label = tk.Label(frame, text=text, font=("Segoe UI", 10), fg="white", bg="#3E0066")
    label.pack(side="left")
    label.bind("<Button-1>", lambda e: toggle())


# ---------- GUI Setup ----------
root = tk.Tk()
root.title("🔐 Strong Password Generator")
root.geometry("500x500")
root.config(bg="#3A0069")

# Title
tk.Label(root, text="🛡️ Secure Password Generator", font=("Segoe UI", 16, "bold"),
         bg="#3E0066", fg="#CE93D8").pack(pady=20)

# Length Input
LABEL_STYLE = {"font": ("Segoe UI", 11), "bg": "#3E0066", "fg": "white"}
ENTRY_STYLE = {"bg": "#F3EEF3", "fg": "black", "insertbackground": "white"}

tk.Label(root, text="Password Length:", **LABEL_STYLE).pack()
length_entry = tk.Entry(root, width=10, font=("Segoe UI", 12), **ENTRY_STYLE)
length_entry.pack(pady=5)

# Checkboxes Area
checkbox_frame = tk.Frame(root, bg="#3E0066")
checkbox_frame.pack(pady=15)

# Boolean Variables
use_upper = tk.BooleanVar()
use_lower = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_special = tk.BooleanVar()

# Add custom black spot checkboxes
add_black_spot_checkbox(checkbox_frame, "Include UPPERCASE", use_upper)
add_black_spot_checkbox(checkbox_frame, "Include lowercase", use_lower)
add_black_spot_checkbox(checkbox_frame, "Include digits", use_digits)
add_black_spot_checkbox(checkbox_frame, "Include special characters", use_special)

# Generate Button with Hover Effect
def on_enter(e): generate_btn.config(bg="#AB47BC")
def on_leave(e): generate_btn.config(bg="#CE93D8")

generate_btn = tk.Button(root, text="Generate Password", command=generate_password,
                         font=("Segoe UI", 12, "bold"), bg="#CE93D8", fg="black", padx=15, pady=5, relief="flat")
generate_btn.pack(pady=15)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

# Password Output
tk.Label(root, text="Generated Password:", **LABEL_STYLE).pack()
password_output = tk.Entry(root, width=30, font=("Consolas", 14), justify="center", state='readonly', **ENTRY_STYLE)
password_output.pack(pady=10)

# Footer
tk.Label(root, text="MUKUL'S PASSFORGE 💡", font=("Segoe UI", 9), bg="#723F94", fg="#DDDDDD").pack(side="bottom", pady=10)

root.mainloop()

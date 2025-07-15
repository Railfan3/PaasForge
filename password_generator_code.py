import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4 characters.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    if not (use_upper or use_lower or use_digits or use_special):
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    char_pool = ""
    password_chars = []

    if use_upper:
        char_pool += string.ascii_uppercase
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        char_pool += string.ascii_lowercase
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        password_chars.append(random.choice(string.digits))
    if use_special:
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

# Tkinter GUI setup
root = tk.Tk()
root.title("🔐 Strong Password Generator")
root.geometry("500x500")
root.config(bg="#3A0069")  # Purple background

# Optional icon
try:
    root.iconbitmap("icon.ico")
except Exception as e:
    print("Icon not set:", e)

# Styling
LABEL_STYLE = {"font": ("Segoe UI", 11), "bg": "#3E0066", "fg": "white"}
ENTRY_STYLE = {"bg": "#F3EEF3", "fg": "black", "insertbackground": "white"}

# Title
tk.Label(root, text="🛡️ Secure Password Generator", font=("Segoe UI", 16, "bold"),
         bg="#3E0066", fg="#CE93D8").pack(pady=20)

# Length input
tk.Label(root, text="Password Length:", **LABEL_STYLE).pack()
length_entry = tk.Entry(root, width=10, font=("Segoe UI", 12), **ENTRY_STYLE)
length_entry.pack(pady=5)

# Checkboxes frame (centered and formally aligned)
checkbox_frame = tk.Frame(root, bg="#3E0066")
checkbox_frame.pack(pady=15)

# BooleanVars
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

# Formally aligned checkbuttons
def add_checkbox(text, variable):
    cb = tk.Checkbutton(
        checkbox_frame,
        text=text,
        variable=variable,
        font=("Segoe UI", 10),
        bg="#3E0066",
        fg="white",
        activebackground="#3E0066",
        activeforeground="white",
        selectcolor="white",
        anchor="w",
        justify="left",
        padx=10,
        width=30
    )
    cb.pack(anchor="w", pady=3)

add_checkbox("Include UPPERCASE", upper_var)
add_checkbox("Include lowercase", lower_var)
add_checkbox("Include digits", digits_var)
add_checkbox("Include special characters", special_var)

# Button hover effect
def on_enter(e): generate_btn.config(bg="#AB47BC")
def on_leave(e): generate_btn.config(bg="#CE93D8")

generate_btn = tk.Button(root, text="Generate Password", command=generate_password,
                         font=("Segoe UI", 12, "bold"), bg="#CE93D8", fg="black", padx=15, pady=5, relief="flat")
generate_btn.pack(pady=15)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

# Output
tk.Label(root, text="Generated Password:", **LABEL_STYLE).pack()
password_output = tk.Entry(root, width=30, font=("Consolas", 14), justify="center", state='readonly', **ENTRY_STYLE)
password_output.pack(pady=10)

# Footer
tk.Label(root, text="MUKUL'S PASSFORGE 💡", font=("Segoe UI", 9), bg="#723F94", fg="#DDDDDD").pack(side="bottom", pady=10)

root.mainloop()

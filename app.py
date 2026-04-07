import tkinter as tk
from main import generate_password
from utils import check_strength
import json

BG_COLOR = "#121212"
FG_COLOR = "#ffffff"
BTN_COLOR = "#1f1f1f"
ACCENT = "#6C244C"

def generate():
    try:
        length = int(entry.get())

        if length < 4 or length > 32:
            result_var.set("Length must be 4–32")
            strength_var.set("")
            return

        password = generate_password(length)

        result_var.set(password)
        strength_var.set("Strength: " + check_strength(password))

    except ValueError:
        result_var.set("Enter a valid number")
        strength_var.set("")

def copy():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())

def save():
    data = {"password": result_var.get()}

    try:
        with open("passwords.json", "r") as f:
            existing = json.load(f)
    except:
        existing = []

    existing.append(data)

    with open("passwords.json", "w") as f:
        json.dump(existing, f, indent=4)

root = tk.Tk()
root.title("Password Generator")
root.geometry("320x300")
root.configure(bg=BG_COLOR)

tk.Label(root, text="Password Generator",
         bg=BG_COLOR, fg=ACCENT,
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter Length:",
         bg=BG_COLOR, fg=FG_COLOR).pack()

entry = tk.Entry(root, bg=BTN_COLOR, fg=FG_COLOR,
                 insertbackground=FG_COLOR, justify="center")
entry.pack(pady=5)

tk.Button(root, text="Generate",
          bg=ACCENT, fg="black",
          command=generate).pack(pady=5)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var,
         bg=BG_COLOR, fg=FG_COLOR,
         wraplength=280).pack(pady=5)

strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var,
         bg=BG_COLOR, fg="#bbbbbb").pack()

tk.Button(root, text="Copy",
          bg=BTN_COLOR, fg=FG_COLOR,
          command=copy).pack(pady=5)

tk.Button(root, text="Save",
          bg=BTN_COLOR, fg=FG_COLOR,
          command=save).pack()

root.mainloop()
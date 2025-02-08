import re
from tkinter import Tk, Label, Entry, Button, StringVar

def check_password_strength(password):
    strength = "Weak"
    if len(password) >= 8:
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            if re.search(r"[0-9]", password) and re.search(r"[!@#$%^&*()_+=-]", password):
                strength = "Strong"
            else:
                strength = "Medium"
    return strength

def evaluate_password():
    password = password_var.get()
    strength = check_password_strength(password)
    result_var.set(f"Password Strength: {strength}")

# GUI Setup
root = Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

password_var = StringVar()
result_var = StringVar()

Label(root, text="Enter Password:").pack(pady=5)
Entry(root, textvariable=password_var, show="*").pack(pady=5)
Button(root, text="Check Strength", command=evaluate_password).pack(pady=10)
Label(root, textvariable=result_var).pack(pady=5)

root.mainloop()

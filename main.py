import tkinter as tk
import re
from tkinter import ttk


common_words = ['password', '123456', 'qwerty', 'letmein', 'welcome']

def check_password_strength(event=None):
    password = entry.get()
    
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None
    unique_criteria = password not in common_words
    
    
    strength_score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria, unique_criteria])

   
    if strength_score == 6:
        strength_var.set(100)
        progress_bar.configure(style="green.Horizontal.TProgressbar")
        quality_label.config(text="Strong Password", fg="green")
    elif strength_score == 5:
        strength_var.set(80)
        progress_bar.configure(style="green.Horizontal.TProgressbar")
        quality_label.config(text="Good Password", fg="green")
    elif strength_score == 4:
        strength_var.set(60)
        progress_bar.configure(style="yellow.Horizontal.TProgressbar")
        quality_label.config(text="Moderate Password", fg="orange")
    elif strength_score == 3:
        strength_var.set(40)
        progress_bar.configure(style="orange.Horizontal.TProgressbar")
        quality_label.config(text="Weak Password", fg="orange")
    else:
        strength_var.set(20)
        progress_bar.configure(style="red.Horizontal.TProgressbar")
        quality_label.config(text="Very Weak Password", fg="red")

def toggle_password_visibility():
    
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(text="Hide")
    else:
        entry.config(show='*')
        toggle_button.config(text="Show")


root = tk.Tk()
root.title("Password Strength Tester")
root.geometry("400x300")
root.resizable(False, False)

label = tk.Label(root, text="Enter your password:", font=('Helvetica', 12, 'bold'))
label.pack(pady=10)


entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, show="*", width=30, font=('Helvetica', 12))
entry.grid(row=0, column=0, padx=5)
entry.bind("<KeyRelease>", check_password_strength)


toggle_button = tk.Button(entry_frame, text="Show", command=toggle_password_visibility)
toggle_button.grid(row=0, column=1)


quality_label = tk.Label(root, text="", font=('Helvetica', 12, 'bold'))
quality_label.pack(pady=5)


strength_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, length=300, variable=strength_var, maximum=100)
progress_bar.pack(pady=10)


style = ttk.Style()
style.theme_use('default')


style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', thickness=20)
style.configure("orange.Horizontal.TProgressbar", foreground='orange', background='orange', thickness=20)
style.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow', thickness=20)
style.configure("green.Horizontal.TProgressbar", foreground='green', background='green', thickness=20)


guide_label = tk.Label(root, text="Password must be 8+ \n characters with letters, \n numbers, symbols, and not common.",
                       font=('Helvetica', 10), fg='gray')
guide_label.pack(pady=10)


root.mainloop()

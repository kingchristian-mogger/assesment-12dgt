import tkinter as tk
from tkinter import messagebox

 
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, "☐ " + task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task!")

def complete_task():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)
        if task.startswith("☐"):
            task_listbox.delete(selected)
            task_listbox.insert(selected, task.replace("☐", "✔", 1))
    except:
        messagebox.showwarning("Warning", "Select a task!")

 
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")
root.configure(bg="#1e1e2e")

 
title = tk.Label(
    root,
    text="📝 TO-DO LIST",
    font=("Arial", 24, "bold"),
    bg="#1e1e2e",
    fg="white"
)
title.pack(pady=15)

 
task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)
task_entry.pack(pady=10)

 
button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack(pady=10)

add_btn = tk.Button(
    button_frame,
    text="➕ Add",
    command=add_task,
    bg="#4CAF50",
    fg="white",
    width=12
)
add_btn.grid(row=0, column=0, padx=5)

complete_btn = tk.Button(
    button_frame,
    text="✔ Complete",
    command=complete_task,
    bg="#2196F3",
    fg="white",
    width=12
)
complete_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(
    button_frame,
    text="🗑 Delete",
    command=delete_task,
    bg="#F44336",
    fg="white",
    width=12
)
delete_btn.grid(row=0, column=2, padx=5)

 
task_listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=40,
    height=18,
    bg="#313244",
    fg="white",
    selectbackground="#89b4fa"
)
task_listbox.pack(pady=20)

root.mainloop()
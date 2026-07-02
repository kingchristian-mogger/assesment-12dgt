import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get()

    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")


def complete_task():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)

        if not task.startswith("Completed - "):
            task_listbox.delete(selected)
            task_listbox.insert(selected, "Completed - " + task)

    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")


root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")
root.configure(bg="gray")


title = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 22, "bold"),
    bg="black",
    fg="white"
)
title.pack(pady=15)


task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)
task_entry.pack(pady=10)


button_frame = tk.Frame(root, bg="gray")
button_frame.pack(pady=10)


add_button = tk.Button(
    button_frame,
    text="Add",
    command=add_task,
    bg="green",
    fg="white",
    width=12
)
add_button.grid(row=0, column=0, padx=5)


complete_button = tk.Button(
    button_frame,
    text="Complete",
    command=complete_task,
    bg="blue",
    fg="white",
    width=12
)
complete_button.grid(row=0, column=1, padx=5)


delete_button = tk.Button(
    button_frame,
    text="Delete",
    command=delete_task,
    bg="red",
    fg="white",
    width=12
)
delete_button.grid(row=0, column=2, padx=5)


task_listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=40,
    height=18,
    bg="white",
    fg="black",
    selectbackground="light blue"
)
task_listbox.pack(pady=20)


root.mainloop()
import tkinter as tk
import numpy as np
from tkinter import messagebox
import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"title": task, "done": False})
        task_entry.delete(0, tk.END)
        refresh_task_list()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks.pop(index)
        refresh_task_list()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def toggle_task():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["done"] = not tasks[index]["done"]
        refresh_task_list()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark done/undone.")

def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['title']}")

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List App")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

task_entry = tk.Entry(frame, width=40)
task_entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=1, padx=5)

task_listbox = tk.Listbox(frame, width=50, height=10, selectbackground="lightblue")
task_listbox.grid(row=1, column=0, columnspan=2, pady=10)

toggle_btn = tk.Button(frame, text="Mark Done/Undone", command=toggle_task)
toggle_btn.grid(row=2, column=0, pady=5)

delete_btn = tk.Button(frame, text="Delete Task", command=delete_task)
delete_btn.grid(row=2, column=1, pady=5)

refresh_task_list()
root.mainloop()

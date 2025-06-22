import tkinter as tk
from tkinter import messagebox
import os 
import json

TASKS_FILE = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)

def save_tasks():
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def show_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()
    for index, task in enumerate(tasks):
        status = "✅ " if task["completed"] else "❌ "
        lbl = tk.Label(task_frame, text=f"{index+1}. {status}{task['task']}", anchor="w", justify="left")
        lbl.pack(fill="both", pady=2)


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(False, False)


# Header label
title = tk.Label(root, text="📝 To-Do List", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

# Task list display frame
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

# Add task entry and button
entry = tk.Entry(root, width=30, font=("Helvetica", 12))
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", width=15)
add_button.pack(pady=5)
load_tasks()
show_tasks()

# Start GUI loop
root.mainloop()

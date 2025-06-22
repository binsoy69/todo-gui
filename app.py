import tkinter as tk
from tkinter import messagebox
import os 
import json

# To-Do List Application using Tkinter and JSON for persistence

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
        task_text = f"{index + 1}. {'✅' if task['completed'] else '❌'} {task['task']}"

        task_row = tk.Frame(task_frame)
        task_row.pack(fill="x", pady=2)

        lbl = tk.Label(task_row, text=task_text, anchor="w", width=25)
        lbl.pack(side="left", padx=5)

        toggle_btn = tk.Button(task_row, text="Toggle", width=7, font=("Helvetica", 9), bg="#97ffa5", command=lambda i=index: toggle_task(i))
        toggle_btn.pack(side="right", padx=5)

        delete_btn = tk.Button(task_row, text="Delete", width=7, font=("Helvetica", 9), bg="#ffcccc", command=lambda i=index: delete_task(i))
        delete_btn.pack(side="right", padx=5)


def add_task():
    task_text = entry.get().strip()
    if task_text == "":
        messagebox.showwarning("Input Error", "Task cannot be empty.")
        return

    tasks.append({"task": task_text, "completed": False})
    save_tasks()
    entry.delete(0, tk.END)
    show_tasks()

def toggle_task(index):
    tasks[index]["completed"] = not tasks[index]["completed"]
    save_tasks()
    show_tasks()

def delete_task(index):
    confirm = messagebox.askyesno("Confirm Delete", f"Delete task: {tasks[index]['task']}?")
    if confirm:
        tasks.pop(index)
        save_tasks()
        show_tasks()


# GUI setup
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

add_button = tk.Button(root, text="Add Task", width=15, command=add_task, font=("Helvetica", 10), bg="#5dbeff")
add_button.pack(pady=5)
load_tasks()
show_tasks()

# Start GUI loop
root.mainloop()

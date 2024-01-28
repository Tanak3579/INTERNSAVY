import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        listbox_tasks.itemconfig(tk.END, {'bg': '#FF6F61', 'fg': 'white', 'font': ('Arial', 12, 'bold')})
        root.after(500, lambda: listbox_tasks.itemconfig(tk.END, {'bg': 'white', 'fg': 'black', 'font': ('Arial', 12)}))

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = listbox_tasks.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, font=("Arial", 12), bg="#FFB6C1", selectbackground="#FF8C00")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50, font=("Arial", 12))
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task, bg="#00008B", fg="white", font=("Arial", 12, 'bold'))
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task, bg="#050505", fg="white", font=("Arial", 12, 'bold'))
button_delete_task.pack()

button_save_tasks = tk.Button(root, text="Save Tasks", width=48, command=save_tasks, bg="#1874CD", fg="white", font=("Arial", 12, 'bold'))
button_save_tasks.pack()

load_tasks()  # Load tasks from file on startup

root.mainloop()

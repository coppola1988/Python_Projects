import tkinter as tk
from tkinter import ttk

def add_task():
    if task.get() != "":
        task_treeview.insert(parent="", index="end", values=(task.get().replace(" ", "\ ")))
        task_entry.delete(0, tk.END)
    else:
        print("Bitte einen Task eingeben ...")


def remove_task():
    selected_item = task_treeview.selection()
    if selected_item != ():
        task_treeview.delete(selected_item)
    else:
        print("Bitte einen Task markieren ...")

root = tk.Tk()
root.title("ToDo-Liste")
root.geometry("600x390")
style = ttk.Style()
style.theme_use("clam")
root.columnconfigure(0,weight=1)

task = tk.StringVar()

# Frames
user_input_frame = ttk.Frame(root)
user_input_frame.grid(row=0, column=0, pady=20)
task_frame = ttk.Frame(root)
task_frame.grid(row=1, column=0, pady=10)

# Widgets für user_input_frame
task_label = ttk.Label(user_input_frame, text="Task: ")
task_label.grid(row=0, column=0)
task_entry = ttk.Entry(user_input_frame, width=60, textvariable=task)
task_entry.grid(row=0, column=1)

add_task_button = ttk.Button(user_input_frame, text="Task hinzufügen", command=add_task)
add_task_button.grid(row=1, column=0, columnspan=2, sticky="EW", pady=2)

# Widgets für task_frame
task_treeview = ttk.Treeview(task_frame, selectmode="browse")
task_treeview.grid(row=0, column=0, sticky="EW")

# Spalten definieren und konfigurieren
task_treeview.configure(columns=("task"))
task_treeview.column("#0", width=0, stretch=tk.NO)
task_treeview.heading("task", text="Tasks")
task_treeview.column("task", width=575)

# Scrollbar für Treeview Widget erzeugen und an task_treeview binden
task_treeview_scroll = ttk.Scrollbar(task_frame, orient="vertical", command=task_treeview.yview)
task_treeview_scroll.grid(row=0, column=1, sticky="NS")
task_treeview.configure(yscrollcommand=task_treeview_scroll.set)

delete_task_button = ttk.Button(task_frame, text="Markierten Task entfernen" , command=remove_task)
delete_task_button.grid(row=1, column=0, columnspan=2, sticky="EW")

root.mainloop()
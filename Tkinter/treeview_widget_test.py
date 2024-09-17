import tkinter as tk
from tkinter import ttk

def remove_all_items():
    for item in example_tree.get_children():
        example_tree.delete(item)


def remove_one_item():
    selected_item = example_tree.selection()[0]
    example_tree.delete(selected_item)

def remove_all_selected_items():
    selected_items = example_tree.selection()
    for item in selected_items:
        example_tree.delete(item)

root = tk.Tk()
root.geometry("500x500")

style = ttk.Style()
style.theme_use("clam")

example_tree = ttk.Treeview(root, selectmode="browse") # Durch Browse wird verhindert, dass man mehrere Zeilen markieren kann. Standart wäre extended
example_tree.pack()

example_tree.configure(columns=("firstname", "lastname", "phone"))

# Überschriften festlegen
example_tree.heading("#0", text="Tree Column")
example_tree.heading("firstname", text="Vorname", anchor="w") # Anchor setzt die Schrift linksbündig an
example_tree.heading("lastname", text="Nachname")
example_tree.heading("phone", text="Telefonnummer")

# Spalten konfigurieren
example_tree.column("#0", width=100)
example_tree.column("firstname", width=100)
example_tree.column("lastname", width=100, minwidth=80)
example_tree.column("phone", width=150)

# Daten hinzufügen
print(example_tree.insert(parent="", index=0, text="item_0", values=("Max", "Mustermann", "01745675665")))
example_tree.insert(parent="", index=1, text="item_1", values=("Hans", "Müller", "01758474933"))
example_tree.insert(parent="", index="end", text="item_2", values=("Karsten", "Huber", "01484485843")) # Durch end wird es immer am Ende eingefügt
print(example_tree.insert(parent="I001", index="end", text="sub_item_0", values=("", "", "08394785983484")))
example_tree.insert(parent="I001", index="end", text="sub_item_1") # Bildet Subitems
example_tree.insert(parent="I004", index="end", text="sub_sub_item_0")


remove_all_button = ttk.Button(root, text="Alle Items entfernen", command=remove_all_items)
remove_all_button.pack()

remove_one_button = ttk.Button(root, text="Ein markiertes Item entfernen", command=remove_one_item)
remove_one_button.pack()

remove_all_selected_button = ttk.Button(root, text="Alle markierten entfernen", command=remove_all_selected_items)
remove_all_selected_button.pack()


root.mainloop()
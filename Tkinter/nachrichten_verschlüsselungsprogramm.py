import tkinter as tk
from tkinter import ttk
import time





root = tk.Tk()
root.title("Verschlüsselungs-Software")

selected_action = tk.StringVar()

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == " " or char == "." or char == "!" or char == "?":
            result += char
        elif char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == " " or char == "." or char == "!" or char == "?":
            result += char
        elif char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

def perform_action():
    if selected_action.get() == "verschlüsseln":
        encrypted_input = encrypt(input_entry.get(), int(key_entry.get()))
        output_entry.delete(0, tk.END)
        output_entry.insert(0, encrypted_input)
    elif selected_action.get() == "entschlüsseln":
        decrypted_input = decrypt(input_entry.get(), int(key_entry.get()))
        output_entry.delete(0, tk.END)
        output_entry.insert(0, decrypted_input)
    else:
        print("Fehler")

input_frame = ttk.Frame(root, padding=10)
input_frame.grid(column=0, row=0)

separator = ttk.Separator(root)
separator.grid(column=0, row=1, sticky="ew")

output_frame = ttk.Frame(root, padding=10)
output_frame.grid(column=0, row=2)

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

input_label = ttk.Label(input_frame, text="Nachricht:", font=("Arial",16))
input_label.grid(column=0, row=0)

input_entry = ttk.Entry(input_frame, width=30, font=("Arial", 16))
input_entry.grid(column=1, row=0)


input_text_scroll = ttk.Scrollbar(input_frame, orient="horizontal", command=input_entry.xview)
input_text_scroll.grid(column=1, row=1, pady=1, sticky="ew")
input_entry.configure(xscrollcommand=input_text_scroll.set)

key_label = ttk.Label(input_frame, text="Key:", font=("Arial", 16))
key_label.grid(column=0, row=2)

key_entry = ttk.Entry(input_frame, width=3, font=("Arial", 16))
key_entry.grid(column=1, row=2, pady=5, sticky="w")

action_label = ttk.Label(input_frame, text="Operation:", font=("Arial", 16))
action_label.grid(column=0, row=3)

action_rb1 = ttk.Radiobutton(input_frame, text="Verschlüsseln", variable=selected_action, value="verschlüsseln")
action_rb1.grid(column=1, row=3, sticky="w")

action_rb2 = ttk.Radiobutton(input_frame, text="Entschlüsseln", variable=selected_action, value="entschlüsseln")
action_rb2.grid(column=1, row=4, sticky="w")

action_button = ttk.Button(input_frame, text="Operation ausführen", command=perform_action)
action_button.grid(column=0, row=5, columnspan=2, sticky="ew")

output_label = ttk.Label(output_frame, text="Ergebnis:", font=("Arial", 16))
output_label.grid(column=0, row=0)

output_entry = ttk.Entry(output_frame, width=30, font=("Arial", 16))
output_entry.grid(column=1, row=0)





root.mainloop()
import tkinter as tk
from tkinter import Entry, Button, Label, Tk

class CustomDialog:
    def __init__(self, parent):
        self.result = ""
        self.parent = parent
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Custom Dialog Box")
        self.dialog.config(bg="#ff6105")
        self.dialog.geometry("350x200")
        self.dialog.focus()
        self.label = Label(self.dialog, text="Enter something:")
        self.label.pack()
        
        self.entry = Entry(self.dialog, width=15, font=("Arial", 15), justify=tk.CENTER)
        self.entry.place(relx=0.25, rely=0.45)
        self.entry.focus()
        
        self.ok_button = Button(self.dialog, text="OK", command=self.on_ok)
        self.ok_button.place(relx=0.35, rely=0.75, relwidth=0.3)

    def on_ok(self):
        self.result = self.entry.get()
        if self.result:
            print("You entered:", self.result)
        self.dialog.destroy()
        return self.result

def open_custom_dialog():
    dialog = CustomDialog(root)
    print("dialog value: ", dialog.result)

root = Tk()
root.title("Main Window")

button = Button(root, text="Open Custom Dialog Box", command=open_custom_dialog)
button.pack()

root.mainloop()

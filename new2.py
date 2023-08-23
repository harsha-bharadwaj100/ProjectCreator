import tkinter as tk
from tkinter import Entry, Button, Label, Toplevel

class CustomDialog:
    def __init__(self, parent):
        self.parent = parent
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Custom Dialog Box")
        
        self.label = Label(self.dialog, text="Enter something:")
        self.label.pack()
        
        self.entry = Entry(self.dialog)
        self.entry.pack()
        
        self.ok_button = Button(self.dialog, text="OK", command=self.on_ok)
        self.ok_button.pack()

        self.userInput = None
        self.dialog.transient(parent)  # Set the dialog as transient to the parent window

    def on_ok(self):
        self.userInput = self.entry.get()
        self.dialog.destroy()

    def get(self):
        self.dialog.grab_set()  # Prevent interaction with the parent window
        self.parent.wait_window(self.dialog)  # Wait for the dialog to be closed
        return self.userInput

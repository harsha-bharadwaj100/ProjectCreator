import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import os
from tkinter import messagebox
# Create a Tkinter window
window = tk.Tk()

# Hide the main window
window.withdraw()

# Open a file dialog to select the directory
directory = filedialog.askdirectory(title="Select Directory")

# Create a new directory
res = simpledialog.askstring('Project Directory', 'Enter: ')
if res == None or res == "": exit()
new_directory = os.path.join(directory, res)
os.mkdir(new_directory)
print("Created Project Directory:", new_directory)

# Create a file inside the new directory
file_path = os.path.join(new_directory, "main.py")
with open(file_path, 'w') as f:
    f.write('print("Hello, world!")')
print("Created main.py:", file_path)

# Create Python virtual environment
venv_path = os.path.join(new_directory, 'env')
subprocess.run([r"C:\Users\INDIA\AppData\Local\Programs\Python\Python311\python.exe", '-m', 'venv', venv_path])
print("Created Python Virtual Environment")

# Initialize Git repository
subprocess.run(['git', 'init', new_directory])
print("Initialized git")

# Create a .gitignore file
gitignore_path = os.path.join(new_directory, ".gitignore")
with open(gitignore_path, 'w') as f:
    f.write('env/')
print("Created .gitignore and added env/ to it:", gitignore_path)

# Open in vs code
response = messagebox.askyesno("Confirmation", "Open in vs code?")
if response:
    # st = 'code '+ new_directory + '\main.py'
    # print(st)
    os.system(rf'code "{new_directory}"')
    os.system(rf'code "{file_path}"')
# Close the window"D:\python programs\aaaaa\main.py"
window.destroy()
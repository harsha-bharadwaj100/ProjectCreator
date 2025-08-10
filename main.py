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

# Get project name
res = simpledialog.askstring("Project Directory", "Enter project name: ")
if res == None or res == "":
    exit()

new_directory = os.path.join(directory, res)

# Initialize uv project (this creates the directory and basic structure)
try:
    subprocess.run(["uv", "init", new_directory], check=True)
    print("Created uv project:", new_directory)
except subprocess.CalledProcessError:
    print("Error: Ensure uv is installed")
    messagebox.showerror("Error", "uv initialization failed. Is uv installed?")
    exit()

# Change to the new directory for subsequent operations
os.chdir(new_directory)

# Initialize Git repository
subprocess.run(["git", "init"], check=True)
print("Initialized git repository")

# uv init already creates a .gitignore, but let's ensure it has the right content
gitignore_path = os.path.join(new_directory, ".gitignore")
gitignore_content = """.venv/
.venv\n.env\n__pycache__/\n*.pyc\n
"""

with open(gitignore_path, "w") as f:
    f.write(gitignore_content)
print("Updated .gitignore with comprehensive Python exclusions")

# Create initial virtual environment and sync dependencies
try:
    subprocess.run(["uv", "sync"], check=True)
    print("Created virtual environment and synced dependencies")
except subprocess.CalledProcessError:
    print("Warning: Could not sync dependencies, but project created successfully")

# Get the path to the main.py file (created by uv init)
file_path = os.path.join(
    new_directory, "hello.py" if "hello" in res.lower() else "main.py"
)

# Open in VS Code
response = messagebox.askyesno("Confirmation", "Open in VS Code?")
if response:
    os.system(rf'code "{new_directory}"')
    if os.path.exists(file_path):
        os.system(rf'code "{file_path}"')

# Close the window
window.destroy()

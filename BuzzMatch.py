import tkinter as tk
from tkinter import filedialog
import os

# Function to center a window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to open the directory dialog
def open_directory_dialog():
    directory_path = filedialog.askdirectory(title="Select a directory")
    if directory_path:
        directory_path_var.set(directory_path)
        display_files(directory_path)

# Dropdown menu
def create_text_fields():
    num_fields = int(selected_option.get())

    # Create a new window for text entry fields
    text_entry_window = tk.Toplevel(Buzzmatch)
    text_entry_window.title("Keywords")

    # Center the text_entry_window
    window_width = 300
    window_height = 150
    center_window(text_entry_window, window_width, window_height)

    # Create the specified number of text fields
    for i in range(num_fields):
        labelkey = tk.Label(text_entry_window, text=f"Keyword {i + 1}:")
        labelkey.grid(row=i, column=0, padx=5, pady=5)

        entry = tk.Entry(text_entry_window)
        entry.grid(row=i, column=1, padx=5, pady=5)

# Function to display files in the selected directory
def display_files(directory_path):
    file_list.delete(0, tk.END)  # Clear the current list

    try:
        files = os.listdir(directory_path)
        for file in files:
            file_list.insert(tk.END, file)
    except FileNotFoundError:
        file_list.insert(tk.END, "Folder not found")

# Create the main application window
Buzzmatch = tk.Tk()
Buzzmatch.title("BuzzMatch")

# Center the window
window_width = 460
window_height = 400
center_window(Buzzmatch, window_width, window_height)

# StringVar for the directory path
directory_path_var = tk.StringVar()

label = tk.Label(Buzzmatch, text="Selected Folder:")
label.grid(row=0, column=0, padx=5, pady=5)

directory_path_entry = tk.Entry(Buzzmatch, textvariable=directory_path_var, state='readonly')
directory_path_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(Buzzmatch, text="Browse", command=open_directory_dialog)
browse_button.grid(row=0, column=2, columnspan=2, padx=5, pady=10)

# Create a Combobox (Dropdown) to select the number of text fields
label2 = tk.Label(Buzzmatch, text="Number of Keywords:")
label2.grid(row=1, column=0, padx=5, pady=5)
options = ["1", "2", "3", "4", "5"]
selected_option = tk.StringVar()
selected_option.set(options[0])
dropdown = tk.OptionMenu(Buzzmatch, selected_option, *options)
dropdown.grid(row=1, column=1, padx=5, pady=5)

# Create a button to create the text fields
create_button = tk.Button(Buzzmatch, text="Keywords", command=create_text_fields)
create_button.grid(row=1, column=2, padx=5, pady=5)

# Categorize button
cat_button = tk.Button(Buzzmatch, text="Categorize")
cat_button.grid(row=4, column=0, columnspan=4, padx=5, pady=10)

# Create a Listbox to display the files in the selected directory
file_list = tk.Listbox(Buzzmatch)
file_list.grid(row=5, column=0, columnspan=4, padx=5, pady=10)
file_list.config(height=10, width=40)

# Start the Tkinter main loop
Buzzmatch.mainloop()

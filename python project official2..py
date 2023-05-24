import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog

# Function to create a new file
def new_file():
    # Clear the input fields and result labels
    length_entry.delete(0, tk.END)
    reaction1_entry.delete(0, tk.END)
    reaction2_entry.delete(0, tk.END)
    no_of_forces_entry.delete(0, tk.END)

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                # Read the file contents and populate the input fields
                lines = file.readlines()
                if len(lines) >= 4:
                    length_entry.insert(0, lines[0].strip())
                    reaction1_entry.insert(0, lines[1].strip())
                    reaction2_entry.insert(0, lines[2].strip())
                    no_of_forces_entry.insert(0, lines[3].strip())
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to save the current input fields to a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                # Write the input field values to the file
                file.write(length_entry.get() + "\n")
                file.write(reaction1_entry.get() + "\n")
                file.write(reaction2_entry.get() + "\n")
                file.write(no_of_forces_entry.get() + "\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to change the text font
def change_text_font():
    font_info = fontchooser.askfont(parent=window)
    if font_info:
        selected_font = font.Font(font=font_info)
        length_entry.configure(font=selected_font)
        reaction1_entry.configure(font=selected_font)
        reaction2_entry.configure(font=selected_font)
        no_of_forces_entry.configure(font=selected_font)

# Function to change the text color
def change_text_color():
    color = colorchooser.askcolor(parent=window)
    if color:
        text_color = color[1]
        length_entry.configure(foreground=text_color)
        reaction1_entry.configure(foreground=text_color)
        reaction2_entry.configure(foreground=text_color)
        no_of_forces_entry.configure(foreground=text_color)

# Function to change the background color
def change_background_color():
    color = colorchooser.askcolor(parent=window)
    if color:
        bg_color = color[1]
        style.configure("Custom.TEntry", fieldbackground=bg_color)
        length_entry.configure(style="Custom.TEntry")
        reaction1_entry.configure(style="Custom.TEntry")
        reaction2_entry.configure(style="Custom.TEntry")
        no_of_forces_entry.configure(style="Custom.TEntry")

# Function to toggle dark mode
def toggle_dark_mode():
    if dark_mode.get():
        window.configure(bg="black")
        style.configure("TLabel", foreground="white", background="black")
        style.configure("TButton", foreground="white", background="black")
    else:
        window.configure(bg="white")
        style.configure("TLabel", foreground="black", background="white")
        style.configure("TButton", foreground="black", background="white")

# Function to perform calculation
def perform_calculation():
    length = length_entry.get()
    reaction1 = reaction1_entry.get()
    reaction2 = reaction2_entry.get()
    no_of_forces = no_of_forces_entry.get()

    # Check if the input values are valid numbers greater than 0
    if not (length.isdigit() and reaction1.isdigit() and reaction2.isdigit() and no_of_forces.isdigit()):
        messagebox.showerror("Error", "Invalid input! Please enter numeric values greater than 0.")
        return

    # Convert the input values to float/int
    length = float(length)
    reaction1 = float(reaction1)
    reaction2 = float(reaction2)
    no_of_forces = int(no_of_forces)

    # Check if the input values are greater than 0
    if length <= 0 or reaction1 <= 0 or reaction2 <= 0 or no_of_forces <= 0:
        messagebox.showerror("Error", "Invalid input! Please enter values greater than 0.")
        return

    # Perform the calculation here and display the result

# Create the main window
window = tk.Tk()
window.title("Beam Analysis Tool")

# Create a style object for customizing the widgets
style = ttk.Style(window)

# Set the theme to default
style.theme_use("default")

# Create a heading font
heading_font = font.Font(family="Arial", size=16, weight="bold")

# Create a label for the heading
heading_label = ttk.Label(window, text="Beam Analysis Tool", font=heading_font)
heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create labels and entry fields for inputs
length_label = ttk.Label(window, text="Length of the beam:")
length_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")

length_entry = ttk.Entry(window, style="Custom.TEntry")
length_entry.grid(row=1, column=1, padx=10, pady=5)

reaction1_label = ttk.Label(window, text="Distance of reaction 1:")
reaction1_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")

reaction1_entry = ttk.Entry(window, style="Custom.TEntry")
reaction1_entry.grid(row=2, column=1, padx=10, pady=5)

reaction2_label = ttk.Label(window, text="Distance of reaction 2:")
reaction2_label.grid(row=3, column=0, padx=10, pady=5, sticky="E")

reaction2_entry = ttk.Entry(window, style="Custom.TEntry")
reaction2_entry.grid(row=3, column=1, padx=10, pady=5)

no_of_forces_label = ttk.Label(window, text="Number of forces:")
no_of_forces_label.grid(row=4, column=0, padx=10, pady=5, sticky="E")

no_of_forces_entry = ttk.Entry(window, style="Custom.TEntry")
no_of_forces_entry.grid(row=4, column=1, padx=10, pady=5)

# Create an Enter button
enter_button = ttk.Button(window, text="Enter", command=perform_calculation)
enter_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Create a settings menu
settings_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Dark Mode", command=toggle_dark_mode)
settings_menu.add_command(label="Light Mode", command=toggle_dark_mode)
settings_menu.add_command(label="Text Font", command=change_text_font)
settings_menu.add_command(label="Text Color", command=change_text_color)
settings_menu.add_command(label="Background Color", command=change_background_color)

# Variable to track the dark mode state
dark_mode = tk.BooleanVar()

# Set initial dark mode state
dark_mode.set(False)

# Start the main event loop
window.mainloop()


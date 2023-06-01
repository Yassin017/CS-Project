import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog
from project2Ravikrishna import *

def start():
    global window,length_entry,reaction1_entry,reaction2_entry,no_of_forces_entry,dark_mode,style,length_slider,reaction1_slider,reaction2_slider,no_of_forces_slider
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

    length_slider = ttk.Scale(window, from_=0, to=100, orient="horizontal", command=lambda value: on_slider_move(value, length_entry))
    length_slider.grid(row=1, column=1, padx=10, pady=5)

    length_entry = ttk.Entry(window, style="Custom.TEntry")
    length_entry.grid(row=1, column=2, padx=10, pady=5)

    reaction1_label = ttk.Label(window, text="Distance of reaction 1:")
    reaction1_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")

    reaction1_slider = ttk.Scale(window, from_=0, to=100, orient="horizontal", command=lambda value: on_slider_move(value, reaction1_entry))
    reaction1_slider.grid(row=2, column=1, padx=10, pady=5)

    reaction1_entry = ttk.Entry(window, style="Custom.TEntry")
    reaction1_entry.grid(row=2, column=2, padx=10, pady=5)

    reaction2_label = ttk.Label(window, text="Distance of reaction 2:")
    reaction2_label.grid(row=3, column=0, padx=10, pady=5, sticky="E")

    reaction2_slider = ttk.Scale(window, from_=0, to=100, orient="horizontal", command=lambda value: on_slider_move(value, reaction2_entry))
    reaction2_slider.grid(row=3, column=1, padx=10, pady=5)

    reaction2_entry = ttk.Entry(window, style="Custom.TEntry")
    reaction2_entry.grid(row=3, column=2, padx=10, pady=5)

    no_of_forces_label = ttk.Label(window, text="Number of forces:")
    no_of_forces_label.grid(row=4, column=0, padx=10, pady=5, sticky="E")

    no_of_forces_slider = ttk.Scale(window, from_=0, to=100, orient="horizontal", command=lambda value: on_slider_move(value, (no_of_forces_entry)))

    no_of_forces_slider.grid(row=4, column=1, padx=10, pady=5)

    no_of_forces_entry = ttk.Entry(window, style="Custom.TEntry")
    no_of_forces_entry.grid(row=4, column=2, padx=10, pady=5)
    
    
    # Function to update the entry field value when the slider moves
    def on_slider_move(value, entry_field):
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(value))


    # Create an Enter button
    enter_button = ttk.Button(window, text="Enter", command=lambda:(get_values(),submit(window,int(no_of_forces_entry1))))
    enter_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    print(length_entry.get(),reaction1_entry.get(),reaction2_entry.get(),no_of_forces_entry.get())

    # Create a result label
    result_label = ttk.Label(window, text="", font=heading_font)
    result_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    # Create a menu bar
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    # Create a File menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)

    # Create an Edit menu
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Change Text Font", command=change_text_font)
    edit_menu.add_command(label="Change Text Color", command=change_text_color)
    edit_menu.add_command(label="Change Background Color", command=change_background_color)
    edit_menu.add_separator()
    dark_mode = tk.BooleanVar()
    edit_menu.add_checkbutton(label="Dark Mode", variable=dark_mode, command=toggle_dark_mode)

    # Run the main event loop
    window.mainloop()



def on_slider_move(value, entry_field):
    entry_field.delete(0, tk.END)
    entry_field.insert(0, value)

# Function to create a new file
def new_file():
    # Clear the input fields and result labels
    length_slider.set(0)
    reaction1_slider.set(0)
    reaction2_slider.set(0)
    no_of_forces_slider.set(0)

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                # Read the file contents and populate the input fields
                lines = file.readlines()
                if len(lines) >= 4:
                    length_slider.set(float(lines[0].strip()))
                    reaction1_slider.set(float(lines[1].strip()))
                    reaction2_slider.set(float(lines[2].strip()))
                    no_of_forces_slider.set(int(lines[3].strip()))
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to save the current input fields to a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                # Write the input field values to the file
                file.write(str(length_slider.get()) + "\n")
                file.write(str(reaction1_slider.get()) + "\n")
                file.write(str(reaction2_slider.get()) + "\n")
                file.write(str(no_of_forces_slider.get()) + "\n")
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

def get_values():
    global length_entry1,reaction11,reaction21,no_of_forces_entry1
    length_entry1=length_entry.get()
    reaction11=reaction1_entry.get()
    reaction21=reaction2_entry.get()
    no_of_forces_entry1 = int(round(float(no_of_forces_entry.get())))
    print(length_entry1,reaction11,reaction21,no_of_forces_entry1)


if __name__=="__main__":
    start()

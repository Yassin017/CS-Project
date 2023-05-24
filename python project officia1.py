import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Force Input")

# Create a label and entry for the number of forces
num_forces_label = ttk.Label(window, text="Number of Forces:")
num_forces_label.pack()

num_forces_entry = ttk.Entry(window)
num_forces_entry.pack()

# Create a list to store the input fields
input_fields = []

# Function to handle the submit button click event
def submit():
    # Get the number of forces from the entry field
    num_forces = int(num_forces_entry.get())

    # Clear the previous input fields
    clear_input_fields()

    # Create input fields for each force
    for i in range(num_forces):
        # Create labels and entry fields for magnitude, angle, and distance
        magnitude_label = ttk.Label(window, text=f"Force {i+1} Magnitude:")
        magnitude_label.pack()

        magnitude_entry = ttk.Entry(window)
        magnitude_entry.pack()

        angle_label = ttk.Label(window, text=f"Force {i+1} Angle:")
        angle_label.pack()

        angle_entry = ttk.Entry(window)
        angle_entry.pack()

        distance_label = ttk.Label(window, text=f"Force {i+1} Distance from Origin:")
        distance_label.pack()

        distance_entry = ttk.Entry(window)
        distance_entry.pack()

        # Append the entry fields to the input_fields list
        input_fields.append((magnitude_entry, angle_entry, distance_entry))

# Function to clear the input fields
def clear_input_fields():
    for entry_fields in input_fields:
        for entry in entry_fields:
            entry.delete(0, tk.END)

# Function to retrieve the input values
def retrieve_input_values():
    input_values = []
    for entry_fields in input_fields:
        magnitude = entry_fields[0].get()
        angle = entry_fields[1].get()
        distance = entry_fields[2].get()

        input_values.append((magnitude, angle, distance))

    # Print the retrieved input values
    for item in input_values:
        print(item)

# Create a submit button
submit_button = ttk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Create a button to retrieve the input values
retrieve_button = ttk.Button(window, text="Retrieve Values", command=retrieve_input_values)
retrieve_button.pack()

# Start the main event loop
window.mainloop()

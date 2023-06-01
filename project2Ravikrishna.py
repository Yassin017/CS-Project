# Import the necessary modules
import tkinter as tk
from tkinter import ttk


def submit():
    # Retrieve the number of forces from the entry field
    num_forces = int(num_forces_entry.get())

    # Clear the previous input fields
    clear_input_fields(input_fields)

    # Create input fields for each force
    for i in range(num_forces):
        # Create labels and entry fields for magnitude, angle, and distance
        magnitude_label = ttk.Label(window, text=f"Force {i+1} Magnitude:")
        magnitude_label.grid(column=0, row=i + 2, padx=10, pady=10)

        magnitude_var = tk.IntVar()
        magnitude_slider = ttk.Scale(window, from_=0, to=100, orient="horizontal", variable=magnitude_var)
        magnitude_slider.grid(column=1, row=i + 2, padx=10, pady=10)

        magnitude_entry = ttk.Entry(window, textvariable=magnitude_var)
        magnitude_entry.grid(column=2, row=i + 2, padx=10, pady=10)

        angle_label = ttk.Label(window, text=f"Force {i+1} Angle:")
        angle_label.grid(column=3, row=i + 2, padx=10, pady=10)

        angle_var = tk.IntVar()
        angle_slider = ttk.Scale(window, from_=0, to=360, orient="horizontal", variable=angle_var)
        angle_slider.grid(column=4, row=i + 2, padx=10, pady=10)

        angle_entry = ttk.Entry(window, textvariable=angle_var)
        angle_entry.grid(column=5, row=i + 2, padx=10, pady=10)

        distance_label = ttk.Label(window, text=f"Force {i+1} Distance from Origin:")
        distance_label.grid(column=6, row=i + 2, padx=10, pady=10)

        distance_var = tk.IntVar()
        distance_slider = ttk.Scale(window, from_=0, to=100, orient="horizontal", variable=distance_var)
        distance_slider.grid(column=7, row=i + 2, padx=10, pady=10)

        distance_entry = ttk.Entry(window, textvariable=distance_var)
        distance_entry.grid(column=8, row=i + 2, padx=10, pady=10)

        # Append the entry fields to the input_fields list
        input_fields.append((magnitude_entry, angle_entry, distance_entry))

    # Create the Retrieve button
    retrieve_button = ttk.Button(window, text="Retrieve", command=retrieve_input_values)
    retrieve_button.grid(column=4, row=num_forces + 3, padx=10, pady=10)

    # Update the Submit button command
    submit_button.configure(command=submit)


# Function to clear the input fields
def clear_input_fields(input_fields):
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


# Create the main window
window = tk.Tk()
window.title("Force Input")

# Create a label and entry field for the number of forces
num_forces_label = ttk.Label(window, text="Number of Forces:")
num_forces_label.grid(column=0, row=0, padx=10, pady=10)

num_forces_entry = ttk.Entry(window)
num_forces_entry.grid(column=1, row=0, padx=10, pady=10)

# Create the Submit button
submit_button = ttk.Button(window, text="Submit", command=submit)
submit_button.grid(column=2, row=0, padx=10, pady=10)

# Initialize the input_fields list
input_fields = []

# Start the main event loop
window.mainloop()

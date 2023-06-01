import PySimpleGUI as sg

def open_input_window(values):
    num_forces = int(values['-NUM_FORCES-'])
    num_moments = int(values['-NUM_MOMENTS-'])

    force_layout = [
        [sg.Text('Force Magnitude'), sg.Text('Force Angle'), sg.Text('Force Position')]
    ]
    force_layout += [
        [sg.InputText(key=f'-FORCE_MAGNITUDE_{i}-'), sg.InputText(key=f'-FORCE_ANGLE_{i}-'), sg.InputText(key=f'-FORCE_POSITION_{i}-')]
        for i in range(num_forces)
    ]

    moment_layout = [
        [sg.Text('Moment Value'), sg.Text('Moment Position')]
    ]
    moment_layout += [
        [sg.InputText(key=f'-MOMENT_VALUE_{i}-'), sg.InputText(key=f'-MOMENT_POSITION_{i}-')]
        for i in range(num_moments)
    ]

    layout = [
        [sg.Text('Forces')],
        *force_layout,
        [sg.Text('Moments')],
        *moment_layout,
        [sg.Button('Save')]
    ]

    input_window = sg.Window('Input Window', layout)

    while True:
        event, input_values = input_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Save':
            break

    input_window.close()

    forces = [[float(input_values[f'-FORCE_MAGNITUDE_{i}-']), float(input_values[f'-FORCE_ANGLE_{i}-']), float(input_values[f'-FORCE_POSITION_{i}-'])] for i in range(num_forces)]
    moments = [[float(input_values[f'-MOMENT_VALUE_{i}-']), float(input_values[f'-MOMENT_POSITION_{i}-'])] for i in range(num_moments)]
    print(forces,moments)
    sg.popup('Input Saved', 'Input data has been saved.')

    

    # You can further process the forces and moments lists here
    # Or pass them to your beam analysis function for further calculations

layout = [
    [sg.Text('Number of Forces'), sg.Input(key='-NUM_FORCES-')],
    [sg.Text('Number of Moments'), sg.Input(key='-NUM_MOMENTS-')],
    [sg.Button('Open Input Window', key='-OPEN_INPUT-')]
]

window = sg.Window('Beam Analysis Tool', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-OPEN_INPUT-':
        open_input_window(values)


window.close()



   


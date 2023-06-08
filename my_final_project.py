import PySimpleGUI as sg


#we are creating a input window
def open_input_window(values):
    num_forces = int(values['-NUM_FORCES-'])
    num_moments = int(values['-NUM_MOMENTS-'])

    #we are creating a input window that take values of all inputs
    #we are creating slider for every function
    force_layout = []
    for i in range(num_forces):
        force_layout += [
            [sg.Text('Force Magnitude')],
            [sg.Slider(range=(-100, 100), default_value=0, orientation='h', key=f'-FORCE_MAGNITUDE_{i}-',
                       enable_events=True)],
            [sg.Input(size=(6, 1), key=f'-FORCE_MAGNITUDE_VALUE_{i}-', enable_events=True)],
            [sg.Text('Force Angle')],
            [sg.Slider(range=(0, 360), default_value=0, orientation='h', key=f'-FORCE_ANGLE_{i}-', enable_events=True)],
            [sg.Input(size=(6, 1), key=f'-FORCE_ANGLE_VALUE_{i}-', enable_events=True)],
            [sg.Text('Force Position')],
            [sg.Slider(range=(-10, 10), default_value=0, orientation='h', key=f'-FORCE_POSITION_{i}-',
                       enable_events=True)],
            [sg.Input(size=(6, 1), key=f'-FORCE_POSITION_VALUE_{i}-', enable_events=True)]
        ]

    moment_layout = [
        [sg.Text('Moment Value'), sg.Text('Moment Position')]
    ]
    moment_layout += [
        [
            sg.Slider(range=(-100, 100), default_value=0, orientation='h', key=f'-MOMENT_VALUE_{i}-',
                      enable_events=True),
            sg.Input(size=(6, 1), key=f'-MOMENT_VALUE_VALUE_{i}-', enable_events=True),
            sg.Slider(range=(-10, 10), default_value=0, orientation='h', key=f'-MOMENT_POSITION_{i}-',
                      enable_events=True),
            sg.Input(size=(6, 1), key=f'-MOMENT_POSITION_VALUE_{i}-', enable_events=True)
        ]
        for i in range(num_moments)
    ]

    layout = [
        [sg.Text('Forces')],
        *force_layout,
        [sg.Text('Moments')],
        *moment_layout,
        [sg.Button('Save', button_color=('white', 'blue'), key='-SAVE-', size=(10, 1), pad=((0, 10), (0, 10))),
         ]
    ]

    input_window = sg.Window('Input Window', layout)
    #we are creating conditions for every function
    while True:
        event, input_values = input_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == '-SAVE-':
            save_file(input_values)
        elif event == '-NEW_FILE-':
            new_file()
        
            
        for i in range(num_forces):
            force_magnitude_value = input_values[f'-FORCE_MAGNITUDE_{i}-']
            force_angle_value = input_values[f'-FORCE_ANGLE_{i}-']
            force_position_value = input_values[f'-FORCE_POSITION_{i}-']
            input_window[f'-FORCE_MAGNITUDE_VALUE_{i}-'].update(force_magnitude_value)
            input_window[f'-FORCE_ANGLE_VALUE_{i}-'].update(force_angle_value)
            input_window[f'-FORCE_POSITION_VALUE_{i}-'].update(force_position_value)
        for i in range(num_moments):
            moment_value_value = input_values[f'-MOMENT_VALUE_{i}-']
            moment_position_value = input_values[f'-MOMENT_POSITION_{i}-']
            input_window[f'-MOMENT_VALUE_VALUE_{i}-'].update(moment_value_value)
            input_window[f'-MOMENT_POSITION_VALUE_{i}-'].update(moment_position_value)

    input_window.close()

    forces = [
        [
            float(input_values[f'-FORCE_MAGNITUDE_{i}-']),
            float(input_values[f'-FORCE_ANGLE_{i}-']),
            float(input_values[f'-FORCE_POSITION_{i}-'])
        ]
        for i in range(num_forces)
    ]

    moments = [
        [
            float(input_values[f'-MOMENT_VALUE_{i}-']) if input_values[f'-MOMENT_VALUE_{i}-'] else 0.0,
            float(input_values[f'-MOMENT_POSITION_{i}-']) if input_values[f'-MOMENT_POSITION_{i}-'] else 0.0
        ]
        for i in range(num_moments)
    ]

    print(forces, moments)
    sg.popup('Input Saved', 'Inputs are saved and are being processed for Calculations')



def save_file(values):
    filepath = sg.popup_get_file('Save File', save_as=True, default_extension='.txt')
    if filepath:
        with open(filepath, 'w') as file:
            for key, value in values.items():
                print(f"{key}: {value}")  #we are printing the key-value pairs
                file.write(f"{key}: {value}\n")
        sg.popup('File Saved', f'File saved at:\n\n{filepath}')


    
layout = [
    [sg.Text('Number of Forces'), sg.Input(key='-NUM_FORCES-')],
    [sg.Text('Number of Moments'), sg.Input(key='-NUM_MOMENTS-')],
    [sg.Button('Open Input Window', key='-OPEN_INPUT-', size=(20, 1))],
    ]

window = sg.Window('Beam Analysis Tool', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-OPEN_INPUT-':
        window.hide()  # we are hiding the first window
        open_input_window(values)
        window.un_hide()  # we are show the first window again after the second window is closed
   

window.close()

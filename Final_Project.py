import PySimpleGUI as sg
import math
import matplotlib.pyplot as mpl


def open_input_window(values):
    num_forces = int(values['-NUM_FORCES-'])
    num_moments = int(values['-NUM_MOMENTS-'])

    force_layout = [
        [sg.Text('Force Magnitude(N)                                                      '),
         sg.Text('Force Angle(deg)                                                            '),
         sg.Text('Force Position(m)')]
    ]
    force_layout += [
        [sg.InputText(key=f'-FORCE_MAGNITUDE_{i}-'), sg.InputText(key=f'-FORCE_ANGLE_{i}-'),
         sg.InputText(key=f'-FORCE_POSITION_{i}-')]
        for i in range(num_forces)
    ]

    moment_layout = [
        [sg.Text('Moment Value(Nm)                                                        '),
         sg.Text('Moment Position(m)')]
    ]
    moment_layout += [
        [sg.InputText(key=f'-MOMENT_VALUE_{i}-'), sg.InputText(key=f'-MOMENT_POSITION_{i}-')]
        for i in range(num_moments)
    ]

    layout = [
        [sg.Text('Length of the Beam'), sg.Input(key='-LENGTH-', size=(10, 1))],
        [sg.Text('Position of Support 1'), sg.Input(key='-POSITION_SUPPORT1-', size=(10, 1))],
        [sg.Text('Position of Support 2'), sg.Input(key='-POSITION_SUPPORT2-', size=(10, 1))],
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
    global length, position_support1, position_support2, forces, moments
    length = float(input_values['-LENGTH-'])
    position_support1 = float(input_values['-POSITION_SUPPORT1-'])
    position_support2 = float(input_values['-POSITION_SUPPORT2-'])
    forces = [[float(input_values[f'-FORCE_MAGNITUDE_{i}-']), float(input_values[f'-FORCE_ANGLE_{i}-']),
               float(input_values[f'-FORCE_POSITION_{i}-'])] for i in range(num_forces)]
    moments = [[float(input_values[f'-MOMENT_VALUE_{i}-']), float(input_values[f'-MOMENT_POSITION_{i}-'])]
               for i in range(num_moments)]

    sg.popup('Calculating results...', 'Continue to view graph')


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

beamspan = length
r1 = position_support1
r2 = position_support2

PL = []  # to store point loads as (dist,xcomp,ycomp)
for i in forces:
    dist = i[2]
    mag = i[0]
    ang = i[1]

    xcomp = -mag * math.cos((ang / 180) * math.pi)
    ycomp = -mag * math.sin((ang / 180) * math.pi)
    PL.append((dist, xcomp, ycomp))

x = []  # x contains values for plotting x axis (each metre into 100 divisions)
c = 0
for i in range(0, int(beamspan * 100) + 1):
    if c <= 10:
        x.append(c)
    c += 1 / 100

support_rns = [0, 0, 0]  # in the form of [vr1,vr2,hr1]


def plreactions(n):
    dist = PL[n][0]  # Location of point load

    xcomp = PL[n][1]
    ycomp = PL[n][2]

    arm_pl = r1 - dist  # perp. distance of pl about r1
    mpl = ycomp * arm_pl  # Moment about A - clockwise (+ve) -sign change at end
    arm_r2 = r2 - r1  # perp. distance of r2 about r1
    vr2 = mpl / arm_r2
    vr1 = -ycomp - vr2
    hr1 = -xcomp
    return vr1, vr2, hr1


PL_store = []  # stores reactions of each point load

if PL != []:
    for i in range(len(PL)):
        vr1, vr2, hr1 = plreactions(i)

        PL_store.append([PL[i], [vr1, vr2, hr1]])  # Store reactions by each PL
        support_rns[0] += vr1
        support_rns[1] += vr2
        support_rns[2] += hr1

PM = moments
# PM stored as list of [val,dist]


def pmreaction(n):
    val = PM[n][0]  # value of moment
    dist = PM[n][1]  # dist from origin

    arm_r2 = r2 - r1
    vr2 = val / arm_r2  # Vertical reaction at r2
    vr1 = -vr2
    return vr1, vr2


PM_store = []  # stores reactions of each point moment

if PM != []:
    for i in range(len(PM)):
        vr1, vr2 = pmreaction(i)
        PM_store.append([PM[i], [vr1, vr2]])  # Store reactions by each PM
        support_rns[0] += vr1
        support_rns[1] += vr2


def sm_from_PL(n):
    dist = PL[n][0]  # dist from origin of PL
    ycomp = PL[n][2]  # only taking y component of force
    vr1 = PL_store[n][1][0]
    vr2 = PL_store[n][1][1]
    SF_values = [0] * len(x)
    BM_values = [0] * len(x)
    for i in range(len(x)):
        s = 0
        m = 0

        if x[i] > dist:
            # shear and moment from PL only
            s = s + ycomp
            m = m - ycomp * (x[i] - dist)

        if x[i] > r1:
            s = s + vr1  # shear and moment from r1 and r2 (separately)
            m = m - vr1 * (x[i] - r1)
        if x[i] > r2:
            s = s + vr2
            m = m - vr2 * (x[i] - r2)

        SF_values[i] = s
        BM_values[i] = m  # store f and bm at each point

    return SF_values, BM_values


shear_total = []
moment_total = []
if PL != []:
    for i in range(len(PL)):
        s, m = sm_from_PL(i)
        shear_total.append(s)  # Store shear force record for each point load
        moment_total.append(m)  # Store bending moment record for each point load


def sm_from_PM(n):
    dist = PM[n][0]  # dist from origin of PM
    val = PM[n][1]  # magnitude of moment
    vr1 = PM_store[n][1][0]
    vr2 = PM_store[n][1][1]
    SF_values = [0] * len(x)
    BM_values = [0] * len(x)
    for i in range(len(x)):
        s = 0
        m = 0

        if x[i] > dist:
            # moment from PM only (does not directly give shear)
            m = m - val

        if x[i] > r1:
            s = s + vr1  # shear and moment from r1 and r2 (separately)
            m = m - vr1 * (x[i] - r1)
        if x[i] > r2:
            s = s + vr2
            m = m - vr2 * (x[i] - r2)

        SF_values[i] = s
        BM_values[i] = m  # store f and bm at each point

    return SF_values, BM_values


if PM != []:
    for i in range(len(PM)):
        s, m = sm_from_PM(i)
        shear_total.append(s)  # Store shear force record for each point load
        moment_total.append(m)  # Store bending moment record for each point load


# to sum up the SF and BM of all forces and moments
shear_sum = [0] * len(x)
moment_sum = [0] * len(x)

for dx in range(len(x)):
    ctr = 0
    for i in range(len(shear_total)):
        ctr += shear_total[i][dx]
    shear_sum[dx] = ctr

for dx in range(len(x)):
    ctr = 0
    for i in range(len(moment_total)):
        ctr += moment_total[i][dx]
    moment_sum[dx] = ctr

print_reactions = '''
The vertical reaction at support R1 is ''' + str(round(support_rns[0], 2)) + '''N
The vertical reaction at support R2 is ''' + str(round(support_rns[1], 2)) + '''N
The horizontal reaction at support R1 is ''' + str(round(support_rns[2], 2)) + '''N'''

for i in range(len(moment_sum)):
    moment_sum[i] *= -1

range_shear = max(shear_sum) - min(shear_sum)
range_moment = max(moment_sum) - min(moment_sum)

fig, (ax1, ax2) = mpl.subplots(2, 1, sharex=True)
ax1.plot(x, shear_sum, color='blue')  # defining both plots with shared x
ax2.plot(x, moment_sum, color='red')

mpl.xlabel('Length (m)')
ax1.set_ylabel('Shear Force (N)')  # setting labels for each axes
ax1.set_title('Shear Force diagram')
ax2.set_ylabel('Bending Moment (Nm)')
ax2.set_title('Bending Moment diagram')
fig.suptitle('Beam Analysis Result', fontsize = 16)

fig.text(
    0.5,
    0.1,
    print_reactions,
    ha='center',
    va='center',
    fontsize=12
)


ax1.set_ylim(max(shear_sum) + range_shear * 0.25, min(shear_sum) - range_shear * 0.25)
ax2.set_ylim(max(moment_sum) + range_moment * 0.25, min(moment_sum) - range_moment * 0.25)
ax1.grid()
ax2.grid()

mpl.subplots_adjust(hspace = 0.80, bottom=0.30)  #spacing parameters in subplot
mpl.show()

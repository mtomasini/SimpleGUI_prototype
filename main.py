import PySimpleGUI as sg

"""This script produces and saves a series of plots that will then be accessed by the GUI at a later stage. 
    
"""

import PySimpleGUI as sg
import os.path
from plots import save_damped_plot, save_normal_plot

sg.theme('LightBlue3')

parameters_column = [
    [
        sg.Text("This GUI allows to run a script and output the results of the script in an image viewer.", font=50),
    ],
    [
        sg.Text("The script calculates the trajectory of an oscillator. Try changing the parameters below!", font=50),
    ],
    [
        sg.Text("Frequency of oscillation", font=35),
        sg.Slider(
            range=(0.1, 20.0),
            resolution=0.1,
            default_value=10,
            size=(50,30),
            orientation='horizontal',
            font=('Helvetica', 20), 
            key="-FREQ-"
        ),
    ],
    [
        sg.Text("Phase of oscillation", font=35),
        sg.Slider(
            range=(0, 10),
            resolution=0.1,
            default_value=0,
            size=(50,30),
            orientation='horizontal',
            font=('Helvetica', 20), 
            key="-PHASE-"
        ),
    ],
    [
        sg.Text("Damping factor", font=35),
        sg.Slider(
            range=(0, 10),
            resolution=0.1,
            default_value=0,
            size=(50,30),
            orientation='horizontal',
            font=('Helvetica', 20), 
            key="-DAMP-"
        ),
    ],
    [
        sg.Button("Calculate oscillation!", size=(30,2)),
        sg.Cancel(size=(10, 2))
    ]
]

image_viewer_column = [
    [sg.Combo(
        ['Harmonic oscillator', 'Damped oscillator'], 
        default_value="Harmonic oscillator",
        key="-MODE-", font=35, auto_size_text=True)
    ],
    # [
    #     sg.Radio('Harmonic oscillator', "-MODE-", default=True), 
    #     sg.Radio('Damped oscillator', "-MODE-")
    # ],
    [sg.Image(key="-IMAGE-", size=(800, 800))],
]

layout = [
    [
        sg.Column(parameters_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),    
    ]
]

window = sg.Window("Script GUI wrapper", layout, margins=(50, 50), location=(100, 100))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "Calculate oscillation!":
        freq = values["-FREQ-"]
        phase = values["-PHASE-"]
        damp = values["-DAMP-"]
        mode = values["-MODE-"]
        
        try:
            if mode == "Harmonic oscillator":
                save_normal_plot(freq, phase)
                filename = "./Plots/normal_oscillation.png"
            elif mode == "Damped oscillator":
                save_damped_plot(freq, phase, damp)
                filename = "./Plots/damped_oscillation.png"
        except:
            print("Something went wrong")
            pass
            
        try:
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
    
        
window.close()
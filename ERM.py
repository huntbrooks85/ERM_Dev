#-----------------------------------------------------------------------#
# ERM v0.1
# Sad Astrophysics Students
#-----------------------------------------------------------------------#
print('------------------------------------------------')
print('               Exoplanet Ring Model             ')
print('------------------------------------------------')
import PySimpleGUI as sg

sg.theme('BlueMono')

#Makes the layout of the WRAP program, providing a place to put the ra, dec, and radius the output file name and which catalogs needs to be used
layout = [  [sg.Text('Exoplanet Ring Model', justification='center', size=(60, 1), font = ('Phosphate', 35))],
            [sg.Text('Output File Name', size=(50, 1), justification='center', font = ('Times New Roman', 22))],
            [sg.InputText(key = 'output', font = ('Times New Roman', 15), size = (70, 3), justification='center')],
            [sg.Text('Variables:', justification='center', size=(50, 1), font = ('Times New Roman', 25))],
            [sg.Text('Ring Albedo', justification = 'center', size = (30), font = ('Times New Roman', 14)), sg.Text('Ring Density', justification = 'center', size = (30), font = ('Times New Roman', 14))],
            [sg.InputText(key = 'r_a', font = ('Times New Roman', 15), size = (25, 1)), sg.InputText(key = 'r_d', font = ('Times New Roman', 15), size = (25, 1))],
            [sg.Text('Ring Width', justification = 'center', size = (30), font = ('Times New Roman', 14)), sg.Text('Ring Thickness', justification = 'center', size = (30), font = ('Times New Roman', 14))],
            [sg.InputText(key = 'r_w', font = ('Times New Roman', 15), size = (25, 1)), sg.InputText(key = 'r_t', font = ('Times New Roman', 15), size = (25, 1))],
            [sg.Text('Planet Albedo', justification = 'center', size = (30), font = ('Times New Roman', 14)), sg.Text('Planet Obliquity', justification = 'center', size = (30), font = ('Times New Roman', 14))],
            [sg.InputText(key = 'p_a', font = ('Times New Roman', 15), size = (25, 2)), sg.InputText(key = 'p_o', font = ('Times New Roman', 15), size = (25, 2))],
            [sg.Text('Planet Radius', justification = 'center', size = (30), font = ('Times New Roman', 14)), sg.Text('Planet-Star Distance', justification = 'center', size = (30), font = ('Times New Roman', 14))],
            [sg.InputText(key = 'p_r', font = ('Times New Roman', 15), size = (25, 2)), sg.InputText(key = 'D', font = ('Times New Roman', 15), size = (25, 2))],
            [sg.Text('Planet Eccentricity', justification = 'center', size = (30), font = ('Times New Roman', 14)), sg.Text('Orbital Period', justification = 'center', size = (30), font = ('Times New Roman', 14))],
            [sg.InputText(key = 'p_e', font = ('Times New Roman', 15), size = (25, 2)), sg.InputText(key = 'P', font = ('Times New Roman', 15), size = (25, 2))],
            [sg.Text('Solar Constant', justification = 'center', size = (30), font = ('Times New Roman', 14)), sg.Text('Atm. Composition Parameter', justification = 'center', size = (30), font = ('Times New Roman', 14))],
            [sg.InputText(key = 'SC', font = ('Times New Roman', 15), size = (25, 2)), sg.InputText(key = 'amp', font = ('Times New Roman', 15), size = (25, 2))],
            [sg.Button('Run ERM', size = (22), button_color = 'green'), sg.Button('Help', size = (22), button_color = 'orange'), sg.Button('Close ERM', size = (22), button_color = 'red')]]

#Makes the windows in the layout from above
window = sg.Window('ERM', layout, size = (450, 520), grab_anywhere=True)

while True:
    #Opens the window
    event, values = window.read()

    #Runs the ERM function if the 'Run ERM' button is pressed
    if event in (None, 'Run ERM'): 
        #Put the function for the equations
        pass


    #Closes WRAP if the 'Close WRAP' button is pressed
    if event in (None, 'Close ERM'):
        print('------------------------------------------------')
        print('            Thank you for using ERM!            ')
        print('------------------------------------------------')
        print('')
        break

    #Provides the user with the authors information if the 'Help' button is pressed
    if event in (None, 'Help'):
        print('                                               ')
        print('          Thank you for using ERM!             ')
        print('-----------------------------------------------')
        print('              Authors Contact:                 ')
        print('           mark.salvatore@nau.edu              ')
        print('               nab393@nau.edu                  ')
        print('               hcb98@nau.edu                   ')
        print('              nat257@nau.edu                   ')
        print('               nqf4@nau.edu                    ')
        print('-----------------------------------------------')
        print('                                               ')

window.close()
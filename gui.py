import PySimpleGUI as sg

import main
import stego

def hide(operation):
    # Changing the color theme of the GUI
    sg.theme('Topanga')
    # Valid image formats
    validFormats = (".png", ".png2")

    # Defining the layout of the window with the secret message and the image
    layout = [
        [sg.Text('Enter the Seed:')],
        [sg.Text('Seed', size=(15, 1)), sg.InputText(key='seed')],
        [sg.Text('Please select an image')],
        [sg.Text('Image:', size=(8, 1)), sg.Input(key='img'), sg.FileBrowse()],
        [sg.Text('Output Folder:'), sg.Input(key='folder'), sg.FolderBrowse(target='folder')],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Hide Face', layout)
    # Reading values of the text fields and checking if we cancel the program
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        window.close()
        exit()

    # Checking if all the fields were completed in order to run the program
    while values['seed'] == '' or values['img'] == '' or values['folder'] == '' \
            or not values['img'].endswith(validFormats):
        # If some field was empty pop up an error
        if event == 'Submit':
            sg.popup('Error: You must enter all parameters and image should be', validFormats)
        # If you cancel the program, exit
        else:
            window.close()
            exit()

        # Read the values of the fields again
        event, values = window.read()

    # We save the data of the fields and close the window
    data = values['seed']
    file_encode = values['img']
    outputPath = values['folder']

    window.close()

    return data, file_encode, outputPath

def init():
    # GUI Theme Color
    sg.theme('Topanga')
    # Defining the layout of the window with the secret message and the image
    layout3 = [
        [sg.Text('Face Obfuscation Tool. Obfuscate or reverse ')],
        [[sg.Button('Obfuscate')], [sg.Button('Reverse')]]
    ]
    # Assign layout to a window
    window3 = sg.Window('Main Menu', layout3)
    # Reading values of the text fields and checking if we cancel the program
    event3, values2 = window3.read()
    if event3 in (sg.WIN_CLOSED, 'Cancel'):
        print("Button cancel was pressed")
        window3.close()
        exit()
    if event3 == 'Obfuscate':
        window3.close()
        # Operator == True: Obfuscation operation
        # Operator == False: De-Obfuscation operation
        operation = True
        seed, file_encode, outputPath = hide(operation)
        code = main.manager(seed, file_encode, outputPath, operation)
        return code
    if event3 == 'Reverse':
        window3.close()
        # Operator == True: Obfuscation operation
        # Operator == False: De-Obfuscation operation
        operation = False
        seed, file_encode, outputPath = hide(operation)
        code = main.manager(seed, file_encode, outputPath, operation)
        return code

import PySimpleGUI as sg
from firebase_storage import *
from firebase_firestore import *
from system import *

# initialize software component
set_system_time()
storageInitialize()
firestoreInitialize()
my_camera = cameraInitialize()


# gui layouts
sg.theme('LightPurple')
layout_take_picture = [
    [sg.Button('Take Picture')],
    [sg.Exit()]
]
layout_fields = [
    [sg.Text('Type', size=(15,1)), 
        sg.Radio('SHIRT', "RADIO_TYPE", default=False, key='shirt'), 
        sg.Radio('SKIRT', "RADIO_TYPE", default=False, key='skirt'), 
        sg.Radio('PANTS', "RADIO_TYPE", default=False, key='pants')],
    [sg.Text('Size', size=(15,1)), 
        sg.Radio('S', "RADIO_SIZE", default=False, key='s'), 
        sg.Radio('M', "RADIO_SIZE", default=False, key='m'), 
        sg.Radio('L', "RADIO_SIZE", default=False, key='l')],
    [sg.Text('Color', size=(15,1)), 
        sg.Radio('RED', "RADIO_COLOR", default=False, key='red'), 
        sg.Radio('GREEN', "RADIO_COLOR", default=False, key='green'), 
        sg.Radio('BLUE', "RADIO_COLOR", default=False, key='blue')],
    [sg.Text('Price', size=(15,1)), 
        sg.Radio('10', "RADIO_PRICE", default=False, key='10'), 
        sg.Radio('20', "RADIO_PRICE", default=False, key='20'), 
        sg.Radio('30', "RADIO_PRICE", default=False, key='30')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window_take_picture = sg.Window('Take Picture', layout_take_picture)
window_fields = sg.Window('Select Info Fields', layout_fields)

# gui functions
def gui_clear_input():
    for key in values:
        window_fields[key](False)

def gui_take_pic(my_camera):
    print ('take pic')
    id, img_url = takePictureAndUpload(my_camera)
    return id , img_url

while True:
    # first window
    event, values = window_take_picture.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Take Picture':
        print("1")
        id , img_url = gui_take_pic(my_camera)

    # second window
    event, values = window_fields.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        gui_clear_input()
    if event == 'Submit':
        checked_values = [k for k,v in values.items() if v == True]
        print(checked_values)
        data = {
            'type': checked_values[0],
            'size': checked_values[1],
            'color': checked_values[2],
            'price': checked_values[3],
            'image': img_url
        }
        print(data)
        firestoreAddDocument(data, id)
        sg.popup('Data saved!')
        gui_clear_input()

window_take_picture.close()
window_fields.close()

my_camera.close()

print("done")
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
    [sg.Button('Take Picture', size=(20,2), font=("calibri", 58))],
    [sg.Exit(size=(20,2), font=("calibri", 58))]
]
layout_fields = [
    [sg.Text('Type', size=(15,1),font=("calibri", 20)), 
        sg.Radio('SHIRT', "RADIO_TYPE", default=False, key='shirt',font=("calibri", 20)), 
        sg.Radio('SKIRT', "RADIO_TYPE", default=False, key='skirt',font=("calibri", 20)), 
        sg.Radio('PANTS', "RADIO_TYPE", default=False, key='pants',font=("calibri", 20))],
    [sg.Text('Size', size=(15,1),font=("calibri", 20)), 
        sg.Radio('S', "RADIO_SIZE", default=False, key='s',font=("calibri", 20)), 
        sg.Radio('M', "RADIO_SIZE", default=False, key='m',font=("calibri", 20)), 
        sg.Radio('L', "RADIO_SIZE", default=False, key='l',font=("calibri", 20))],
    [sg.Text('Color', size=(15,1),font=("calibri", 20)), 
        sg.Radio('RED', "RADIO_COLOR", default=False, key='red',font=("calibri", 20)), 
        sg.Radio('GREEN', "RADIO_COLOR", default=False, key='green',font=("calibri", 20)), 
        sg.Radio('BLUE', "RADIO_COLOR", default=False, key='blue',font=("calibri", 20))],
    [sg.Text('Price', size=(15,1),font=("calibri", 20)), 
        sg.Radio('10', "RADIO_PRICE", default=False, key='10',font=("calibri", 20)), 
        sg.Radio('20', "RADIO_PRICE", default=False, key='20',font=("calibri", 20)), 
        sg.Radio('30', "RADIO_PRICE", default=False, key='30',font=("calibri", 20))],
    [sg.Submit(font=("calibri", 20)), sg.Button('Clear',font=("calibri", 20)), sg.Exit(font=("calibri", 20))]
]

window_take_picture = sg.Window('Take Picture', layout_take_picture, size=(800, 480), element_justification='c')
window_fields = sg.Window('Select Info Fields', layout_fields, size=(800, 480))

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
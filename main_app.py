#import PySimpleGUI as sg
from system import *
from gui_utils import *
from firebase_storage import *
from firebase_firestore import *

# initialize software component
systemInitialize()
storageInitialize()
firestoreInitialize()
my_camera = cameraInitialize()

window_fields = make_window_fields()
window_take_picture = make_window_take_picture()

while True:

    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
   
    # first window
    elif window == window_take_picture:
        if event == 'Take Picture':
            print("1")
            id , img_url = gui_take_pic(my_camera)
            # switch windows
            window_take_picture.hide()
            window_fields.un_hide()
            # move cursor
            os.system("xdotool mousemove 800 600") 

    # second window
    elif window == window_fields:
        if event == 'Clear':
            gui_clear_input(window_fields, values)
            # move cursor
            os.system("xdotool mousemove 800 600") 
        if event == 'Submit':
            checked_values = [k for k,v in values.items() if v == True]
            if len(checked_values) != num_of_fields:
                sg.popup('please choose all fields')
            else:
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
                gui_clear_input(window_fields, values)
                # switch windows 
                window_fields.hide()
                window_take_picture.un_hide()
            # move cursor
            os.system("xdotool mousemove 800 600") 

window_take_picture.close()
window_fields.close()

my_camera.close()

print("done")
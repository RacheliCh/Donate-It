from system import *
from gui_utils import *
from firebase_storage import *
from firebase_firestore import *

# initialize software component
systemInitialize()
storageInitialize()
firestoreInitialize()
my_camera = systemCameraInitialize()

window_fields = guiMakeWindowFields()
window_approve_picture = guiMakeWindowApprovePicture()
window_take_picture = guiMakeWindowTakePicture()

while True:

    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
   
    # first window
    elif window == window_take_picture:
        if event == 'Take Picture':
            id = guiTakePicture(my_camera)
            image_name = id + ".jpg"
            guiUpdatePicToDisplay(window_approve_picture, image_name)
            # switch windows
            window_approve_picture.un_hide()
            window_take_picture.hide()
            # move cursor
            os.system("xdotool mousemove 800 600") 

    # second window
    elif window == window_approve_picture:
        if event == 'Confirm':
            img_url = guiUploadPicture(id)
            # switch windows
            window_fields.un_hide()
            window_approve_picture.hide()
            # move cursor
            os.system("xdotool mousemove 800 600")
        elif event == 'Try Again':
            systemRemoveFile(image_name)
            # switch windows
            window_take_picture.un_hide()
            window_approve_picture.hide()
            # move cursor
            os.system("xdotool mousemove 800 600")
    
    # third window
    elif window == window_fields:
        if event == 'Clear':
            guiClearInput(window_fields, values)
            # move cursor
            os.system("xdotool mousemove 800 600") 
        elif event == 'Submit':
            checked_values = [k for k,v in values.items() if v == True]
            if len(checked_values) != num_of_fields:
                sg.popup('please choose all fields', font=("calibri", 20), title = ' ')
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
                sg.popup('Data saved!', font=("calibri", 20), title = ' ')
                
                message_to_print = "ITEM ID: " + id + "\n\n" + checked_values[0] + "\n" + checked_values[1] + "\n" + checked_values[2] + "\n\n" + checked_values[3] + " NIS" 
                printReceipt(message_to_print)
                
                guiClearInput(window_fields, values)
                
                # switch windows
                window_take_picture.un_hide() 
                window_fields.hide()
            
            # move cursor
            os.system("xdotool mousemove 800 600") 

window_take_picture.close()
window_fields.close()

my_camera.close()

print("done")
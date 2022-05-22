import PySimpleGUI as sg
import io
from PIL import Image
from system import *
from firebase_storage import *
from firebase_firestore import *


### gui layouts ###

sg.theme('LightPurple')
num_of_fields = 4

layout_take_picture = [
    [sg.Button('Take Picture', size=(20,2), font=("calibri", 58))],
    [sg.Exit(size=(20,2), font=("calibri", 58))]
]

layout_approve_picture = [
    [sg.Image(key='IMAGE')],
    [sg.Button('Confirm', size=(10,2), font=("calibri", 25)),
     sg.Button('Try Again', size=(10,2), font=("calibri", 25))]
]

layout_fields = [
    [sg.Text('Type', size=(15,1),font=("calibri", 20)), 
        sg.Radio('SHIRT', "RADIO_TYPE", default=False, key='SHIRT',font=("calibri", 20)), 
        sg.Radio('SKIRT', "RADIO_TYPE", default=False, key='SKIRT',font=("calibri", 20)), 
        sg.Radio('PANTS', "RADIO_TYPE", default=False, key='PANTS',font=("calibri", 20))],
    [sg.Text('Size', size=(15,1),font=("calibri", 20)), 
        sg.Radio('S', "RADIO_SIZE", default=False, key='S',font=("calibri", 20)), 
        sg.Radio('M', "RADIO_SIZE", default=False, key='M',font=("calibri", 20)), 
        sg.Radio('L', "RADIO_SIZE", default=False, key='L',font=("calibri", 20))],
    [sg.Text('Color', size=(15,1),font=("calibri", 20)), 
        sg.Radio('RED', "RADIO_COLOR", default=False, key='RED',font=("calibri", 20)), 
        sg.Radio('GREEN', "RADIO_COLOR", default=False, key='GREEN',font=("calibri", 20)), 
        sg.Radio('BLUE', "RADIO_COLOR", default=False, key='BLUE',font=("calibri", 20))],
    [sg.Text('Price', size=(15,1),font=("calibri", 20)), 
        sg.Radio('10', "RADIO_PRICE", default=False, key='10',font=("calibri", 20)), 
        sg.Radio('20', "RADIO_PRICE", default=False, key='20',font=("calibri", 20)), 
        sg.Radio('30', "RADIO_PRICE", default=False, key='30',font=("calibri", 20))],
    [sg.Submit(font=("calibri", 20)), sg.Button('Clear',font=("calibri", 20)), sg.Exit(font=("calibri", 20))]
]



### gui functions ###

def guiMakeWindowFields():
    return sg.Window('Select Info Fields', layout_fields, size=(800, 480), finalize=True)

def guiMakeWindowApprovePicture():
    return sg.Window('Approve Picture', layout_approve_picture, size=(800, 480), element_justification='c', finalize=True)

def guiMakeWindowTakePicture():
    return sg.Window('Take Picture', layout_take_picture, size=(800, 480), element_justification='c', finalize=True)

def guiClearInput(window, values):
    for key in values:
        window[key](False)

def guiTakePicture(my_camera):
    print ('take pic')
    id = systemTakePicture(my_camera)
    return id

# update the image displayed in the window
def guiUpdatePicToDisplay(window, image_name):
    image = Image.open(image_name)
    image.thumbnail((300, 300))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window["IMAGE"].update(data=bio.getvalue())

# upload to firebse and return the url
def guiUploadPicture(id):
    img_name = id + ".jpg"
    storageUploadImage(img_name)

    print("Image sent")
    systemRemoveFile(img_name)

    img_url = storageGetImageUrl(img_name)
    return img_url

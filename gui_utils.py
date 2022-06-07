import PySimpleGUI as sg
import io
from PIL import Image
from system import *
from firebase_storage import *
from firebase_firestore import *
import yaml
from yaml.loader import SafeLoader


# Open the yaml file and load the data
with open('/home/pi/Documents/project/Donate-It/items_config.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

### gui layouts ###

sg.theme('LightPurple')
num_of_fields = len(yaml_data.keys())

layout_take_picture = [
    [sg.Button('Show Preview', size=(20, 2), font=('calibri', 35))],
    [sg.Button('Take Picture', size=(20, 2), font=('calibri', 35))],
    [sg.Exit(size=(20, 2), font=('calibri', 35))]
]

layout_approve_picture = [
    [sg.Image(key='IMAGE')],
    [sg.Button('Confirm', size=(10, 2), font=('calibri', 25)),
     sg.Button('Try Again', size=(10, 2), font=('calibri', 25))]
]

fields_layout_list = []
for FIELD_NAME in yaml_data.keys():
    field_row_list = []
    field_row_list.append(sg.Text(FIELD_NAME, size=(7, 1), font=('calibri', 20)))
    for VALUE in yaml_data[FIELD_NAME]:
        field_row_list.append(sg.Radio(VALUE, 'RADIO_'+FIELD_NAME, default=False, key=VALUE, font=('calibri', 20)))
    fields_layout_list.append([*field_row_list])

fields_col = [
    *fields_layout_list
]

layout_fields = [
    [sg.Column(fields_col, scrollable=True, size=(800, 330))],
    [sg.Submit(font=('calibri', 20)), sg.Button('Clear', font=('calibri', 20))]
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

    systemRemoveFile(img_name)

    img_url = storageGetImageUrl(img_name)
    return img_url

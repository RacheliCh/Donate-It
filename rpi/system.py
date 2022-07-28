from picamera import PiCamera
from time import sleep
from urllib.request import urlopen
from datetime import datetime, timedelta
import os
from escpos.printer import *
from firebase_storage import *

def systemSetTime():
    res = urlopen('http://just-the-time.appspot.com/')
    # if there is no wifi the code will stop here and nothing will appear on screen
    result = res.read().strip()
    result_str = result.decode('utf-8')
    day = result_str[8:10]
    month = result_str[5:7]
    year = result_str[2:4]
    times = datetime.strptime(result_str[11:], "%H:%M:%S")
    times += timedelta(hours=3)
    times = times.strftime("%H:%M:%S")
    os.system("sudo date -s \'" + year + "-" + month + "-" + day + " " + times + "\'") 

def systemInitialize():
    systemSetTime()
    os.environ['DISPLAY']=':0.0'
    os.system("sudo chmod 777 /dev/usb/lp0")
    os.system("xdotool mousemove 800 600")

def systemPowerOff():
    os.system("sudo poweroff")

def systemCameraInitialize():
    camera = PiCamera()
    camera.framerate=30
    camera.resolution=(1080,1080)
    return camera

def systemCameraShowPreview(camera):
    camera.start_preview()
    sleep(5)
    camera.stop_preview()

# capture picture
def systemTakePicture(camera):
    now = datetime.now()
    dt = now.strftime("%d%m%y%H%M%S")
    img_name = dt + ".jpg"
    camera.capture(img_name)
    return dt

def systemRemoveFile(file_name):
    os.remove(file_name)

# def systemPrintReceipt(message):
#     os.system("echo \"" + message + "\n\n\n\" > /dev/usb/lp0")

def systemPrintLabel(item_id, info):
        """ 9600 Baud, 8N1, Flow Control Enabled """
        p = File(devfile='/dev/usb/lp0')

        p.set(align="center", width=1, height=1)
        p.text("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        p.text("\n")
        p.image("rpi/logo.png",impl="bitImageColumn")
        p.text("\n")
        p.set(align="left", width=1, height=1, text_type="B")
        p.text("ITEM ID: " + item_id)
        p.text("\n\n")
        p.set(align="left", width=1, height=1)
        p.text(info)
        p.text("\n")
        p.text("\n")
        p.set(align="center", width=1, height=1)
        p.text("To The Store:")
        p.text("\n\n")
        p.set(align="center", width=3, height=3)
        p.qr("https://donateit100.wixsite.com/donate-it/blank",native=True,size=8)
        p.set(align="center", width=1, height=1)
        p.text("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        p.text("\n\n\n")
from picamera import PiCamera
from time import sleep
from urllib.request import urlopen
from datetime import datetime, timedelta
import os
from firebase_storage import *

def systemSetTime():
    # TODO: add exception if no wifi
    res = urlopen('http://just-the-time.appspot.com/')
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

def systemCameraInitialize():
    camera = PiCamera()
    camera.framerate=30
    camera.resolution=(1080,1080)
    return camera

# capture picture
def systemTakePicture(camera):
    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    print("pushed")
    now = datetime.now()
    dt = now.strftime("%d%m%y%H%M%S")
    img_name = dt + ".jpg"
    camera.capture(img_name)
    print(img_name+" saved")
    return dt

def systemRemoveFile(file_name):
    os.remove(file_name)
    print("File Removed")

def printReceipt(message):
    print("printing: " + message)
    os.system("echo \"" + message + "\n\n\n\" > /dev/usb/lp0")
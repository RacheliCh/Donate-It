from picamera import PiCamera
from time import sleep
from urllib.request import urlopen
from datetime import datetime, timedelta
import os
from firebase_storage import *

def set_system_time():
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
    set_system_time()
    # os.system("export DISPLAY=\":0\"") # not working, still need to run manualy in terminal !!!!!!!
    os.system("xdotool mousemove 800 600")

def cameraInitialize():
    camera = PiCamera()
    camera.framerate=30
    camera.resolution=(1080,1080)
    return camera

# capture picture upload to firebse and return the url
def takePictureAndUpload(camera):
    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    print("pushed")
    now = datetime.now()
    dt = now.strftime("%d%m%y%H%M%S")
    img_name = dt + ".jpg"
    camera.capture(img_name)
    print(img_name+" saved")

    storageUploadImage(img_name)

    print("Image sent")
    os.remove(img_name)
    print("File Removed")

    img_url = storageGetImageUrl(img_name)
    return dt , img_url

def printReceipt(message):
    print("printing: " + message)
    os.system("echo \"" + message + "\n\n\n\" > /dev/usb/lp0")
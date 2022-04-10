from datetime import datetime
from picamera import PiCamera
from time import sleep
import os
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyAazJ0F0VxXBfeDSivJB8G9eOq09qUxoDE",
    'authDomain': "test-86af6.firebaseapp.com",
    'databaseURL': "https://test-86af6-default-rtdb.firebaseio.com",
    'projectId': "test-86af6",
    'storageBucket': "test-86af6.appspot.com",
    'messagingSenderId': "301273604843",
    'appId': "1:301273604843:web:ecc57177d2320b91e314ae",
    'measurementId': "G-NNRK6XG1YY"
}

#  "serviceAccount": "firebaseServiceAccountCredentials.json"

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

# Create Authentication user account in firebase  
auth = firebase.auth()

# Enter your user account details 
email = "donate.it100@gmail.com"
password = "DonateIt100"

try:
    auth.create_user_with_email_and_password(email, password)
except Exception as e:
    attrs = vars(e)
    print(attrs)

camera = PiCamera()

print("pushed")
now = datetime.now()
dt = now.strftime("%d%m%Y%H:%M:%S")
name = dt + ".jpg"
camera.capture(name)
print(name+" saved")
storage.child(name).put(name)
print("Image sent")
os.remove(name)
print("File Removed")
camera.close()

token = "AAAARiVOYus:APA91bEOKXx81_dYtk_vmPO9LMFRR1LEQ3ipe3eqIA3NX8XGxIrJMliPg_vE8TvojkC2iFNvM3NECjJaS2pyl067g43vE8PCQYZ4e6P_0E-ds5NACq-sMgH-1dPENXP9kJUOydbrqgY3"
imageUrl = storage.child("1004202217:51:26.jpg").get_url(token)
print(imageUrl)

# not good - send to realtime
db = firebase.database()
data = {"name": "aaa"}
db.child("c1").push(data)

exit()
# not working - upload to firestore

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('/home/pi/Documents/project/Donate-It/firebaseServiceAccountCredentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
data = {"name": "Smith"}
db.collection(u'c1').add(data)
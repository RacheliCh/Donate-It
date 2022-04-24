from datetime import datetime
import os
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyBfYHarCf_LRBBrQSUCzIlO9PEVj8oGQRE",
    'authDomain': "donateit-d274f.firebaseapp.com",
    'databaseURL': "https://test-86af6-default-rtdb.firebaseio.com",
    'projectId': "donateit-d274f",
    'storageBucket': "donateit-d274f.appspot.com",
    'messagingSenderId': "508136337397",
    'appId': "1:508136337397:web:98fb282ad141c254b03abc",
    'measurementId': "G-BGC246215Q"
}

#  "serviceAccount": "firebaseServiceAccountCredentials.json"

def storageInitialize():
    global firebase
    global storage
    firebase = pyrebase.initialize_app(firebaseConfig)
    storage = firebase.storage()

def storageUploadImage(img_name):
    storage.child(img_name).put(img_name)

def storageGetImageUrl(img_name):
    # token = "AAAAdk9JL_U:APA91bEuKaFKQfpOYc_MU0ZEQJKGqxXwZOVAKPX-qxQO6hj0_9qBKLgllT1mgHJlWuts1ExHiCdD8rRfO8-3FIDFAQ0cF7fezu9eyjIt0THg382KXqAked4cd9BWm9g3ZcCJijd0sHix"
    image_url = storage.child(img_name).get_url(None) # or token ?
    print(image_url)
    return image_url

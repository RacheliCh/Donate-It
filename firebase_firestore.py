import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def firestoreInitialize():
    global db
    cred = firebase_admin.credentials.Certificate("/home/pi/Documents/project/Donate-It/DonateItServiceAccountKey.json") # /home/pi/Documents/project/Donate-It/
    firebase_admin.initialize_app(cred)
    db = firestore.client()

def firestoreAddDocument(doc):
    db.collection('items').add(doc)
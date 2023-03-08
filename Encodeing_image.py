
# Importing Module We Need 

import cv2
import face_recognition
import pickle
import os
import checkinternet as ch
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage

# Intialize the Firebase Datebase 

Key = credentials.Certificate("servicekey.json")
firebase_admin.initialize_app(Key, {
    "databaseURL" : "https://icore-attendence-system-default-rtdb.firebaseio.com/",
    'storageBucket': "icore-attendence-system.appspot.com"
})

# Assign the Variable 

is_Access = ch.is_connect()
folderPath = 'Image/Images'
Image_Path = os.listdir(folderPath)
ImageArray = []
EmployInfo_Id = []
Counter = 0
# print(Image_Path)

# Sperate Images into ID and Path

for img in Image_Path:
    ImageArray.append(cv2.imread(os.path.join(folderPath, img)))
    EmployInfo_Id.append(os.path.splitext(img)[0])

    if is_Access :
        fileName = f'{folderPath}/{img}'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
        
        # Counter += 1
# if Internet Connected this store the Image in the Firebase Storage Bucket

# print(img)
# print(EmployInfo_Id)
# print(ImageArray)

# Starting Encoding Function to Store The Image in the `p` format
# p format formaly used for binary store the value of image

def Convert_Encodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = [face_recognition.face_encodings(img)][0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ")
EncodeArray_Known = Convert_Encodings(ImageArray)
# print(EncodeArray_Known)
EncodeArray_KnownWithIds = [EncodeArray_Known, EmployInfo_Id]
# print(len(EncodeArray_KnownWithIds))
# print(EncodeArray_KnownWithIds)
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(EncodeArray_KnownWithIds, file)
file.close()
print("File Saved")
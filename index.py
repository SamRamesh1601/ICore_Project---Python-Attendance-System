# Importing Module We Need 

import numpy as np
import cv2
import ctypes
import os
import pickle
import face_recognition
import FullBody_DetectionModule as f
# import cvzone
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import checkinternet as ch
from datetime import datetime
import warnings
# Intialize the Firebase Datebase 

Certifiacte_Key = credentials.Certificate("servicekey.json")
firebase_admin.initialize_app(Certifiacte_Key, {
    "databaseURL" : "https://icore-attendence-system-default-rtdb.firebaseio.com/",
    'storageBucket': "icore-attendence-system.appspot.com"
})

# Set the Camera Or Video Capture 

# cap=cv2.VideoCapture("C:/Users/SAM/Desktop/Attandance_project/1.mp4")
cap=cv2.VideoCapture(0)
# print(str("WIDTH : "),cv2.CAP_PROP_FRAME_WIDTH, str("HEIGHT : ") ,cv2.CAP_PROP_FRAME_HEIGHT)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640) 

# Assign the Variable 

Active =ch.is_connect()
bucket = storage.bucket()
# ptime = 0
Index_ModeImage = 0
Timing_Counter = 0
id = -1
EmployeeImage = []

floderpath = os.getcwd() + "/Image/modes"
modepath = os.listdir(floderpath)
imgmodelist = []
dector = f.FullBody_Detector() # Create FaceMesh 468 Locations

for path in modepath :
    imgmodelist.append(cv2.imread(os.path.join(floderpath,path))) # Store Image of Modes Folder

imgBackground = cv2.imread("Image/3.png") # set the Background Image

# print(len(imgmodelist))
# print(type(imgbackground))
# print(type(cap))

print(" loaded Encoding file....")
file = open( os.getcwd() +'/EncodeFile.p', 'rb')
encodelistknownwithid = pickle.load(file)
file.close()
# print(len(encodelistknownwithid))
# print(encodelistknownwithid)
encodelistknown , EmployeeId = encodelistknownwithid[0] , encodelistknownwithid[1]
# print(EmployeeId)
# print(len(encodelistknown))
print(" Encoding Loaded Compelete")

# Starting Interface of User

if not Active:
    print(" This process Required Internet Services")
    print(" so Kindly Connect BroadBand or WIfi")
    print("")
    ctypes.windll.user32.MessageBoxW(0,"Need Internet Connection ",'Warnings!',16)


while True:

    if not cap.isOpened():
        print(" Please Open Camera Device or Play Video MP4 ")
        break

    success , video = cap.read()

    Video_resize = cv2.resize(video, (0, 0), None, 0.25, 0.25)
    Video_resize = cv2.cvtColor(Video_resize , cv2.COLOR_BGR2RGB)

    Facecurframe = face_recognition.face_locations(Video_resize)
    # print(len(Facecurframe))
    Encodecurframe =face_recognition.face_encodings(Video_resize,Facecurframe)
    #print(Encodecurframe)
    #print(encodelistknown[0])
                      
    # print(type(Facecurframe))
    # print(type(Encodecurframe))
    # print(Facecurframe)
    # print(Encodecurframe)
    video , facemesh_data = dector.findFaceMesh(video)  # Create FaceMesh of Face detection 
    # video , facedetect_data = dector.finddetectface(video) # Create Rectangle of Face detection

    imgBackground[ 240:240 + 480,15:15+ 640] = video # Set Width Position and Height Position Video of Camera To Background Image
    # imgbackground[ 1180:1180 + 720,340:340+ 1280] = video # Set Video of MP4 Files To Background Image
    imgBackground[50:50 + 600,905:905 + 350] = imgmodelist[Index_ModeImage] # Set Actice bar of Image To Background Image

    # if len(face_recognition.face_encodings(face_recognition.load_image_file("Image/Images/355652.jpg"))) > 0:
        # print("test passwed")
        # print(face_recognition.face_distance(encodelistknown, Encodecurframe))
    if Facecurframe:
        for lm_encodelistknown ,Encode in zip(encodelistknown, Encodecurframe):
            # print(Encodecurframe) 
            # print(Facecurframe)
            # print(type(Encodecurframe),type(Facecurframe))
            faceDis =face_recognition.face_distance(encodelistknown, Encode)
            # faceDis = face_recognition.face_distance(encodelistknown, Encode)
            warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
            # face_matches = np.array( face_recognition.compare_faces(encodelistknown, Encode),dtype=object)
            face_matches =  np.ndarray(face_recognition.compare_faces(lm_encodelistknown,Encode),dtype=object)
            #print("face_matches", face_matches)
            print("faceDis", faceDis)
            print(type(faceDis),type(face_matches))

            matchIndex = np.argmin(faceDis)
            # print("Match Index", matchIndex)

            if face_matches[matchIndex]:
                # print("Known Face Detected")
                # print(EmployeeId[matchIndex])
                # y1, x2, y2, x1 = Facecurframe
                # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                # bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                # imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=1)
                id = EmployeeId[matchIndex]

                # if Timing_Counter == 0:
                #     cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                #     cv2.imshow("Face Attendance", imgBackground)
                #     cv2.waitKey(1)
                #     Timing_Counter = 1
                #     Index_ModeImage = 1

        if Timing_Counter != 0:

            if Timing_Counter == 1:

                # Get the FireBase Database 
                # get from directory Previous Database Directory Empolyee 

                Employee_Information = db.reference(f'Employee/{id}').get() 
                # print(Employee_Information)

                # Get the Image from the storage

                blob = bucket.get_blob(f'Image/Images/{id}.jpg')
                Bufferd_Array = np.frombuffer(blob.download_as_string(), np.uint8)
                EmployeeImage = cv2.imdecode(Bufferd_Array, cv2.COLOR_BGRA2BGR) # Decode the Iamge from Storage to BGR 2 RGB

                # Update data of attendance

                datetimeObject = datetime.strptime(Employee_Information['Last_Attendance'],"%Y-%m-%d %H:%M:%S")
                secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                # print(secondsElapsed)

                if secondsElapsed > 30:

                    ref = db.reference(f'Employee/{id}')
                    Employee_Information['Total_Attendance'] += 1
                    ref.child('Total_Attendance').set(Employee_Information['Total_Attendance'])
                    # print(f"Current Date is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    ref.child('Last_Attendance').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                else:
                    Index_ModeImage = 3
                    Timing_Counter = 0
                    # imgBackground[44:44 + 633, 808:808 + 414] = imgmodelist[Index_ModeImage]
                    imgBackground[50:50 + 600,905:905 + 350] = imgmodelist[Index_ModeImage]

            if Index_ModeImage != 3:

                if 10 < Timing_Counter < 20:
                    Index_ModeImage = 2

                # imgBackground[44:44 + 633, 808:808 + 414] = imgmodelist[Index_ModeImage]
                imgBackground[50:50 + 600,905:905 + 350] = imgmodelist[Index_ModeImage]

                if Timing_Counter <= 10:
                    cv2.putText(imgBackground, str(Employee_Information['Total_Attendance']), (861, 125), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(Employee_Information['Dept']), (1006, 550), cv2.FONT_HERSHEY_PLAIN, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(id), (1006, 493),cv2.FONT_HERSHEY_PLAIN, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(Employee_Information['Standing']), (910, 625),cv2.FONT_HERSHEY_PLAIN, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(Employee_Information['Total_Year']), (1025, 625),cv2.FONT_HERSHEY_PLAIN, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(Employee_Information['Starting_year']), (1125, 625),cv2.FONT_HERSHEY_PLAIN, 0.6, (100, 100, 100), 1)

                    (w, h), _ = cv2.getTextSize(Employee_Information['Name'], cv2.FONT_HERSHEY_PLAIN, 1, 1)
                    offset = (414 - w) // 2 # find right width of Text in Mode Image 
                    cv2.putText(imgBackground, str(Employee_Information['Name']), (808 + offset, 445),cv2.FONT_HERSHEY_PLAIN, 1, (50, 50, 50), 1)

                    imgBackground[175:175 + 216, 909:909 + 216] = EmployeeImage

                Timing_Counter += 1

                if Timing_Counter >= 20:
                    Timing_Counter = 0
                    Index_ModeImage = 0
                    Employee_Information = []
                    EmployeeImage = []
                    # imgBackground[44:44 + 633, 808:808 + 414] = imgmodelist[Index_ModeImage]
                    imgBackground[50:50 + 600,905:905 + 350] = imgmodelist[Index_ModeImage]
    else:
        Index_ModeImage = 0
        Timing_Counter = 0

    # imgbackground=cv2.resize(imgbackground,(1200,700)) 
    # ctime = time.time()
    # fps = 1/(ctime - ptime)
    # ptime = ctime 
    # cv2.putText(imgbackground,f"{int(fps)}",(250,50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
    cv2.imshow(" Interface Of Attendence System ",imgBackground)
    cv2.waitKey(1)
    # print(CLEAR)
    # break

# else:
#     print(" Please Continue With Turn On InterNet Connection")
#     print(" Database Required Connection ")
#     ctypes.windll.user32.MessageBoxW(0,"Need Internet Connection ",'Warnings!',16)

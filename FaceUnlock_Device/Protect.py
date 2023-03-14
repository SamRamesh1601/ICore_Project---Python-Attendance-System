
import face_recognition
import cv2
import numpy as np
import pyautogui
from selenium import webdriver
import time
import os
import socket


def is_connect():
    try:
        x=socket.create_connection(("www.google.com",80))
        if x is not None:
            x.close()
        return True
    except OSError:
        pass
    return False

gmail = "rameshsam1601@gmail.com"
password = "sam5065ram"

video_capture = cv2.VideoCapture(0)

root_image = face_recognition.load_image_file("obama.png")
root_encoding = face_recognition.face_encodings(root_image)


known_face_encodings = [
    root_encoding,
]
known_face_names = [
    "Sam",
]

while is_connect():
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    name = "Sam"

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    if name != "Your Name":
        driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\Chrome.exe")
        driver.get("https://www.google.com/android/find")
        time.sleep(2)
        pyautogui.typewrite(gmail)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.typewrite(password)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.click(x=85,y=231)
        time.sleep(2)
        pyautogui.click(x=200,y=495)
        pyautogui.hotkey('ctrlleft', 'altleft', 'l')

    else:
        print("Welcome BOSS")
        os.system("gnome-terminal")

    # Display the resulting image
    cv2.imshow('Video', frame)
    k= cv2.waitKey(1)
    
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
        
else:
    print(" PLease Turn ON Internet Connection ")

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

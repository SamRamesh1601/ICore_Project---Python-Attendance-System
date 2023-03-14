import cv2
import numpy as np
import face_recognition
import os

print(os.getcwd())
img = face_recognition.load_image_file("1.jpg")
imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("2.jpg")
imgrgbTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# cv2.imshow("Image 1",imgrgb)
# cv2.imshow("testing Image",img)
faceloc = face_recognition.face_locations(imgrgb)
encode = face_recognition.face_encodings(imgrgb)

# print(faceloc)
# print(encode)
# cv2.rectangle(img, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (155, 0, 255), 2)

facelocTest = face_recognition.face_locations(imgrgbTest)
encodeTest = face_recognition.face_encodings(imgrgbTest)

# print(facelocTest)
# print(encodeTest)

if len(faceloc) > 1 or len(facelocTest) > 1 :
    print(" The Image containes Face ")
else:
    print(" The Image don't have Face,So Change Images ")
# cv2.rectangle(imgTest, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (155, 0, 255), 2)

results = face_recognition.compare_faces(encode, encodeTest)
faceDis = face_recognition.face_distance(encode, encodeTest)
print(results, faceDis)
# cv2.putText(imgrgbTest, f'{results} {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

while faceloc and facelocTest:
    cv2.imshow('Santha', img)
    cv2.imshow('Testing Rat', imgTest)
    cv2.waitKey(1)
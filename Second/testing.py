import cv2
import numpy as np
import face_recognition

img = cv2.imread('C:/Users/SAM/Desktop/ICore_project/Image/Images/355652.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgTest = cv2.imread('C:/Users/SAM/Pictures/Camera/IMG_20221223_132759.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
cv2.imshow("Image 1",img)
cv2.imshow("testing Image",img)
faceloc = face_recognition.face_locations(img)
encode = face_recognition.face_encodings(img)
print(len(faceloc))
print(len(encode))
# cv2.rectangle(img, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (155, 0, 255), 2)

facelocTest = [face_recognition.face_locations(imgTest)][0]
encodeTest = [face_recognition.face_encodings(imgTest)][1]

print(len(facelocTest))
print(len(encodeTest))

# cv2.rectangle(imgTest, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (155, 0, 255), 2)

results = face_recognition.compare_faces([encode], encodeTest)
faceDis = face_recognition.face_distance([encode], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('Santha', img)
cv2.imshow('Testing Rat', imgTest)
cv2.waitKeys(0)

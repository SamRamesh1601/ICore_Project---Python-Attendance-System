
import cv2
from datetime import datetime 
# Curent_Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(Curent_Date)
# while True:
#     cv2.imshow(" Interface of Face recognition ",img)
#     cv2.waitKey(1)

# FaceCascade = cv2.CascadeClassifier(cv2.data.haarcascades / 'haarcascade_frontalface_default.xml')
img = cv2.imread("C:/Users/SAM/Desktop/ICore_project/Image/Images/355652.jpg")
imggrey = cv2.cvtColor( img,cv2.COLOR_BGR2GRAY)
imgrgb = cv2.cvtColor( img,cv2.COLOR_BGR2RGB)
# faces = FaceCascade.detectMultiScale(imggrey , 1.1 , 4)

# for (x,y,w,h) in faces :
    # cv2.rectangle(img,(x,y),(x+w , y+h),(0,255,0),2)

cv2.imshow("Img",imggrey)
cv2.imshow("Img",img)
cv2.imshow("Img",imgrgb)
cv2.waitKey(0)
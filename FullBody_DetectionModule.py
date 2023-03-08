
import cv2
import mediapipe as mp
import numpy as np
import time

class FullBody_Detector():

    def __init__(self,mode=False , complexity = 1, landmark = True ,dectcon = 0.5 , trackcon = 0.5, maxhands=2 , maxface = 2):

        # Basic Module Variable

        self.mode = mode
        self.maxhands = maxhands
        self.maxface = maxface
        self.complexity = complexity
        self.landmark = landmark
        self.dectcon = dectcon
        self.trackcon = trackcon

        # BodyPose Tracking Module 

        self.npPose = mp.solutions.pose
        self.Pose = self.npPose.Pose(self.mode , self.complexity, self.landmark , min_detection_confidence= 0.5 , min_tracking_confidence = 0.5 )
        self.npdraw = mp.solutions.drawing_utils
        self.color = self.npdraw.DrawingSpec(color=(0,255,0))
        self.color1 = self.npdraw.DrawingSpec(color=(0,0,0),thickness=2)
        
        # Hand Tracking Module

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode , self.maxhands , min_detection_confidence = 0.5 , min_tracking_confidence = 0.5)
        
        # FaceMesh Tracking Module

        self.npfacemesh=mp.solutions.face_mesh
        self.face_mesh = self.npfacemesh.FaceMesh(self.mode , self.maxface ,min_detection_confidence = 0.5 , min_tracking_confidence = 0.5)
        self.drawspc = self.npdraw.DrawingSpec(color=(0,0,0),thickness=1, circle_radius=0)

        # Face Detection Module

        self.npfacedetect = mp.solutions.face_detection
        self.face_detection = self.npfacedetect.FaceDetection(0.75)

    def findbodypose(self,img,draw = True):

        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.Pose.process(imgrgb)
        if self.results.pose_landmarks :
            if draw :
                self.npdraw.draw_landmarks(img,self.results.pose_landmarks,self.npPose.POSE_CONNECTIONS,self.color,self.color1)
        return img

    def getbodyposition(self,img,draw=True):
        lmlist = []
        if self.results.pose_landmarks :

            for id1, lm in enumerate(self.results.pose_landmarks.landmark):
                h , w , c =  img.shape
                cx , cy = int(lm.x*w) , int(lm.y*h)
                lmlist.append([id1,cx,cy])
                if draw:
                    # cv2.putText(img,str(id1),(cx,cy),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),4)
                    cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)

        return lmlist
    
    def findhand(self,img,draw=True):

        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgrgb)

        if self.results.multi_hand_landmarks :
            for handlms in self.results.multi_hand_landmarks :
                if draw:
                    self.mpdraw.draw_landmarks(img,handlms,self.mpHands.HAND_CONNECTIONS)
        # print(len(self.results.multi_hand_landmarks))

        return img
                
    def gethandpositons(self,img,handno=0, draw = True):
        
        lmlist = []
        if self.results.multi_hand_landmarks :
            myhand = self.results.multi_hand_landmarks[handno]
            for id1 ,lm in enumerate(myhand.landmark):
                # print(id,lm)
                h , w, c = img.shape
                cx,cy = int(lm.x*w) , int(lm.y*h)
                # print(id1,cx,cy)
                cv2.putText(img,str(id1),(cx,cy),cv2.FONT_HERSHEY_PLAIN,1.2,(0,255,0),2)
                lmlist.append([id1,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
        return lmlist

    def findFaceMesh(self,img,draw = True):
        
        self.imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.face_mesh.process(self.imgrgb)

        faces = []

        if self.results.multi_face_landmarks :
            for facelms in self.results.multi_face_landmarks :
                if draw:
                    self.npdraw.draw_landmarks(img ,facelms ,self.npfacemesh.FACEMESH_CONTOURS ,self.drawspc,self.drawspc)
                
                face = []

                for id1,lm in enumerate(facelms.landmark):
                    # print(lm)
                    ih, iw, ic = img.shape
                    x , y = int(lm.x*iw) , int(lm.y*ih)
                    # print(str(id1))
                    # cv2.putText(img,str(id1),(x,y),cv2.FONT_HERSHEY_PLAIN,0.7,(0,255,0),1)
                    # print(id1,x,y)
                    face.append([x,y])
                faces.append(face)    

        return img , faces

    def finddetectface(self,img,draw=True):

        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results =self.face_detection.process(imgrgb)
        bbox = []
        if self.results.detections :
            for id2 ,detection in enumerate(self.results.detections):
                
                obj = detection.location_data.relative_bounding_box
                ih , iw , ic = img.shape
                cx = int(obj.xmin * iw) , int(obj.ymin * ih) , int(obj.width * iw) , int(obj.height * ih)              
                bbox.append([id2,cx,detection.score])
                cv2.rectangle(img,cx,(255,0,255),2)
                cv2.putText(img,f' {int(detection.score[0]*100)}% ',(cx[0],cx[1]),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),6)
        return img , bbox
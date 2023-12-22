#!/usr/bin/env python3
import cv2  
import threading
import time
import datetime 
import os
os.chdir("/home/zesma/Desktop/project/")

class Camera():

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')  
        self.cap = None
        self.video_file = 'video.mp4'
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = None
        self.recording_duration = 1.0
        self.start_time = 0
        self.record_lock = threading.Lock()
        self.count = 1
        self.exit_flag = False

    def video(self):
        record_duration = 5
        cap = cv2.VideoCapture(0)  
        while 1:  
        
            ret, img = cap.read() 

            current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            cv2.putText(img, current_time, (449, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (193, 58, 21), 1, cv2.LINE_AA)
            if self.out is None:
                    self.out = cv2.VideoWriter(self.video_file, self.fourcc, 25.0, (640, 480))
                    self.start_time = cv2.getTickCount()

            self.out.write(img)

            if (cv2.getTickCount() - self.start_time) / cv2.getTickFrequency() > record_duration:
                    self.out.release()
                    self.out = None
                    break
        cap.release()  
        cv2.destroyAllWindows()

         

   
  




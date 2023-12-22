import threading
import cv2  
import time
import os
import datetime
os.chdir("/home/zesma/Desktop/project/")


class CatDetection: 
      
    def _init_(self): 
        self._running = True
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')  

      
    def terminate(self): 
        self._running = False


    def run(self): 
        cap = cv2.VideoCapture(0) 
        count = 1

        while self._running: 
            ret, img = cap.read()  

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

 

            if len(faces) > 0:
                current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                cv2.putText(img, current_time, (449, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (193, 58, 21), 1, cv2.LINE_AA) 

                # Save the face images at 2-second intervals
                if count % 25 == 0:  # Assuming 25 frames per second, 2 seconds = 50 frames
                    filename = f'image_{count // 25}.png'
                    cv2.imwrite(filename, img)
                    print(f"Image {count // 25} saved.")
                count += 1

                if count // 25 > 1:
                        print("fotolar çekildi")
                        count = 1
                        self._running = False
                        break
            if self._running == False:
                break

        cap.release()  
        cv2.destroyAllWindows()
        self.terminate()
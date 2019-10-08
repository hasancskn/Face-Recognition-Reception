#!/usr/bin/env python
#-*-coding:utf-8-*-
from gtts import gTTS
import cv2
import os
import time


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
names = ['None', 'Hasan']

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()
    img = cv2.flip(img, -1)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Tanıyabilme oranını veriyor
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "Tanıyamadım"
            confidence = "  {0}%".format(round(100 - confidence))
        #Kamerayı açıp üzerinde isim görmek istersek kullanabiliriz
        #cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        #cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

    print("Tanımaya Çalışıyorum")
    if id=="Hasan":
        print("tanıdım")
        tts = gTTS("Hoşgeldin Hasan, Seni çok özledik, Öğrenciler Seni Bekliyor", lang="tr")
        tts.save("HosgeldinHasan.mp3")
        os.system("HosgeldinHasan.mp3")
        print("kaydettim")
        time.sleep(7)
        def kill_by_process_name_shell(name):
            os.system("taskkill /f /im " + name)
        kill_by_process_name_shell("Music.UI.exe")
        time.sleep(3)
        id=""
cam.release()
cv2.destroyAllWindows()

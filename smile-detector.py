# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:29:45 2024

@author: Sahil
"""

import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\\Sahil\\Desktop\\Projects\\Smile-Detector\\haarcascade_face.xml')
eye_cascade =cv2.CascadeClassifier('C:\\Users\\Sahil\\Desktop\\Projects\\Smile-Detector\\haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('C:\\Users\\Sahil\\Desktop\\Projects\\Smile-Detector\\haarcascade_smile.xml')

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        region_of_intrest_gray = gray[y:y+h, x:x+w]
        region_of_intrest_color = frame[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(region_of_intrest_gray, 1.7, 22)
        eyes = eye_cascade.detectMultiScale(region_of_intrest_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(region_of_intrest_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(region_of_intrest_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
    return frame

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

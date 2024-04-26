import cv2
import numpy as np

source = 0 #'video/people.mp4' #0
cap = cv2.VideoCapture(source)
ret, frame = cap.read()
frame1 = frame

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_c = frame.copy()
    diff = cv2.absdiff(frame1, frame)
    diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    rett, diff = cv2.threshold (diff, 10, 255, 0)
    cv2.imshow('diff', diff)
    contures, _ = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contures:
        if cv2.contourArea(c) > 10000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame_c,(x, y), (x + w, y + h), (255, 0, 0), 5)
    cv2.imshow('frame', frame_c)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    frame1 = frame

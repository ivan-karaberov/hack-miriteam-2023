import cv2
import asyncio
import requests
import numpy as np
from qreader import QReader


def findQR(frame, qreader):
    lst = []
    lower = np.array([0, 26, 144])
    higher = np.array([100, 255, 255])
    cat_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(cat_hsv, lower, higher)
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if(w > 90 and h > 90):
            ori = frame[y:y+h, x:x+w]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (36,255,12), 2)
            decoded_text = qreader.detect_and_decode(image=ori)
            if decoded_text:
                lst.append(decoded_text)
            if(len(lst)):
                return lst


async def cameraFactory():
    lst = []
    cap = cv2.VideoCapture('test2.mp4')
    qreader = QReader()
    while True:
        img, frame = cap.read()
        if not img:
            break
            # image = cv2.rectangle(frame, (450, 275), (450+510, 275+230), (255, 255, 255), 2)
        crop_img = frame[275:275+230, 450:450+510]
        # original = frame.copy()
        lst = findQR(crop_img, qreader)
        if lst != None and (len(lst) >= 1):
            break
    for i in lst:
        a = {
            'id':i[0],
            'status':1
            }
        print(a)
        requests.post('http://127.0.0.1:8000/update_data', json = a)


async def cameraStock():
    lst = []
    cap = cv2.VideoCapture('test3.mp4')
    qreader = QReader()
    while True:
        img, frame = cap.read()
        if not img:
            break
        # image = cv2.rectangle(frame, (100, 150), (100+710, 150+240), (255, 255, 255), 2)
        crop_img = frame[150:150+240, 100:100+710]
        # original = frame.copy()
        lst = findQR(crop_img, qreader)
        if lst != None and (len(lst) >= 1):
            break
    for i in lst:
        a = {
            'id':i[0],
            'status':2
            }
        print(a)
        requests.post('http://127.0.0.1:8000/update_data', json = a)


async def main():
    await cameraFactory()
    await asyncio.sleep(5)
    await cameraStock()

asyncio.run(main())
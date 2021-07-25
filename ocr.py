from typing import Text
import numpy as np
import cv2
import pytesseract as tess
import os 

from PIL import Image
from pytesseract import pytesseract

image_frames='image_frames'

def files():

    try:
        os.remove(image_frames)
    except OSError:
        pass

    if not os.path.exists(image_frames):
        os.makedirs(image_frames)

    cap=cv2.VideoCapture(0)
    return(cap)

def process(cap):

    index=0 
    while cap.isOpened():
        
        
        ret, frame =cap.read()
        #gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame',frame)

        if not ret:
            break 

        name='./image_frames/frame' + str(index) + '.png'

        if index%200==0:
           print('Extracting frames...' + name)
           cv2.imwrite(name,frame)
        index = index + 1
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def get_text():
    for i in os.listdir(image_frames):
        my_example= Image.open(image_frames +"/"+ i)
        text=pytesseract.image_to_string(my_example,lang='eng')
        print(text)

if __name__=='__main__':
    vid=files()
    process(vid)
    get_text()


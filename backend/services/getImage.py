import cv2
import os

def getImage():
      
    image_path = "./media/test2.jpg"
    im = cv2.imread(image_path)
 
    return im


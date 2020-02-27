# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:25:05 2020

@author: DINESH
"""

import cv2
#import numpy as np

def getTextOverlay(image):
    img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,output = cv2.threshold(img,3,255,cv2.THRESH_BINARY)    
    return output


if __name__ == '__main__':
    image = cv2.imread(r'C:\Users\DC44819\Pictures\simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite(r'C:\Users\DC44819\Pictures\simpons_text.png', output)
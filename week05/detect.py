# Calling module opencv(cv2)
import cv2
# Calling module numpy as np
import numpy as np
# Calling module math
import math

# A function convert image to  Grayscale + Blur
def preprocess(img):
    gray = cv2.cvtColor(img. cv2.COLR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (15, 15), 0)
    
    #
    result, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY)
    
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    opened =cv2.morphologyEx(th, cv2.MORPH_OPEN, k, interations-1)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, k, interations=1)
    return closed

def



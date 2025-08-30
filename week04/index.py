# OpenCv is used to for remember the face or object and upload (image, video, display) gestures
import cv2
# Numpy is for CalCulate math deep drive (vectors, matrices)
import numpy as np


img = cv2.imread('week04/Tung-Tung-Sahur-Plush.png')


if img is None:
    print("Image not found. Please check th file path.")
    exit()



kernel = np.array([[0, -1, 0],
[-1, 5, -1], 
[0, -1, 0]])

sharpened = cv2.filter2D(img, -1, kernel)



cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
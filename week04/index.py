# OpenCv is used to for remember the face or object and upload (image, video, display) gestures
import cv2
# Numpy is for CalCulate math deep drive (vectors, matrices)
import numpy as np

# The named of the library(cv2)
# .imread is to read the image
img = cv2.imread('week04/Tung-Tung-Sahur-Plush.png')

# if image not found, showed print text & exit the program
if img is None:
    print("Image not found. Please check th file path.")
    exit()
# Include kernel with 3x3 to adjust the image to blur & brightness

# Include kernel with 3x3 to adjust the image to blur & brightness
kernel = np.array([[0, -1, 0],
[-1, 5, -1], 
[0, -1, 0]])

# sharpened it's keep the value of filter2D of image to make a kernal 3x3
sharpened = cv2.filter2D(img, -1, kernel)


# Show an image with import
cv2.imshow('Sharpened Image', sharpened)
# waiting key for any press button for....
cv2.waitKey(0)
# close the program
cv2.destroyAllWindows()
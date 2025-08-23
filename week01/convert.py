# import it's mean a calling libraries or module OpenCV as cv2
import cv2

# The named of library [cv2] | .The named of a function()
# .imread() Used to read an images
img = cv2.imread("week01/Tung-Tung-Sahur-Plush.png")

# convert color of image to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert color of image to red green blue
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# .imshow() 1st arguement used for label 2nd arguement used for show the image (gray)
cv2.imshow("Show an image", gray)


# wait for the key to be press any button for.....
cv2.waitKey(0)
# Used to close all windows
cv2.destroyAllWindows()
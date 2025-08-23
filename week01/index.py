# import it's mean a calling libraries or modules OpenCV as cv2
import cv2

# print(cv2._version_)
# The named of library [cv2] | .The named of a function()
# .imread() Used to read an images
img = cv2.imread("week01/Tung-Tung-Sahur-Plush.png")

# .imwrite() Used to new an images
# Inculde 2 arguement (1.The named of new file ["new.png"], 2.image [or variable name])
cv2.imwrite("new.png", img)

# .imshow() Show an images
cv2.imshow("Show an image", img)

# .waitKey(0) Press any button for....
# .destroyAllWindows() Close a Windows()
cv2.waitKey(0)
cv2.destroyAllWindows()
 
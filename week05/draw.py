import cv2
import numpy as np
# Creat a white paper size 600 x 800 px
img = np.ones((600, 800, 3), dtype=np.uint8) * 255
# Create a rectangle, color BLUE (255, 0, 0)
cv2.rectangle(img, (100,50), (250, 200), (255, 0, 0), -1)
# Create a circle, color green -circle(img, center point, radius, colr, thickness)
cv2.circle(img, (400, 150), 100, (0, 255, 0), -1)
# Create a triangle color red with Polygon
pts = np.array([[500, 200], [700, 60], [750, 220]], np.int32)
cv2.fillPoly(img, [pts], (0, 0, 255))

for x in range(100, 750, 120):
    cv2.circle(img, (x, 350), 30, (0, 0, 0), -1)
    
cv2.putText(img, "Testing shapes and image", (50, 420),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (50, 50, 50), 2)

cv2.imwrite("shapes_test.png", img)
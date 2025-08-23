# import is a calling for library or module cv2 (OpenCV)
import cv2
# A function .VideoCapture(0) it means reading a videocapture
# 0 it means open webcam on your device local
cap = cv2.VideoCapture(0)
# if webcam is not found it means that it has already printed out "it's not Open"
if not cap.isOpened():
    raise IOError("It's not Open💩💩💀💀💀🌹🌹")
# while a function this is True, define variable ret & frame keep the videocapture
while True:
    ret, frame = cap.read()
    # if not found webcam it's just break the program or close the program
    if not ret:
        break
    # if condition it's True, show the webcam on your device local
    cv2.imshow("Webcam is available", frame)
    
    # if not found or found the webcam but the program doesn't open in 10 sec,
    # if nothing happens just close the program with key "q"
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Thiis function it's calling to use open webcam    
cap.release()
# Close all windows
cv2.destroyAllWindows()
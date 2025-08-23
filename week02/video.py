# The named of library
import cv2
# cap is a variable
# a function .VideoCapture("week02/cat-f1.mp4") means reading the videocapture
cap = cv2.VideoCapture("week02/cat-f1.mp4")

# if while program is True(conditional)
while True:
    # define a variable ret & frame to keep the videocapture
    ret, frame = cap.read()
    # if not found the video, just close the program
    if not ret:
        break
    # showing the video
    cv2.imshow("cat driving F1", frame)
    # In 10 sec, if nothing happens to the program(not found the video, just press the key "q")
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
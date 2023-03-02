import cv2
import time

cap = cv2.VideoCapture("DATA/video_example.mp4")
FPS = 25

if cap.isOpened() == False:
    print("Error opening the video file.")

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        time.sleep(1/FPS)
        cv2.imshow("frame", frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

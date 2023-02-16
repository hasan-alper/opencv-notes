import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# MACOS AND LINUX: *"XVID", WINDOWS *"VIDX"
writer = cv2.VideoWriter("DATA/video_capture_test.mp4", cv2.VideoWriter_fourcc(*"XVID"), 25, (width, height))

while True:
    ret, frame = cap.read()
    writer.write(frame)
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

        
cap.release()
writer.release()
cv2.destroyAllWindows()
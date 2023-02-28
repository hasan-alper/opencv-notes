import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):  # Create a function based on a CV2 Event
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0, 0, 255), 4)


# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# This names the window so we can reference it
cv2.namedWindow(winname="window_name")

# Connects the mouse button to our callback function
cv2.setMouseCallback("window_name", draw_circle)

while True:
    cv2.imshow("window_name", img)

    # If we've waited at least 0 ms AND we've pressed the q button
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

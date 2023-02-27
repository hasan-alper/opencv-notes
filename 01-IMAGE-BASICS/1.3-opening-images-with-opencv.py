import cv2

img = cv2.imread("DATA/puppy.jpg")

while True:
    cv2.imshow("window_name", img)

    # If we've waited at least 0 ms AND we've pressed the q button
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

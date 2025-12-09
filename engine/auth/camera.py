import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cam.isOpened():
    print("❌ Camera failed to open!")
else:
    print("✅ Camera opened successfully!")

while True:
    ret, frame = cam.read()
    if not ret:
        print("❌ Failed to read frame")
        break

    cv2.imshow("Test Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC
        break

cam.release()
cv2.destroyAllWindows()

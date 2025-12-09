import cv2
import os

def AuthenticateFace():

    cascade_path = "engine/auth/haarcascade_frontalface_default.xml"
    trainer_path = "engine/auth/trainer/trainer.yml"

    # Load recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(trainer_path)

    # Load cascade
    faceCascade = cv2.CascadeClassifier(cascade_path)

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    names = ["", "ismail"]

    valid_count = 0      # counts how many times accuracy is within range
    required_count = 5  # stop after 3 valid detections

    print("📸 Face Auth Running...")

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id_, acc = recognizer.predict(gray[y:y + h, x:x + w])
            accuracy = 100 - acc

            # Show accuracy
            cv2.putText(frame, f"{accuracy:.2f}%", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # CHECK: accuracy must be between 60 and 80
            if 60 < accuracy < 80:
                valid_count += 1
                print(f"✔ Valid Accuracy {accuracy:.2f}%  | Count = {valid_count}")
            else:
                valid_count = 0   # reset counter if out of range

            # STOP after 3 valid detections
            if valid_count >= required_count:
                print("🎉 FACE VERIFIED SUCCESSFULLY!")
                cam.release()
                cv2.destroyAllWindows()
                return 1   # success flag

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    return 0   # failed



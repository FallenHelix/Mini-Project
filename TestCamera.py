import cv2

def test_camera():

    # Load the cascade
    cascadeClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    print("Testing Camera , Press q to quit!")
    # To capture video from webcam.
    # CAP_DSHOW => Remove Warning Sign
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = cascadeClassifier.detectMultiScale(gray, 1.3, 5, minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,0),2)


        # Display
        cv2.imshow('Testing Camera, Press q to quit', img)

        # Stop if escape key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object
    print("Camera Realsed!!")
    cap.release()
    cv2.destroyAllWindows()

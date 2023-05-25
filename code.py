import cv2

# load pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')

# Check if the classifier object is not None
if face_cascade is not None:
    print("Classifier loaded successfully")
else:
    print("Error loading classifier")

# initialize video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, frame = cap.read()

    # Display the captured frame
    cv2.imshow('frame', frame)

    # Wait for user input to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


while True:
    # capture video frame
    ret, frame = cap.read()

    # convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # check if at least one face is present
    if len(faces) > 0:
        print("Person is present")
    else:
        print("No person detected")

    # display video frame
    cv2.imshow('frame', frame)

    # wait for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
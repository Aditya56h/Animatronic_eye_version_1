"""
Author: Aditya

This script is designed to detect faces and eyes in real-time using a webcam. 
It uses OpenCV for image processing and pySerial for serial communication. 
The script captures video from the webcam, detects faces and eyes in each frame, 
and sends commands to a serial port based on the position of the detected face.

The script is divided into several parts:
1. Importing the necessary libraries
2. Defining a function to set the resolution of the video capture
3. Initializing the serial port and video capture
4. Loading the cascade classifiers for face and eye detection
5. Starting the video capture loop, where each frame is processed and faces and eyes are detected
6. If a face is detected, the script calculates the error between the center of the face and the center of the frame, and sends this error to the serial port
7. If eyes are detected, the script sends a specific command to the serial port
8. The loop continues until the 'E' key is pressed
9. Finally, the serial port and video capture are closed, and all windows are destroyed
"""

# Import the required libraries
import cv2
import serial

# Function to set the resolution of the video capture
def set_res(cap, x, y):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(x))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(y))

# Initialize the serial port
ser = serial.Serial('COM4', 250000)

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Set the frame width and height
frame_w = 640
frame_h = 480
set_res(cap, frame_w, frame_h)

# Load the cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier('C:/Users/addua/Downloads/haarcascade_frontalface_default.xml')
EYE_cascade = cv2.CascadeClassifier('C:/Users/addua/Downloads/archive/haarcascade_eye.xml')

# Initialize error variables
err_x = 0
err_y = 0

# Start the video capture loop
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # If the frame is None, print an error message and continue
    if frame is None:
        print("Error: Frame is None")
        continue

    # Flip the frame and convert it to grayscale
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

    # For each detected face, draw a rectangle and detect eyes within the face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, "Aditya", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)
        faceROI = gray[y:y+h, x:x+w]
        eyes = EYE_cascade.detectMultiScale(faceROI, scaleFactor=1.05, minNeighbors=300,minSize=(5,5))

        # For each detected eye, draw a rectangle
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 0, 0), 2)

    # Display the frame
    cv2.imshow('frame', frame)

    # If 'E' is pressed, break the loop
    if cv2.waitKey(1) & 0xFF == ord('E'):
        break

    # If eyes are detected, print a message and write to the serial port
    if len(eyes)>0:
        print('the eyes are opened')
        ser.write((str(-30)+'z!').encode())
    else:
        print('the eyes are closed')   
        ser.write((str(70)+'z!').encode())

    # If faces are detected, calculate the error and write to the serial port
    if len(faces) > 0:
        face_center_x = faces[0,0] + faces[0,2] / 2
        face_center_y = faces[0,1] + faces[0,3] / 2
        err_x = 70 * (face_center_x - frame_w / 2) / (frame_w / 2)
        err_y =  100* (face_center_y - frame_h / 2) / (frame_h / 2)
        ser.write((str(err_x) + "x!").encode())        
        ser.write((str(err_y) + "y!").encode())        
        print("X: ", err_x, " ", "Y: ", err_y)

# Close the serial port and video capture, and destroy all windows
ser.close()
cap.release()
cv2.destroyAllWindows()

# Real-Time Eye Blink and Movement Detection with Servo Control

This project is designed to detect eye blinks and movements in real-time using a webcam, process the information using Python and OpenCV, and then control a servo motor based on the detected eye movements. The project uses a combination of software (Python, OpenCV) and hardware (webcam, Arduino, servo motor).

## Hardware Components

1. **Webcam**: Used to capture video frames in real-time.
2. **Arduino**: Used as an interface between the Python script and the servo motor. The Arduino receives commands from the Python script via serial communication and controls the servo motor accordingly.
3. **Servo Motor**: Moves based on the commands received from the Arduino.

## Software Components

1. **Python**: The main programming language used for this project.
2. **OpenCV**: A powerful computer vision library used for real-time image processing.
3. **Haar Cascade Classifiers**: Machine learning-based approach for object detection, used to detect faces and eyes in the video frames.

## Arduino Code Explanation

The Arduino code is responsible for receiving commands from the Python script via serial communication and controlling the servo motor based on these commands. 

The Arduino code uses the Adafruit_PWMServoDriver library to control a 16-channel PWM servo driver. It sets the PWM frequency for the servo driver to 60 Hz, which is the standard update frequency for analog servos. 

The Arduino code receives two types of commands from the Python script: one for eye blinks and one for eye movements. For eye blinks, the Arduino receives a command to move the servo to a specific position. For eye movements, the Arduino receives a command to move the servo based on the calculated error between the center of the face and the center of the frame.

## How It Works

The Python script captures video frames from the webcam in real-time. It then uses OpenCV and Haar cascade classifiers to detect faces and eyes in each frame. 

If eyes are detected, it means the eyes are open. If no eyes are detected for a certain period, it indicates a blink. 

The position of the detected face in the frame is used to calculate the direction of eye movement. This is done by calculating the error between the center of the face and the center of the frame.

These eye blink and movement detections are then sent as commands to the Arduino via serial communication. The Arduino controls the servo motor based on these commands.

## Usage

To use this project, you need to have the hardware components set up correctly, with the Arduino connected to the servo motor and the computer, and the webcam connected to the computer.

You also need to have Python installed on your computer, along with the OpenCV library. The Python script should be run on the computer, and the Arduino should be programmed to receive serial commands and control the servo motor accordingly.

## References
This project is inspired by and uses STL files from Will Cogley's original animatronic eye project. His work has been a great resource and inspiration in the development of this project.


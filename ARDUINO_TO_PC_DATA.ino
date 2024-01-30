/*
Author: Aditya


This script is designed to control a 16-channel PWM servo driver using the Adafruit_PWMServoDriver library. 
It uses the Wire library for I2C communication. The script initializes the servo driver, sets the PWM frequency, 
and then enters a loop where it drives each servo one at a time.

The script is divided into several parts:
1. Importing the necessary libraries
2. Defining the minimum and maximum pulse lengths
3. Initializing the servo driver
4. Defining the setup function, which initializes the serial port and the servo driver
5. Defining a function to set the PWM signal for a specific servo
6. Defining the main loop, which drives each servo one at a time by varying the pulse length
*/

// Import the required libraries
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// Initialize the servo driver with the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Define the minimum and maximum pulse lengths
#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)

// Initialize the servo number counter
uint8_t servonum = 0;

void setup() {
  // Initialize the serial port and print a message
  Serial.begin(250000);
  Serial.println("16 channel PWM test!");

  // Initialize the servo driver
  pwm.begin();
  
  // Set the PWM frequency for analog servos
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  delay(10);
}

// Function to set the PWM signal for a specific servo
// This function can be used as a drop-in replacement for 'analogWrite'
void setPWM(uint8_t num, uint16_t on, uint16_t off) {
  pwm.setPWM(num, on, off);
}

void loop() {
  // Print the current servo number
  Serial.println(servonum);

  // Drive the current servo by varying the pulse length from minimum to maximum
  for (uint16_t pulselen = SERVOMIN; pulselen < SERVOMAX; pulselen++) {
    pwm.setPWM(servonum, 0, pulselen);
  }

  delay(500);

  // Drive the current servo by varying the pulse length from maximum to minimum
  for (uint16_t pulselen = SERVOMAX; pulselen > SERVOMIN; pulselen--) {
    pwm.setPWM(servonum, 0, pulselen);
  }

  delay(500);

  // Increment the servo number counter
  servonum ++;
  if (servonum > 15) servonum = 0;
}


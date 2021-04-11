# Steering-Wheel
An OpenCV based minor project using Python and ArduinoIDE. It works as a virtual steering wheel for an arduino based-vehicle.
It works in such a way that it takes input from the web-cam for a paper with two large dots one green and another red.
Then based on their relative distance and angle, it decides whether to turn right/left or whether to go forward/backward.
It sends data to arduino using serial communication through python. And, depending on sent data, arduino takes action.

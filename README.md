# Steering-Wheel
An OpenCV based minor project using Python and ArduinoIDE. It works as a virtual steering wheel for an arduino based-vehicle.
It works in such a way that it takes input from the web-cam for a paper with two large dots one green and another red.
This is done using colour detection techniques of OpenCV. Colour detection is a easier in HSV, so I converted the BGR to HSV.
Now, we take their centres and calculate the number of pixels between them and also check if the dots are almost in straight line.
If these conditions are satisfied, then the bot is instructed to move forward or backward depending on the number of pixels.
If the dots are non-aligned by a certain pixel, then depending on whether red dot is to right or left of green dot, bot turns.
It sends data to arduino using serial communication through python. And, depending on sent data, arduino takes action.

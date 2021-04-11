import numpy as np
import cv2
import math
import serial
import time

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)

cam = cv2.VideoCapture(0)

#Global variables
rhmin,rsmin,rvmin,ghmin,gsmin,gvmin=0,0,0,0,0,0
rhmax,rsmax,rvmax,ghmax,gsmax,gvmax=180,255,255,180,255,255

def rhmin_change(val):
    global rhmin
    rhmin=val

def rhmax_change(val):
    global rhmax
    rhmax=val

def rsmin_change(val):
    global rsmin
    rsmin=val

def rsmax_change(val):
    global rsmax
    rsmax=val

def rvmin_change(val):
    global rvmin
    rvmin=val

def rvmax_change(val):
    global rvmax
    rvmax=val

def ghmin_change(val):
    global ghmin
    ghmin=val

def ghmax_change(val):
    global ghmax
    ghmax=val

def gsmin_change(val):
    global gsmin
    gsmin=val

def gsmax_change(val):
    global gsmax
    gsmax=val

def gvmin_change(val):
    global gvmin
    gvmin=val

def gvmax_change(val):
    global gvmax
    gvmax=val

cv2.namedWindow("Set Values", cv2.WINDOW_NORMAL)

#Trackbars for Red colour
cv2.createTrackbar('rhmin','Set Values',90,180,rhmin_change)
cv2.createTrackbar('rhmax','Set Values',180,180,rhmax_change)
cv2.createTrackbar('rsmin','Set Values',100,255,rsmin_change)
cv2.createTrackbar('rsmax','Set Values',255,255,rsmax_change)
cv2.createTrackbar('rvmin','Set Values',100,255,rvmin_change)
cv2.createTrackbar('rvmax','Set Values',255,255,rvmax_change)

#Trackbars for Green Colour
cv2.createTrackbar('ghmin','Set Values',30,180,ghmin_change)
cv2.createTrackbar('ghmax','Set Values',120,180,ghmax_change)
cv2.createTrackbar('gsmin','Set Values',95,255,gsmin_change)
cv2.createTrackbar('gsmax','Set Values',255,255,gsmax_change)
cv2.createTrackbar('gvmin','Set Values',92,255,gvmin_change)
cv2.createTrackbar('gvmax','Set Values',255,255,gvmax_change)

z="X"
z=input("Enter S to start and X to brake:")
while(1):
      
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
  
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
    # Set range for red color and 
    # define mask
    #90, 100, 100 
    red_lower = np.array([rhmin, rsmin, rvmin], np.uint8)
    red_upper = np.array([rhmax, rsmax, rvmax], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
  
    # Set range for green color and 
    # define mask
    # 30-120, 95, 92
    green_lower = np.array([ghmin, gsmin, gvmin], np.uint8)
    green_upper = np.array([ghmax, gsmax, gvmax], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
      
    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernel = np.ones((5, 5), "uint8")
      
    # For red color
    red_mask = cv2.dilate(red_mask, kernel)
    res_red = cv2.bitwise_and(frame, frame, mask = red_mask)
      
    # For green color
    green_mask = cv2.dilate(green_mask, kernel)
    res_green = cv2.bitwise_and(frame, frame, mask = green_mask)
   
    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      
    rx,ry,gx,gy=0,0,0,0
    for pic, contour in enumerate(contours):
      area = cv2.contourArea(contour)
      if(area > 300):
        (rx,ry), r = cv2.minEnclosingCircle(contours[0])
        cv2.circle(frame, (int(rx),int(ry)), 1, (0,0,0), 3)    
  
    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
      area = cv2.contourArea(contour)
      if(area > 300):
        (gx,gy), r = cv2.minEnclosingCircle(contours[0])
        cv2.circle(frame, (int(gx),int(gy)), 1, (0,0,0), 3)
    
    n,m,l= frame.shape
    q='P'
    if(z=='X'):
        write_read('X')
    if(z=="S"):
        if(ry-gy>=int(n/2) and q!='F'):
            write_read('F')
            q='F'
        elif(ry-gy<int(n/2) and q!='B'):
            write_read('B')
            q='B'
        if(rx-gx>40 and q!='R'):
            write_read('R')
            q='R'
        if(gx-rx>40 and q!='R'):
            write_read('L')
            q='L'
    cv2.imshow("Multiple Color Detection in Real-TIme", frame)
    cv2.waitKey(100)
cap.release()
cv2.destroyAllWindows()
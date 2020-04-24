import tkinter as tk
import RPi.GPIO as GPIO
import picamera
from time import sleep
camera = picamera.PiCamera()

camera.preview_fullscreen=False
camera.preview_window=(90,100,320,240)
camera.resolution=(640,480)
camera.start_preview() 

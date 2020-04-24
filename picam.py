from picamera import PiCamera
from time import sleep
import tkinter as tk
import RPi.GPIO as GPIO
import os,os.path

def PrendrePhoto():
    
    #sleep(2)
    liste = os.listdir("/home/pi/photo/projet/")
    NombreFichier = len(liste)
    camera.capture('/home/pi/photo/projet/test%s.jpg'% NombreFichier)
    camera.stop_preview()
    camera.preview_fullscreen=False
    camera.preview_window=(-7,-100, 1080, 600)
    camera.resolution=(1920,1080)
    camera.start_preview()
    
def EnvoitPhoto():
    
    
def CameraON():
    camera.preview_fullscreen=False
    camera.preview_window=(-7,-100, 1080, 600)
    camera.resolution=(1920,1080)
    camera.start_preview()

def CameraOFF():
    camera.stop_preview()
  
def EXIT():
    root.destroy
    camera.stop_preview()
    camera.close()
    quit()    

camera = PiCamera() # Créer une variable camera pour le module PiCamera
camera.rotation = 0
index = 0


root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("1080x100+0+500")#largeur * hauteur + X vers la droite + Y vers le bas
root.title("Camera Button Test")

root.buttonframe = tk.Frame(root)
root.buttonframe.grid(row=5, column=3, columnspan=2)

tk.Button(root.buttonframe, text='Start Camera', command=CameraON).grid(row=1, column = 1)
tk.Button(root.buttonframe, text='Kill Camera', command=CameraOFF).grid(row=1, column = 2)
tk.Button(root.buttonframe, text='Exit Program', command=EXIT).grid(row=1, column = 3)
tk.Button(root.buttonframe, text='PrendrePhoto', command=PrendrePhoto).grid(row=1, column = 4)

#root.overrideredirect(True)

root.mainloop()

#camera.start_preview()  # Affiche la vision de la caméra
#sleep(5)       # Attend 5 seconde
#while True:
    #index = index + 1
    #repository = '/home/pi/Desktop/' + str(index) + '.jpg'
    #print(repository)
    #camera.capture(repository)
#camera.stop_preview()   # Ferme la vision de la caméra
#sleep(0.1)
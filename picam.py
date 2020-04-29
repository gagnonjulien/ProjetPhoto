from picamera import PiCamera
import tkinter as tk
import os,os.path
import pysftp 

choices = ['off', 'auto', 'sunlight','cloudy','shade','tungsten','fluorescent','incandescent','flash','horizon']
effects = ['none','negative','solarize','sketch','denoise','emboss','oilpaint','hatch','gpen','pastel','watercolor','film','blur','saturation','colorswap','washedout','posterise','colorpoint','colorbalance','cartoon','deinterlace1','deinterlace2']


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
    myHostname = "192.168.0.109"
    myUsername = "pi"
    myPassword = "patate123"
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None 
    with pysftp.Connection(host = myHostname, username=myUsername, password=myPassword,cnopts=cnopts) as sftp:
        print("connection etablie")
        
        localFilePath = '/home/pi/photo/projet/'
        remoteFilePath = '/var/www/html/gallery/'
        sftp.put_d(localFilePath, remoteFilePath)
        sftp.close()
        
#menu debut        
        
def menu():
    camera.stop_preview()
    camera.preview_fullscreen=False
    camera.preview_window=(0,0, 540, 300)
    camera.resolution=(1920,1080)
    camera.start_preview()
    window = tk.Toplevel()
    
    tk.Scale(window, from_=30, to=100, orient=tk.HORIZONTAL, label = "Brightness", command=UpdateBrightness).grid(row=2,column=1)
    tk.Scale(window, from_=-100, to=100, orient=tk.HORIZONTAL, label = "Contrast", command=UpdateContrast).grid(row=2,column=2)
    tk.Scale(window, from_=-100, to=100, orient=tk.HORIZONTAL, label = "Sharpness", command=UpdateSharpness).grid(row=2,column=3)
    tk.Scale(window, from_=-100, to=100, orient=tk.HORIZONTAL, label = "Saturation", command=UpdateSaturation).grid(row=3,column=1)
    
    AWB_Var = tk.StringVar(root)
    AWB_Var.set(choices[0]) 
    AWB_Option = tk.OptionMenu(window, AWB_Var, *choices, command=SetAWB).grid(row=3,column=2)

    EFFECT_Var = tk.StringVar(root)
    EFFECT_Var.set(effects[0]) 
    EFFECT_Option = tk.OptionMenu(window, EFFECT_Var, *effects, command=SetEFFECTS).grid(row=3,column=3)
    
    
def UpdateBrightness(value):
    camera.brightness = int(value)
    
def UpdateContrast(value):
    camera.contrast = int(value)
    
def UpdateSharpness(value):
    camera.sharpness = int(value)
    
def UpdateSaturation(value):
    camera.saturation = int(value)

def SetAWB(var):
    camera.awb_mode = var

def SetEFFECTS(var):
    camera.image_effect = var

#def Zoom(var):
#    x = float("0."+var)
#    camera.zoom = (0.5,0.5,x,x)    
    
    
    
    
    
    
#menu fin    
    
    
def CameraON():
    camera.stop_preview()
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
tk.Button(root.buttonframe, text='EnvoitPhoto', command=EnvoitPhoto).grid(row=1, column = 5)
tk.Button(root.buttonframe, text='Menu', command=menu).grid(row=1, column = 6)




#root.overrideredirect(True)

root.mainloop()

